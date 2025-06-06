# Adopting unified Maps URLs

**Framework**: MapKit

Access Maps URLs and options for displaying Maps information across Apple platforms.

#### Overview

In iOS 18.4 and later, macOS 15.4 and later, and watchOS 11.4 and later, the Maps platform provides a new, unified collection of URLs that offers the same functionality on all devices. Use the Maps path components to control aspects of the Maps display, ranging from the presentation of a simple map centered on a location you provide, to finding specific points of interest (POIs) and providing complex multistop driving, walking, or transit directions.

#### Frame the Map Display

Use the `/frame` path component and `query` parameters to control aspects of the map’s framing and representation. This component allows you to set a map’s orientation, style, visible area (the map’s span), and other perspective controls, as described in the table below.

| Parameter | Description |
| --- | --- |
| `center` | Frames the map on a specific center described by comma-separated coordinate pair, such as `40.773957,-73.970974`. |
| `span` | Specifies the size of the area around the center point of the search in degrees of longitude and latitude, for example `0.05,0.05`, which is approximately one km for these examples. For more information on what these distances mean at different latitudes, see [`init(latitudeDelta:longitudeDelta:)`](MKCoordinateSpan/init(latitudeDelta:longitudeDelta:).md). |
| `mode` | Sets the map’s mode to optionally allow location tracking: values can be `follow` or `follow-with-heading`, or `none`. |
| `heading` | Sets the direction toward which the map orients. |
| `pitch` | Sets the the vertical angle the map is oriented to. |
| `distance` | Sets the apparent distance from the viewer to the map surface; this parameter also affects the map’s `span`. |
| `map` | Sets the type of map to display: values can be `explore`, `driving`, `transit`, `satellite`, or `hybrid`. |

The following  `/frame` path component examples demonstrate different kinds of map framing, along with details, where necessary, on how specific parameters affect what the map displays.

