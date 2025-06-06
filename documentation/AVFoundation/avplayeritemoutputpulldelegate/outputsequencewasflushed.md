# outputSequenceWasFlushed(_:)

**Framework**: AVFoundation  
**Kind**: method

Tells the delegate that a new sample sequence is commencing.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
optional func outputSequenceWasFlushed(_ output: AVPlayerItemOutput)
```

#### Discussion

This method is called after any attempt to seek or change the playback direction of the item’s content. If you are maintaining any queued future samples, you can use your implementation of this method to discard those samples.

## Parameters

- `output`: The output object that sent the message.

## See Also

- [func outputMediaDataWillChange(AVPlayerItemOutput)](avplayeritemoutputpulldelegate/outputmediadatawillchange(_:).md)
  Tells the delegate that new samples are about to arrive.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayeritemoutputpulldelegate/outputsequencewasflushed(_:))*