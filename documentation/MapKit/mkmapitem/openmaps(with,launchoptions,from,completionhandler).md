# openMaps(with:launchOptions:from:completionHandler:)

**Framework**: MapKit  
**Kind**: method  
**Role**: Type Method

Opens the Maps app from a particular scene using the specified map items and options.

**Availability**:
- iOS 13.2+
- iPadOS 13.2+
- Mac Catalyst 13.2+
- visionOS 1.0+

## Declaration

```swift
class func openMaps(with mapItems: [MKMapItem], launchOptions: [String : Any]? = nil, from scene: UIScene?, completionHandler completion: (@Sendable (Bool) -> Void)? = nil)
```

```swift
class func openMaps(with mapItems: [MKMapItem], launchOptions: [String : Any]? = nil, from scene: UIScene?) async -> Bool
```

```objc
+ (void) openMapsWithItems:(NSArray<MKMapItem *> *) mapItems launchOptions:(NSDictionary<NSString *,id> *) launchOptions fromScene:(UIScene *) scene completionHandler:(void (^)(BOOL success)) completion;
```

## Parameters

- `mapItems`: An array of map items to open in the Maps app.
- `launchOptions`: A dictionary of launch options to pass to the Maps app.
- `scene`: The scene where the user interaction takes place.
- `completion`: A completion block the system calls that indicates whether the request was successful.

## See Also

### Launching the Maps app
- [class func openMaps(with: [MKMapItem], launchOptions: [String : Any]?) -> Bool](./openmaps%28with,launchoptions%29.md)
  Opens the Maps app and displays the specified map items.
- [class func openMaps(with: [MKMapItem], launchOptions: [String : Any]?, completionHandler: ((Bool) -> Void)?)](./openmaps%28with,launchoptions,completionhandler%29.md)
  Opens the Maps app using the specified map items and options.
- [func openInMaps(launchOptions: [String : Any]?) -> Bool](./openinmaps%28launchoptions%29.md)
  Opens the Maps app and displays the map item.
- [func openInMaps(launchOptions: [String : Any]?, completionHandler: ((Bool) -> Void)?)](./openinmaps%28launchoptions,completionhandler%29.md)
  Opens the Maps app and displays the map item.
- [func openInMaps(launchOptions: [String : Any]?, from: UIScene?, completionHandler: ((Bool) -> Void)?)](./openinmaps%28launchoptions,from,completionhandler%29.md)
  Opens the Maps app from a particular scene using the specified options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkmapitem/openmaps(with:launchoptions:from:completionhandler:))*