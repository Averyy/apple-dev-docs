# AVPlayerItemOutputPullDelegate

**Framework**: AVFoundation  
**Kind**: protocol  
**Role**: Protocol

Methods you can implement to respond to pixel buffer changes.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
protocol AVPlayerItemOutputPullDelegate : NSObjectProtocol, Sendable
```

```objc
@protocol AVPlayerItemOutputPullDelegate <NSObject>
```

## Overview

The methods in this protocol are called by [`AVPlayerItemVideoOutput`](./avplayeritemvideooutput.md) objects.

## Topics

### Responding to pixel buffer changes
- [func outputMediaDataWillChange(AVPlayerItemOutput)](./avplayeritemoutputpulldelegate/outputmediadatawillchange%28_%29.md)
  Tells the delegate that new samples are about to arrive.
- [func outputSequenceWasFlushed(AVPlayerItemOutput)](./avplayeritemoutputpulldelegate/outputsequencewasflushed%28_%29.md)
  Tells the delegate that a new sample sequence is commencing.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Configuring the delegate
- [func setDelegate((any AVPlayerItemOutputPullDelegate)?, queue: dispatch_queue_t?)](./avplayeritemvideooutput/setdelegate%28_,queue%29.md)
  Sets the delegate and dispatch queue for the receiver.
- [var delegate: (any AVPlayerItemOutputPullDelegate)?](./avplayeritemvideooutput/delegate.md)
  The delegate for the video output object.
- [var delegateQueue: dispatch_queue_t?](./avplayeritemvideooutput/delegatequeue.md)
  The dispatch queue on which to call delegate methods.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayeritemoutputpulldelegate)*