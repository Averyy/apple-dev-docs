# getMapItem(completionHandler:)

**Framework**: MapKit  
**Kind**: method

Requests a map item and calls the provided completion handler.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 1.0+

## Declaration

```swift
var mapItem: MKMapItem { get async throws }
```

#### Discussion

> **Note**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can access it as an asynchronous property that has the following declaration: ```swift
var mapItem: MKMapItem { get async throws }
``` For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

 You can call this method from synchronous code using a completion handler, as shown on this page, or you can access it as an asynchronous property that has the following declaration:

```swift
var mapItem: MKMapItem { get async throws }
```

For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

## Parameters

- `completionHandler`: A completion handler the framework calls to indicate the success or failure of the map item request.

## See Also

- [func cancel()](mkmapitemrequest/cancel.md)
  Cancels an in-progress map item request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkmapitemrequest/getmapitem(completionhandler:))*