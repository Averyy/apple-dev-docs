# setServiceStatus(_:channelUUID:completionHandler:)

**Framework**: Push to Talk  
**Kind**: method

Sets the service connection status.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+

## Declaration

```swift
func setServiceStatus(_ status: PTServiceStatus, channelUUID: UUID) async throws
```

#### Discussion

> ❗ **Important**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration: ```swift
func setServiceStatus(_ status: PTServiceStatus, channelUUID: UUID) async throws
``` For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

 You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration:

```swift
func setServiceStatus(_ status: PTServiceStatus, channelUUID: UUID) async throws
```

For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

The default value for the service status is [`PTServiceStatus.ready`](ptservicestatus/ready.md). Set the appropriate service status if your network connection experiences an issue. The system reflects your service status in the user interface.

## Parameters

- `status`: The service status.
- `channelUUID`: The channel identifier.
- `completionHandler`: The completion handler.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pushtotalk/ptchannelmanager/setservicestatus(_:channeluuid:completionhandler:))*