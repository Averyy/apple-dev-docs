# channelManager(delegate:restorationDelegate:completionHandler:)

**Framework**: Push to Talk  
**Kind**: method

Creates a channel manager with the configuration you specify.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+

## Declaration

```swift
class func channelManager(delegate: any PTChannelManagerDelegate, restorationDelegate: any PTChannelRestorationDelegate) async throws -> PTChannelManager
```

## Mentions

- [Creating a Push to Talk app](creating-a-push-to-talk-app.md)

#### Discussion

> ❗ **Important**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration: ```swift
class func channelManager(delegate: PTChannelManagerDelegate, restorationDelegate: PTChannelRestorationDelegate) async throws -> PTChannelManager
``` For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

You must create a channel manager as soon as possible when launching your app so the system is able to restore existing challenge and deliver push notifications to your [`PTChannelManagerDelegate`](ptchannelmanagerdelegate.md). By providing the restoration delegate, you decide whether to rejoin or leave any previously active channel the system knows about.

## Parameters

- `delegate`: An object that conforms to the channel manager protocol.
- `restorationDelegate`: An object that conforms to the channel resoration protocol.
- `completionHandler`: The completion callback handler.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pushtotalk/ptchannelmanager/channelmanager(delegate:restorationdelegate:completionhandler:))*