- Center the map at specific coordinate — [`https://maps.apple.com/frame?center=40.753035,-73.981846`](https://developer.apple.comhttps://maps.apple.com/frame?center=40.753035,-73.981846).
- Set map mode to transit and center map at specific coordinate — [`https://maps.apple.com/frame?map=transit&center=40.753035,-73.981846`](https://developer.apple.comhttps://maps.apple.com/frame?map=transit&center=40.753035,-73.981846).
- Set the map mode to `explore` and set user tracking to `follow` —  [`https://maps.apple.com/frame?coordinate=40.753035,-73.981846&map=explore&mode=follow&span=0.024461,0.043938`](https://developer.apple.comhttps://maps.apple.com/frame?coordinate=40.753035,-73.981846&map=explore&mode=follow&span=0.024461,0.043938).
- Set map mode to `explore`; this setting cause the map to focus on a specified coordinate, and sets the map camera attributes — [`https://maps.apple.com/frame?map=explore&center=40.753035,-73.981846&heading=180&pitch=15&distance=10000`](https://developer.apple.comhttps://maps.apple.com/frame?map=explore&center=40.753035,-73.981846&heading=180&pitch=15&distance=10000).
- Set the map mode to `explore`, and set location tracking mode to `follow` — [`https://maps.apple.com/frame?map=explore&center=40.753035,-73.981846&heading=18a0&pitch=15&distance=10000&mode=follow`](https://developer.apple.comhttps://maps.apple.com/frame?map=explore&center=40.753035,-73.981846&heading=18a0&pitch=15&distance=10000&mode=follow). If you’re setting tracking mode and camera properties, the tracking mode takes precedence. Setting camera properties requires a center coordinate.
- Center the map at a specific coordinate and frame the map to the specified span —  [`https://maps.apple.com/frame?center=40.753035,-73.981846&span=0.05,0.05`](https://developer.apple.comhttps://maps.apple.com/frame?center=40.753035,-73.981846&span=0.05,0.05). It’s also possible to frame the map using the `distance` parameter, for example, [`https://maps.apple.com/frame?center=40.753035,-73.981846&distance=17825`](https://developer.apple.comhttps://maps.apple.com/frame?center=40.753035,-73.981846&distance=17825).
- Set the map mode to `explore`, which centers the map at a specified coordinate, and sets the map camera elevation, heading, and angle; in this example, facing East (90˚), a distance of 1 km, and a map pitch of 15˚ — [`https://maps.apple.com/frame?map=explore&center=40.753035,-73.981846&heading=90&pitch=15&distance=10000`](https://developer.apple.comhttps://maps.apple.com/frame?map=explore&center=37.316115,-122.050910&heading=90&pitch=15&distance=10000).
- Center the map at a specific coordinate and set the camera `distance` — [`https://maps.apple.com/frame?map=explore&center=40.753035,-73.981846&distance=10000`](https://developer.apple.comhttps://maps.apple.com/frame?map=explore&center=40.753035,-73.981846&distance=10000).
- Center the map at a specific coordinate and set the camera to the specified properties —  [`https://maps.apple.com/frame?center=40.753035,-73.981846&distance=5000&pitch=15&heading=180&span=1.0,1.0`](https://developer.apple.comhttps://maps.apple.com/frame?center=37.797198,-122.407377&distance=5000&pitch=15&heading=180&span=1.0,1.0). If you provide both the `span` and `camera` properties, the `camera` properties take precedence, since they’re more specific than a `span`.

#### Perform General Searches

You can use the `/search` path component to search for specific kinds of locations using several `query` parameters.

| Parameter | Description |
| --- | --- |
| `query` | A search string. This parameter can be a general point of interest (POI) such as `pizza`, or a specific location such as an address string, such as `1000 Fifth Avenue, NY, NY`, or a city name such as `San Francisco`. For a list of POIs, see [`MKPointOfInterestCategory`](MKPointOfInterestCategory.md). |
| `span` | A span that specifies the size of the area around the center point of the search in degrees of longitude and latitude, for example `0.05,0.05` which is approximately 1 km for these examples. For more information on what these distances mean at different latitudes, see [`init(latitudeDelta:longitudeDelta:)`](MKCoordinateSpan/init(latitudeDelta:longitudeDelta:).md). |

The following  `/search`  path component examples demonstrate how to use the `search` path component to find `pizza`, one of Maps’ POI identifiers, using different kinds of location and distance descriptions.

- Show results for `pizza` around a person’s location: [`https://maps.apple.com/search?query=pizza`](https://developer.apple.comhttps://maps.apple.com/search?query=pizza). The default center point is a person’s location.
- Show results for `pizza` centered on Trafalgar Square in London, United Kingdom — [`https://maps.apple.com/search?query=pizza&center=51.507984,-0.128015`](https://developer.apple.comhttps://maps.apple.com/search?query=pizza&center=51.507984,-0.128015).
- Show results for `pizza` within approximately 1 km around Washington Square Park in New York City —  [`https://maps.apple.com/search?query=pizza&center=40.730877,-73.997603&span=0.05,0.05`](https://developer.apple.comhttps://maps.apple.com/search?query=pizza&center=40.730877,-73.997603&span=0.05,0.05).

#### Show the Place Card of a Poi

Using the `/place` path component enables you to specify a place card that shows useful details about points of interest on the map. Use the parameters in the following table to specify a POI and optionally the place card name and map type.

| Parameter | Description |
| --- | --- |
| `coordinate` | The latitude and longitude of the location, as a comma-separated pair of floating point values that represent latitude and longitude. |
| `address` | The address of the location, such as “1000 Fifth Ave, New York, NY”. |
| `place-id` | A Place ID is a unique identifier for a POI, such as `I521E602783BA9605`, The Metropolitan Museum of Art at 1000 Fifth Avenue, New York, NY 10028, United States; for more information on Place IDs, see [`Identifying unique locations with Place IDs`](identifying-unique-locations-with-place-ids.md). |
| `map` | The type of map to display. Maps supports `explore`, `driving`, `transit`, `satellite`, or `hybrid` as the map type. |

The following examples demonstrate different place card details along with details, where necessary, on how specific parameters affect what the maps displays.

- Show the address 1000 Fifth Ave, NY, NY, which is located at the specified coordinate and associated POIs near this address —  [`https://maps.apple.com/place?coordinate=40.779092,-73.962932`](https://developer.apple.comhttps://maps.apple.com/place?coordinate=40.779092,-73.962932).
- Show 1000 Fifth Ave, NY, NY, 10028 using an address string and display associated POIs near this address: [`https://maps.apple.com/place?address=1000%20Fifth%20Ave,%20NY,NY,10028%20United%20States`](https://developer.apple.comhttps://maps.apple.com/place?address=1000%20Fifth%20Ave,%20NY,NY,10028%20United%20States).
- Show the place at PlaceID `IF149E70A3B3C4CB2` — American Museum of Natural History, 200 Central Park W, New York, NY 10024, United States — [`https://maps.apple.com/place?place-id=IF149E70A3B3C4CB2`](https://developer.apple.comhttps://maps.apple.com/place?place-id=IF149E70A3B3C4CB2). To find a specific Place ID, you can use [`MKMapItem`](MKMapItem.md) in AppKit and UIKit, [`Place`](https://developer.apple.com/documentation/MapKitJS/Place) in MapKitJS, or see [`Place ID Lookup`](https://developer.apple.comhttps://developer.apple.com/maps/place-id-lookup/).
- Show a place card at the specified coordinate with custom name you provide —  [`https://maps.apple.com/place?coordinate=40.864791,-73.931723&name=My%20Favorite%20Place`](https://developer.apple.comhttps://maps.apple.com/place?coordinate=40.864791,-73.931723&name=My%20Favorite%20Place). You can use this parameter when dropping a pin if you need to display a custom name for the place card.
- Show a person’s current location — [`https://maps.apple.com/place?place-id=my-location`](https://developer.apple.comhttps://maps.apple.com/place?place-id=my-location). This parameter requires that a person has given permission for Maps to display their location.
- Show the location of a person’s parked car — [`https://maps.apple.com/place?place-id=parked-car`](https://developer.apple.comhttps://maps.apple.com/place?place-id=parked-car). This parameter requires that a person has given Maps permission to record the place they parked.

#### Explore the Environment Using Look Around

Use the `/look-around` path component and one of the following parameters to specify the initial location to start a session using Look Around.

| Parameter | Description |
| --- | --- |
| `coordinate` | The latitude and longitude of the location as  a comma-separated pair of floating point values that represent latitude and longitude. |
| `address` | The address of the location. This parameter is an address string, such as “1000 Fifth Avenue, New York, NY 10028”. |
| `place-id` | A Place ID, which is a unique identifier for a point of interest, such as `I521E602783BA9605`, The Metropolitan Museum of Art at 1000 Fifth Avenue, New York, NY 10028, United States; for more information on Place IDs, see [`Identifying unique locations with Place IDs`](identifying-unique-locations-with-place-ids.md). |

The following examples demonstrate Look Around experiences in different cities:

- The San Francisco Ferry Building — [`https://maps.apple.com/look-around?place-id=IBE1F65094A7A13B1`](https://developer.apple.comhttps://maps.apple.com/look-around?place-id=IBE1F65094A7A13B1)
- The New York Stock Exchange, New York City, United States —  [`https://maps.apple.com/look-around?coordinate=40.706974,-74.011281`](https://developer.apple.comhttps://maps.apple.com/look-around?coordinate=40.706974,-74.011281)
- The Tower of London, London, United Kingdom — [`https://maps.apple.com/look-around?address=The%20Tower%20of%20London,London,UK`](https://developer.apple.comhttps://maps.apple.com/look-around?address=The%20Tower%20of%20London,London,UK)
- The Eiffel Tower, Paris, France — [`https://maps.apple.com/look-around?address=The%20Eiffel%20Tower,Paris,France`](https://developer.apple.comhttps://maps.apple.com/look-around?address=The%20Eiffel%20Tower,Paris,France)

#### Request Directions

Use the `/directions` path component and following query parameters in several combinations to request directions.

| Parameters | Description | Values | Notes |
| --- | --- | --- | --- |
| `source` | The starting point of the navigation route | Specify an address, coordinate, or a place name |  |
| `source-place-id` | An optional place identifier for the source parameter | A Place ID | Specifying a `source-place-id` also requires the `source` parameter |
| `destination` | The ending destination of the navigation route | Specify an address, coordinate, or a place name |  |
| `destination-place-id` | An optional place identifier for the destination parameter | A Place ID | Specifying a `destination-place-id` also requires the `destination` parameter |
| `waypoint` | This parameter describes destinations in between the `source` and `destination` you can use for multistop routing | Specify an address, coordinate, or a place name | You can specify multiple waypoints by repeating the `waypoint` parameter |
| `waypoint-place-id` | An optional place identifier for the waypoint parameter | A Place ID, which is a unique identifier for a point of interest, such as `I521E602783BA9605`, The Metropolitan Museum of Art at 1000 Fifth Avenue, New York, NY 10028, United States; for more information on Place IDs, see [`Identifying unique locations with Place IDs`](identifying-unique-locations-with-place-ids.md) |  |
| `mode` | The transportation mode | You can specify one of `driving`, `walking`, `transit`, or `cycling` |  |
| `avoid` | The route preferences are specific to the transportation mode | You can specify `tolls`, `highways`, `busy-roads`, or `stairs` | Specify multiple options by using a comma (,) as the delimiter |
| `transit-preferences` | The preferred method of travel for transit | Available modes are `bus`, `subway`, `commuter`, or `ferry` | Specify multiple options by using the comma (,) as the delimiter |
| `start` | Starts navigation after the delay in seconds that you specify | An integer that indicates the number of seconds to delay |  |

You can use the query parameters to the `directions` path in a large number of combinations to control how Maps displays directions. Limitations on the combinators or side effect that they may have are listed in the table above.

- Show driving directions from a person’s current location to San Francisco City Hall: [`https://maps.apple.com/directions?destination=1%Dr.%20Carlton%20B.%20Goodlatte%20Place,%20San%20Francisco,%20CA%20%94102,%20United%20States&mode=driving`](https://developer.apple.comhttps://maps.apple.com/directions?destination=1%Dr.%20Carlton%20B.%20Goodlatte%20Place,%20San%20Francisco,%20CA%20%94102,%20United%20States&mode=driving]).
- Show the step-by-step walking directions from the San Franciso Ferry Building to San Francisco City Hall: [`https://maps.apple.com/directions?source=37.795442,-122.393624&destination=1%Dr.%20Carlton%20B.%20Goodlatte%20Place,%20San%20Francisco,%20CA%20%94102,%20United%20States&mode=walking`](https://developer.apple.comhttps://maps.apple.com/directions?source=37.795442,-122.393624&destination=1%Dr.%20Carlton%20B.%20Goodlatte%20Place,%20San%20Francisco,%20CA%20%94102,%20United%20States&mode=walking).
- Show multistop driving directions to The San Francisco Ferry Building and San Francisco City Hall — [`https://maps.apple.com/directions?destination=1%Dr.%20Carlton%20B.%20Goodlatte%20Place,%20San%20Francisco,%20CA%20%94102,%20United%20States&waypoint=37.795442,-122.393624&mode=driving`](https://developer.apple.comhttps://maps.apple.com/directions?destination=1%Dr.%20Carlton%20B.%20Goodlatte%20Place,%20San%20Francisco,%20CA%20%94102,%20United%20States&waypoint=37.795442,-122.393624&mode=driving). You can specify multiple `waypoint` parameters for different waypoints.
- Show multistop driving directions, in New York City, from Riverside Park to The American Museum of Natural History, The Metropolitan Museum of Art, and The New York Public Library — [`https://maps.apple.com/directions?source=328%10Riverside%20Drive,%20New%20York,NY%2010025&destination=200%20Central%20Park%20W%20New%20York,%20NY%2010024%20United%20States&waypoint=40.779092,-73.962932&waypoint=476%20Fifth%20Ave%20New%20York,%20NY%2010018%20United%20States&mode=driving`](https://developer.apple.comhttps://maps.apple.com/directions?source=328%10Riverside%20Drive,%20New%20York,NY%2010025&destination=200%20Central%20Park%20W%20New%20York,%20NY%2010024%20United%20States&waypoint=40.779092,-73.962932&waypoint=476%20Fifth%20Ave%20New%20York,%20NY%2010018%20United%20States&mode=driving).
- Show transit directions from the New York Public Library to the American Museum of Natural History in New York City —  [`https://maps.apple.com/directions?source=200%20Central%20Park%20W%20New%20York,%20NY%2010024%20United%20States&destination=200%20Central%20Park%20W%20New%20York,%20NY%2010024%20United%20States&mode=transit`](https://developer.apple.comhttps://maps.apple.com/directions?source=476%20Fifth%20Ave%20New%20York,%20NY%2010018%20United%20States&destination=200%20Central%20Park%20W%20New%20York,%20NY%2010024%20United%20States&mode=transit). Leaving off the `source` instructs Maps to display directions using public transit to the specified destination from a person’s current location, which might not be practical depending on a person’s location.
- Show driving directions from The American Museum of Natural History in New York City to Jones Beach State Park on Long Island, New York, avoiding tolls, if possible — [`https://maps.apple.com/directions?source=476%20Fifth%20Ave%20New%20York,%20NY%2010018%20United%20States&destination=40.596896,-73.514907&mode=driving&avoid=tolls`](https://developer.apple.comhttps://maps.apple.com/directions?source=476%20Fifth%20Ave%20New%20York,%20NY%2010018%20United%20States&destination=40.596896,-73.514907&mode=driving&avoid=tolls).
- Show driving directions to 941 Alamo Dr, in San Francisco, CA avoiding tolls and highways, if possible — [`https://maps.apple.com/directions?destination=941%20Alamo%20Dr,%20Vacaville,%20CA%20%2095687,%20United%20States&mode=driving&avoid=tolls,highways`](https://developer.apple.comhttps://maps.apple.com/directions?destination=941%20Alamo%20Dr,%20Vacaville,%20CA%20%2095687,%20United%20States&mode=driving&avoid=tolls,highways). You can use ‘,’ as a separator to specify multiple `avoid` options.
- Show walking directions from, a person’s current location to 1 La Avanzada St, San Francisco, CA avoiding highways, hills, stairs, and busy roads, if possible — [`https://maps.apple.com/directions?destination=1%20La%20Avanzada%20St,%20San%20Francisco,%20CA%20%2094131,%20United%20States&mode=walking&avoid=highways,hills,stairs,busy-roads`](https://developer.apple.comhttps://maps.apple.com/directions?destination=1%20La%20Avanzada%20St,%20San%20Francisco,%20CA%20%2094131,%20United%20States&mode=walking&avoid=highways,hills,stairs,busy-roads). The `avoid` options are only applicable to their respective transportation modes.
- Show transit directions from a person’s current location to Sausalito, preferring bus and ferry —  [`https://maps.apple.com/directions?destination=Sausalito,%20CA,%20United%20States&transit-preferences=bus,ferry&mode=transit`](https://developer.apple.comhttps://maps.apple.com/directions?destination=Sausalito,%20CA,%20United%20States&transit-preferences=bus,ferry&mode=transit). Leaving off the `source` instructs Maps to display directions using public transit to the specified destination from a person’s current location, which might not be practical depending on their location.

#### Find Guides and Curated Places

Using the `/guides` path component, you can ask Maps to provide details about place guides and curated collections using the following URL: [`https://maps.apple.com/guides`](https://developer.apple.comhttps://maps.apple.com/guides).

#### Report a Problem

If you find an issue with Apple Maps, you can report a problem using the `/report-a-problem path` component, followed by any of the following parameters:

| Parameters | Description | Values |
| --- | --- | --- |
| `coordinate` | The latitude and longitude of the location | A comma-separated pair of floating point values that represent latitude and longitude |
| `address` | The address of the location | An address string, such as 1000 Fifth Avenue |
| `place-id` | The unique Place ID for a point of interest; for example, the place ID `I8CAD8EFA77AA3D42` represents Bethesda Terrace in New York City’s Central Park | For more information on Place IDs, see [`Identifying unique locations with Place IDs`](identifying-unique-locations-with-place-ids.md) |

##### Example Problem Reports

You can report a problem using the same kinds of location descriptors the other queries use. The following examples show how to report a problem using a coordinate, an address, or a Place ID.

- Report a problem at the coordinate `40.753035,-73.981846` (The New York Public Library at 42nd St & 5th Ave in New York City) - [`https://maps.apple.com/report-a-problem?coordinate=37.316115,-122.050910`](https://developer.apple.comhttps://maps.apple.com/report-a-problem?coordinate=37.316115,-122.050910)
- Report a problem at the address 1000 Fifth Avenue, New York, NY 10028 United States — [`https://maps.apple.com/report-a-problem?address=1000%20Fifth%20Ave%20New%20York%20NY%2100284%20United%20States`](https://developer.apple.comhttps://maps.apple.com/report-a-problem?address=1000%20Fifth%20Ave%20New%20York%20NY%2100284%20United%20States)
- Report a problem at Place ID `IBE1F65094A7A13B1`, the San Francisco Ferry Building — [`https://maps.apple.com/report-a-problem?place-id=IBE1F65094A7A13B1`](https://developer.apple.comhttps://maps.apple.com/report-a-problem?place-id=IBE1F65094A7A13B1)

When you open the `report-a-problem` URL, Maps opens a problem report sheet to ask a person for more detail on the nature of the problem, which Apple uses to investigate the report.

## See Also

- [MapKit for AppKit and UIKit](mapkit-for-appkit-and-uikit.md)
- [MapKit for SwiftUI](mapkit-for-swiftui.md)
  MapKit for SwiftUI allows you to build map-centric views and apps across Apple platforms. You can design expressive and highly interactive Maps with minimal code by composing views, using ViewBuilders and view modifiers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/unified-map-urls)*