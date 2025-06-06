# Maintaining a local copy of server data

**Framework**: Swiftdata

Create and update a persistent store to cache read-only network data.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- macOS 14.0+
- Xcode 15.0+

#### Overview

This sample app displays a list that contains a day’s worth of earthquakes, showing their time, location, and size. To help people visualize the list, the app also pinpoints each earthquake on a map. You can select an earthquake in the list to highlight it on the map.

![A screenshot of the sample app on an iPad. The sidebar shows a list of earthquakes. An earthquake with magnitude 2.2 in Orange Cove, California is selected. The detail view shows a map centered on California with small multicolored circles scattered around to mark earthquake locations. One circle in the center of the map's visible region is highlighted.](https://docs-assets.developer.apple.com/published/6025cf0d8cff930d1e73c209a7a362b3/Maintaining-a-local-copy-of-server-data-1%402x.png)

The app downloads earthquake data from the network under the following assumptions:

-  — The app doesn’t need to synchronize local and remote changes. The server is always the source of truth.
-  — The app needs to provide a way to get an initial list of earthquakes and to periodically refresh that list.
-  — For example, the reported magnitude of an earthquake might change as additional measurements become available. The app needs to distinguish between new earthquakes and updates to previously downloaded ones.

The app uses SwiftData to persistently store the data that it downloads. By caching the data locally, the app reduces its need to access the server. SwiftData also makes it easy for the app to manage updates when downloading new data.

> **Note**: To learn how the app manages data presentation with queries and predicates, see [`Filtering and sorting persistent data`](filtering-and-sorting-persistent-data.md).

##### Define the Apps Data Model

The app represents the information it needs for its interface by defining a `Quake` class. The class definition includes the [`Model()`](model().md) macro to tell the system to store the data persistently using SwiftData:

```swift
import SwiftData

@Model
class Quake {
    @Attribute(.unique) var code: String
    var magnitude: Double
    var time: Date
    var location: Location
}
```

The model includes the following fields:

-  — By including the [`Attribute(_:originalName:hashModifier:)`](attribute(_:originalname:hashmodifier:).md) macro with the [`unique`](schema/attribute/option/unique.md) property option, the app ensures that SwiftData stores only one earthquake with a particular value for this field.
-  — The size of the earthquake.
-  — The moment in time when the earthquake happened, stored as a [`Date`](https://developer.apple.com/documentation/Foundation/Date) instance.
-  — A custom `Location` instance that contains a location name and map coordinates: ```swift
struct Location: Codable {
    var name: String
    var longitude: Double
    var latitude: Double
}
```

The `Quake` model can embed a location instance because the `Location` structure conforms to the [`Codable`](https://developer.apple.com/documentation/Swift/Codable) protocol.

##### Model the Server Data

The app loads data from a U.S. Geological Survey (USGS) server, which provides earthquake data in [`GeoJSON`](https://developer.apple.comhttps://earthquake.usgs.gov/earthquakes/feed/v1.0/geojson.php) format. To interpret this data, the app defines a `GeoFeatureCollection` structure with property names that match the names of relevant JSON properties:

```swift
struct GeoFeatureCollection: Decodable {
    let features: [Feature]

    struct Feature: Decodable {
        let properties: Properties
        let geometry: Geometry
        
        struct Properties: Decodable {
            let mag: Double
            let place: String
            let time: Date
            let code: String
        }

        struct Geometry: Decodable {
            let coordinates: [Double]
        }
    }
}
```

The structure and its substructures include elements relevant to this app, namely magnitude, time, and location information. They omit many other fields that the server provides because the app doesn’t need them. The structure also conforms to the [`Decodable`](https://developer.apple.com/documentation/Swift/Decodable) protocol so the app can use the structure to decode the downloaded data.

##### Download Data From the Server

To retrieve data, the app defines a `fetchFeatures()` method that uses a [`URLSession`](https://developer.apple.com/documentation/Foundation/URLSession) to store the earthquake JSON in a `data` property:

```swift
let session = URLSession.shared
guard let (data, response) = try? await session.data(from: url),
      let httpResponse = response as? HTTPURLResponse,
      httpResponse.statusCode == 200
else {
    throw DownloadError.missingData
}
```

The method then parses the data with a [`JSONDecoder`](https://developer.apple.com/documentation/Foundation/JSONDecoder) instance, according to the definition provided by the decodable `GeoFeatureCollection` structure:

```swift
do {
    let jsonDecoder = JSONDecoder()
    jsonDecoder.dateDecodingStrategy = .millisecondsSince1970
    return try jsonDecoder.decode(GeoFeatureCollection.self, from: data)
} catch {
    throw DownloadError.wrongDataFormat(error: error)
}
```

For other examples of decoding JSON data, see [`Using JSON with Custom Types`](https://developer.apple.com/documentation/foundation/archives_and_serialization/using_json_with_custom_types).

##### Translate Server Data Into Model Data

After retrieving a collection of features, the app interprets each feature as an earthquake. The `Quake` class defines a convenience initializer that creates a new earthquake from a feature instance:

```swift
convenience init(from feature: GeoFeatureCollection.Feature) {
    self.init(
        code: feature.properties.code,
        magnitude: feature.properties.mag,
        time: feature.properties.time,
        name: feature.properties.place,
        longitude: feature.geometry.coordinates[0],
        latitude: feature.geometry.coordinates[1]
    )
}
```

This enables the app to translate the data from a format that the server provides to a format that’s convenient for the app. For example, the initializer converts longitude and latitude coordinates that appear as anonymous elements in the feature’s `geometry.coordinates` array into named parameters.

##### Insert or Update New Earthquake Data

As the app creates new earthquake instances, it persistently stores any that have a magnitude greater than zero by calling the model context’s [`insert(_:)`](modelcontext/insert(_:).md) method for each one:

```swift
for feature in featureCollection.features {
    let quake = Quake(from: feature)

    if quake.magnitude > 0 {
        modelContext.insert(quake)
    }
}
```

The app runs this loop for both the initial download and later refresh operations. When the app saves the changes — which happens automatically in this case because the context’s [`autosaveEnabled`](modelcontext/autosaveenabled.md) property has the default value of `true` — SwiftData checks if the specified earthquake’s `code` parameter matches the code of an earthquake that’s already in the store. If so, the framework updates the stored earthquake’s other parameters using the values in the specified one. Otherwise, the framework adds a new earthquake to the store.

The insert method works for both creating and updating earthquake model instances because the model indicates that the `code` parameter is unique. This relies on the fact that the server ensures a unique, stable code for each earthquake event.

## See Also

- [Adding and editing persistent data in your app](adding-and-editing-persistent-data-in-your-app.md)
  Create a data entry form for collecting and changing data managed by SwiftData.
- [Deleting persistent data from your app](deleting-persistent-data-from-your-app.md)
  Explore different ways to use SwiftData to delete persistent data.
- [Defining data relationships with enumerations and model classes](defining-data-relationships-with-enumerations-and-model-classes.md)
  Create relationships for static and dynamic data stored in your app.
- [macro Model()](model().md)
  Converts a Swift class into a stored model that’s managed by SwiftData.
- [macro Attribute(Schema.Attribute.Option..., originalName: String?, hashModifier: String?)](attribute(_:originalname:hashmodifier:).md)
  Specifies the custom behavior that SwiftData applies to the annotated property when managing the owning class.
- [macro Transient()](transient().md)
  Tells SwiftData not to persist the annotated property when managing the owning class.
- [macro Relationship(Schema.Relationship.Option..., deleteRule: Schema.Relationship.DeleteRule, minimumModelCount: Int?, maximumModelCount: Int?, originalName: String?, inverse: AnyKeyPath?, hashModifier: String?)](relationship(_:deleterule:minimummodelcount:maximummodelcount:originalname:inverse:hashmodifier:).md)
  Specifies the options that SwiftData needs to manage the annotated property as a relationship between two models.
- [protocol PersistentModel](persistentmodel.md)
  An interface that enables SwiftData to manage a Swift class as a stored model.


---

*[View on Apple Developer](https://developer.apple.com/documentation/SwiftData/maintaining-a-local-copy-of-server-data)*