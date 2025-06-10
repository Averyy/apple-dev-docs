# setChannelDescriptor(_:channelUUID:completionHandler:)

**Framework**: Push to Talk  
**Kind**: method

Sets the channel description.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+

## Declaration

```swift
func setChannelDescriptor(_ channelDescriptor: PTChannelDescriptor, channelUUID: UUID) async throws
```

## Mentions

- [Creating a Push to Talk app](creating-a-push-to-talk-app.md)

#### Discussion

> ❗ **Important**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration: ```swift
func setChannelDescriptor(_ channelDescriptor: PTChannelDescriptor, channelUUID: UUID) async throws
``` For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

## Parameters

- `channelDescriptor`: The channel description.
- `channelUUID`: The channel identifier.
- `completionHandler`: The completion handler.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pushtotalk/ptchannelmanager/setchanneldescriptor(_:channeluuid:completionhandler:))*