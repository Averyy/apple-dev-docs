# setAccessoryButtonEventsEnabled(_:channelUUID:completionHandler:)

**Framework**: Push to Talk  
**Kind**: method  
**Role**: Instance Method

Maps supported accessory button events to actions that begin and end transmission.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+

## Declaration

```swift
func setAccessoryButtonEventsEnabled(_ enabled: Bool, channelUUID: UUID, completionHandler: (@Sendable ((any Error)?) -> Void)? = nil)
```

```swift
func setAccessoryButtonEventsEnabled(_ enabled: Bool, channelUUID: UUID) async throws
```

```objc
- (void) setAccessoryButtonEventsEnabled:(BOOL) enabled forChannelUUID:(NSUUID *) channelUUID completionHandler:(void (^)(NSError *)) completionHandler;
```

#### Discussion

> ❗ **Important**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration:
>
> ```swift
> func setAccessoryButtonEventsEnabled(_ enabled: Bool, channelUUID: UUID) async throws
> ```
>
> For information about concurrency and asynchronous code in Swift, see [Calling Objective-C APIs Asynchronously](../../Swift/calling-objective-c-apis-asynchronously.md).

## Parameters

- `enabled`: A flag that accessory button events map to begin and end transmission actions. If your app doesn’t map these button events to transmission actions, you can disable them by setting the value to [`false`](../../Swift/false.md).
- `channelUUID`: The unique channel identifier of the active participant.
- `completionHandler`: An error that indicates the reason why the system couldn’t set the supported accessory button events.

## See Also

### Starting and stopping transmission
- [func requestBeginTransmitting(channelUUID: UUID)](./requestbegintransmitting%28channeluuid%29.md)
  Begins an audio transmission with the channel identifer you specify.
- [func stopTransmitting(channelUUID: UUID)](./stoptransmitting%28channeluuid%29.md)
  Stops an audio transmission with the channel identifer you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pushtotalk/ptchannelmanager/setaccessorybuttoneventsenabled(_:channeluuid:completionhandler:))*