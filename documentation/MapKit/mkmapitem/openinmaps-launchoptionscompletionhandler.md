# openInMaps(launchOptions:completionHandler:)

**Framework**: MapKit  
**Kind**: method

Opens the Maps app and displays the map item.

**Availability**:
- macOS 14.4+

## Declaration

```swift
func openInMaps(launchOptions: [String : Any]? = nil) async -> Bool
```

#### Discussion

> **Note**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration: ```swift
func openInMaps(launchOptions: [String : Any]? = nil) async -> Bool
``` For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

 You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration:

```swift
func openInMaps(launchOptions: [String : Any]? = nil) async -> Bool
```

For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

## Parameters

- `launchOptions`: A dictionary of launch options to pass to the Maps app.
- `completion`: A completion block the system calls that indicates whether the request was successful.

## See Also

- [class func openMaps(with: [MKMapItem], launchOptions: [String : Any]?) -> Bool](mkmapitem/openmaps(with:launchoptions:).md)
  Opens the Maps app and displays the specified map items.
- [class func openMaps(with: [MKMapItem], launchOptions: [String : Any]?, completionHandler: ((Bool) -> Void)?)](mkmapitem/openmaps(with:launchoptions:completionhandler:).md)
  Opens the Maps app using the specified map items and options.
- [class func openMaps(with: [MKMapItem], launchOptions: [String : Any]?, from: UIScene?, completionHandler: ((Bool) -> Void)?)](mkmapitem/openmaps(with:launchoptions:from:completionhandler:).md)
  Opens the Maps app from a particular scene using the specified map items and options.
- [func openInMaps(launchOptions: [String : Any]?) -> Bool](mkmapitem/openinmaps(launchoptions:).md)
  Opens the Maps app and displays the map item.
- [func openInMaps(launchOptions: [String : Any]?, from: UIScene?, completionHandler: ((Bool) -> Void)?)](mkmapitem/openinmaps(launchoptions:from:completionhandler:).md)
  Opens the Maps app from a particular scene using the specified options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkmapitem/openinmaps(launchoptions:completionhandler:))*