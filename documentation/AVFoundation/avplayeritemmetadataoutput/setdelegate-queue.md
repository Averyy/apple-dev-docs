# setDelegate(_:queue:)

**Framework**: AVFoundation  
**Kind**: method

Sets the delegate and a dispatch queue on which the delegate is called.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
func setDelegate(_ delegate: (any AVPlayerItemMetadataOutputPushDelegate)?, queue delegateQueue: dispatch_queue_t?)
```

#### Discussion

You specify the metadata delegate, and a dispatch queue on which it will be called, to be notified as new metadata is encountered in the source media.

> ❗ **Important**:  The values set for the `delegate` and `delegateQueue` arguments can be `nil` , but passing `nil` for one requires you to do the same for the other. Passing a `nil` value for only one argument results in an exception being raised at runtime.

 The values set for the `delegate` and `delegateQueue` arguments can be `nil` , but passing `nil` for one requires you to do the same for the other. Passing a `nil` value for only one argument results in an exception being raised at runtime.

## Parameters

- `delegate`: An object conforming to   protocol.
- `delegateQueue`: A dispatch queue on which all delegate methods will be called.

## See Also

- [var advanceIntervalForDelegateInvocation: TimeInterval](avplayeritemmetadataoutput/advanceintervalfordelegateinvocation.md)
  The time interval, in seconds, the player item metadata output object messages its delegate earlier than normal.
- [var delegate: (any AVPlayerItemMetadataOutputPushDelegate)?](avplayeritemmetadataoutput/delegate.md)
  The delegate object.
- [protocol AVPlayerItemMetadataOutputPushDelegate](avplayeritemmetadataoutputpushdelegate.md)
  Methods you can implement to provide additional metadata.
- [var delegateQueue: dispatch_queue_t?](avplayeritemmetadataoutput/delegatequeue.md)
  The dispatch queue on which messages are sent to the delegate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayeritemmetadataoutput/setdelegate(_:queue:))*