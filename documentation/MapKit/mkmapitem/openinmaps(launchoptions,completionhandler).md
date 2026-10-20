# openInMaps(launchOptions:completionHandler:)

**Framework**: MapKit  
**Kind**: method  
**Role**: Instance Method

Opens the Maps app and displays the map item.

**Availability**:
- macOS 14.4+

## Declaration

```swift
func openInMaps(launchOptions: [String : Any]? = nil, completionHandler completion: (@Sendable (Bool) -> Void)? = nil)
```

```swift
func openInMaps(launchOptions: [String : Any]? = nil) async -> Bool
```

```objc
- (void) openInMapsWithLaunchOptions:(NSDictionary<NSString *,id> *) launchOptions completionHandler:(void (^)(BOOL success)) completion;
```

## Parameters

- `launchOptions`: A dictionary of launch options to pass to the Maps app.
- `completion`: A completion block the system calls that indicates whether the request was successful.

## See Also

### Launching the Maps app
- [class func openMaps(with: [MKMapItem], launchOptions: [String : Any]?) -> Bool](./openmaps%28with,launchoptions%29.md)
  Opens the Maps app and displays the specified map items.
- [class func openMaps(with: [MKMapItem], launchOptions: [String : Any]?, completionHandler: ((Bool) -> Void)?)](./openmaps%28with,launchoptions,completionhandler%29.md)
  Opens the Maps app using the specified map items and options.
- [class func openMaps(with: [MKMapItem], launchOptions: [String : Any]?, from: UIScene?, completionHandler: ((Bool) -> Void)?)](./openmaps%28with,launchoptions,from,completionhandler%29.md)
  Opens the Maps app from a particular scene using the specified map items and options.
- [func openInMaps(launchOptions: [String : Any]?) -> Bool](./openinmaps%28launchoptions%29.md)
  Opens the Maps app and displays the map item.
- [func openInMaps(launchOptions: [String : Any]?, from: UIScene?, completionHandler: ((Bool) -> Void)?)](./openinmaps%28launchoptions,from,completionhandler%29.md)
  Opens the Maps app from a particular scene using the specified options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkmapitem/openinmaps(launchoptions:completionhandler:))*