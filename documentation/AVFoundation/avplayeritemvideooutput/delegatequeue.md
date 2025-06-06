# delegateQueue

**Framework**: AVFoundation  
**Kind**: property

The dispatch queue on which to call delegate methods.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var delegateQueue: dispatch_queue_t? { get }
```

## See Also

- [func setDelegate((any AVPlayerItemOutputPullDelegate)?, queue: dispatch_queue_t?)](avplayeritemvideooutput/setdelegate(_:queue:).md)
  Sets the delegate and dispatch queue for the receiver.
- [var delegate: (any AVPlayerItemOutputPullDelegate)?](avplayeritemvideooutput/delegate.md)
  The delegate for the video output object.
- [protocol AVPlayerItemOutputPullDelegate](avplayeritemoutputpulldelegate.md)
  Methods you can implement to respond to pixel buffer changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayeritemvideooutput/delegatequeue)*