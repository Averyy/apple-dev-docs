# openMaps(with:launchOptions:from:completionHandler:)

**Framework**: MapKit  
**Kind**: method

Opens the Maps app from a particular scene using the specified map items and options.

**Availability**:
- iOS 13.2+
- iPadOS 13.2+
- Mac Catalyst 13.2+
- visionOS 1.0+

## Declaration

```swift
class func openMaps(with mapItems: [MKMapItem], launchOptions: [String : Any]? = nil, from scene: UIScene?) async -> Bool
```

## Parameters

- `mapItems`: An array of map items to open in the Maps app.
- `launchOptions`: A dictionary of launch options to pass to the Maps app.
- `scene`: The scene where the user interaction takes place.
- `completion`: A completion block the system calls that indicates whether the request was successful.

## See Also

- [class func openMaps(with: [MKMapItem], launchOptions: [String : Any]?) -> Bool](mkmapitem/openmaps(with:launchoptions:).md)
  Opens the Maps app and displays the specified map items.
- [class func openMaps(with: [MKMapItem], launchOptions: [String : Any]?, completionHandler: ((Bool) -> Void)?)](mkmapitem/openmaps(with:launchoptions:completionhandler:).md)
  Opens the Maps app using the specified map items and options.
- [func openInMaps(launchOptions: [String : Any]?) -> Bool](mkmapitem/openinmaps(launchoptions:).md)
  Opens the Maps app and displays the map item.
- [func openInMaps(launchOptions: [String : Any]?, completionHandler: ((Bool) -> Void)?)](mkmapitem/openinmaps(launchoptions:completionhandler:).md)
  Opens the Maps app and displays the map item.
- [func openInMaps(launchOptions: [String : Any]?, from: UIScene?, completionHandler: ((Bool) -> Void)?)](mkmapitem/openinmaps(launchoptions:from:completionhandler:).md)
  Opens the Maps app from a particular scene using the specified options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkmapitem/openmaps(with:launchoptions:from:completionhandler:))*