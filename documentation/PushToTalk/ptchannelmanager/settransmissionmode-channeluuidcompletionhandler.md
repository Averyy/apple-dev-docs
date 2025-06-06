# setTransmissionMode(_:channelUUID:completionHandler:)

**Framework**: Push to Talk  
**Kind**: method

Sets the audio transmission mode for the channel you specify.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+

## Declaration

```swift
func setTransmissionMode(_ transmissionMode: PTTransmissionMode, channelUUID: UUID) async throws
```

#### Discussion

> ❗ **Important**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration: ```swift
func setTransmissionMode(_ transmissionMode: PTTransmissionMode, channelUUID: UUID) async throws
``` For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

 You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration:

```swift
func setTransmissionMode(_ transmissionMode: PTTransmissionMode, channelUUID: UUID) async throws
```

For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

By default, a channel’s transmission mode is [`PTTransmissionMode.halfDuplex`](pttransmissionmode/halfduplex.md) — indicating that only one participant can send or receive audio at a time. Use [`PTTransmissionMode.fullDuplex`](pttransmissionmode/fullduplex.md) to allow a person to transmit and receive audio simultaneously.

Set the transmission mode to [`PTTransmissionMode.listenOnly`](pttransmissionmode/listenonly.md) to prevent a participant from transmitting any audio.

## Parameters

- `transmissionMode`: The transmission mode.
- `channelUUID`: The channel identifier the participant becomes active in.
- `completionHandler`: The completion handler that contains an optional error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pushtotalk/ptchannelmanager/settransmissionmode(_:channeluuid:completionhandler:))*