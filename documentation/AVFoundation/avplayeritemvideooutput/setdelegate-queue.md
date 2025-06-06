# setDelegate(_:queue:)

**Framework**: AVFoundation  
**Kind**: method

Sets the delegate and dispatch queue for the receiver.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func setDelegate(_ delegate: (any AVPlayerItemOutputPullDelegate)?, queue delegateQueue: dispatch_queue_t?)
```

## Parameters

- `delegate`: The delegate object for the receiver. You may specify   for this parameter.
- `delegateQueue`: The dispatch queue on which to call delegate methods. If you specify   for this parameter, the video output object calls the delegate on the dispatch queue for your app’s main thread.

## See Also

- [var delegate: (any AVPlayerItemOutputPullDelegate)?](avplayeritemvideooutput/delegate.md)
  The delegate for the video output object.
- [protocol AVPlayerItemOutputPullDelegate](avplayeritemoutputpulldelegate.md)
  Methods you can implement to respond to pixel buffer changes.
- [var delegateQueue: dispatch_queue_t?](avplayeritemvideooutput/delegatequeue.md)
  The dispatch queue on which to call delegate methods.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayeritemvideooutput/setdelegate(_:queue:))*