# getSceneWithCompletionHandler(_:)

**Framework**: MapKit  
**Kind**: method

Requests a LookAround scene and calls the specified completion handler.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
var scene: MKLookAroundScene? { get async throws }
```

#### Discussion

> **Note**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can access it as an asynchronous property that has the following declaration: ```swift
var scene: MKLookAroundScene? { get async throws }
``` For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

 You can call this method from synchronous code using a completion handler, as shown on this page, or you can access it as an asynchronous property that has the following declaration:

```swift
var scene: MKLookAroundScene? { get async throws }
```

For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

## Parameters

- `completionHandler`: A completion handler the framework calls when the scene request completes to indicate the success or failure of the request.

## See Also

- [func cancel()](mklookaroundscenerequest/cancel.md)
  Cancels the pending scene request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mklookaroundscenerequest/getscenewithcompletionhandler(_:))*