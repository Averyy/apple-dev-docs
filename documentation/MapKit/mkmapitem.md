# MKMapItem

**Framework**: MapKit  
**Kind**: class

A point of interest on the map.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.2+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class MKMapItem
```

## Mentions

- [Identifying unique locations with Place IDs](identifying-unique-locations-with-place-ids.md)

#### Overview

A map item includes a geographic location and any interesting data that might apply to that location, such as the address at that location and the name of a business at that address. You can also create a special `MKMapItem` object representing the user’s location.

Use this class to do the following:

- Share map-related data with the Maps app.
- Handle requests for directions that originate from the Maps app.

To display information in the Maps app, create an `MKMapItem` object with the information you want to display and call the [`openMaps(with:launchOptions:)`](mkmapitem/openmaps(with:launchoptions:).md) method. The Maps app displays that location on the map and shows the information you provide.

If you implement a routing app, the Maps app provides two `MKMapItem` objects representing the start and end points. Use the information in those two objects to plot the route and generate directions.

## Topics

### Creating map items
- [init(placemark: MKPlacemark)](mkmapitem/init(placemark:).md)
  Creates and returns a map item object using the specified placemark object.
- [class func forCurrentLocation() -> MKMapItem](mkmapitem/forcurrentlocation.md)
  Creates and returns a singleton map item object representing the user’s location.
### Accessing the map item attributes
- [MKMapItem.Identifier](mkmapitem/identifier-swift.class.md)
  A unique identifier for a place.
- [var alternateIdentifiers: Set<MKMapItem.Identifier>](mkmapitem/alternateidentifiers.md)
  A set of alternative identifiers for a place.
- [var identifier: MKMapItem.Identifier?](mkmapitem/identifier-swift.property.md)
  A unique identifier for a place.
- [var isCurrentLocation: Bool](mkmapitem/iscurrentlocation.md)
  A Boolean value that indicates whether the map item represents the user’s location.
- [var name: String?](mkmapitem/name.md)
  The descriptive name associated with the map item.
- [var placemark: MKPlacemark](mkmapitem/placemark.md)
  The placemark object containing the location information.
- [var pointOfInterestCategory: MKPointOfInterestCategory?](mkmapitem/pointofinterestcategory.md)
  The point-of-interest category for the map item.
- [var phoneNumber: String?](mkmapitem/phonenumber.md)
  The phone number associated with a business at the specified location.
- [var timeZone: TimeZone?](mkmapitem/timezone.md)
  The time zone of the specified location.
- [var url: URL?](mkmapitem/url.md)
  The URL associated with the specified location.
### Launching the Maps app
- [class func openMaps(with: [MKMapItem], launchOptions: [String : Any]?) -> Bool](mkmapitem/openmaps(with:launchoptions:).md)
  Opens the Maps app and displays the specified map items.
- [class func openMaps(with: [MKMapItem], launchOptions: [String : Any]?, completionHandler: ((Bool) -> Void)?)](mkmapitem/openmaps(with:launchoptions:completionhandler:).md)
  Opens the Maps app using the specified map items and options.
- [class func openMaps(with: [MKMapItem], launchOptions: [String : Any]?, from: UIScene?, completionHandler: ((Bool) -> Void)?)](mkmapitem/openmaps(with:launchoptions:from:completionhandler:).md)
  Opens the Maps app from a particular scene using the specified map items and options.
- [func openInMaps(launchOptions: [String : Any]?) -> Bool](mkmapitem/openinmaps(launchoptions:).md)
  Opens the Maps app and displays the map item.
- [func openInMaps(launchOptions: [String : Any]?, completionHandler: ((Bool) -> Void)?)](mkmapitem/openinmaps(launchoptions:completionhandler:).md)
  Opens the Maps app and displays the map item.
- [func openInMaps(launchOptions: [String : Any]?, from: UIScene?, completionHandler: ((Bool) -> Void)?)](mkmapitem/openinmaps(launchoptions:from:completionhandler:).md)
  Opens the Maps app from a particular scene using the specified options.
### Serializing a map item
- [let MKMapItemTypeIdentifier: String](mkmapitemtypeidentifier.md)
  A constant that indicates the type of a serialized map item.
### Opening items at launch time
- [Launch options dictionary keys](launch-options-dictionary-keys.md)
  Launch options to specify when opening map items in the Maps app.
- [Directions mode values](directions-mode-values.md)
  Strings that represent the possible values of the launch options direction mode key.
### Initializers
- [init?(coder: NSCoder)](mkmapitem/init(coder:).md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSItemProviderReading](../Foundation/NSItemProviderReading.md)
- [NSItemProviderWriting](../Foundation/NSItemProviderWriting.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)

## See Also

- [Enabling Maps capability in Xcode](enabling-maps-capability-in-xcode.md)
  Configure your routing app to support providing directions.
- [Identifying unique locations with Place IDs](identifying-unique-locations-with-place-ids.md)
  Obtain information about a point of interest that persists over its lifetime.
- [class MKMapView](mkmapview.md)
  An embeddable map interface, similar to the one that the Maps app provides.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkmapitem)*