# AVPlayerItemOutputPullDelegate

**Framework**: AVFoundation  
**Kind**: protocol

Methods you can implement to respond to pixel buffer changes.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
protocol AVPlayerItemOutputPullDelegate : NSObjectProtocol, Sendable
```

#### Overview

The methods in this protocol are called by [`AVPlayerItemVideoOutput`](avplayeritemvideooutput.md) objects.

## Topics

### Responding to Pixel Buffer Changes
- [func outputMediaDataWillChange(AVPlayerItemOutput)](avplayeritemoutputpulldelegate/outputmediadatawillchange(_:).md)
  Tells the delegate that new samples are about to arrive.
- [func outputSequenceWasFlushed(AVPlayerItemOutput)](avplayeritemoutputpulldelegate/outputsequencewasflushed(_:).md)
  Tells the delegate that a new sample sequence is commencing.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [func setDelegate((any AVPlayerItemOutputPullDelegate)?, queue: dispatch_queue_t?)](avplayeritemvideooutput/setdelegate(_:queue:).md)
  Sets the delegate and dispatch queue for the receiver.
- [var delegate: (any AVPlayerItemOutputPullDelegate)?](avplayeritemvideooutput/delegate.md)
  The delegate for the video output object.
- [var delegateQueue: dispatch_queue_t?](avplayeritemvideooutput/delegatequeue.md)
  The dispatch queue on which to call delegate methods.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayeritemoutputpulldelegate)*