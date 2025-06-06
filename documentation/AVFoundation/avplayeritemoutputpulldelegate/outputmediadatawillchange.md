# outputMediaDataWillChange(_:)

**Framework**: AVFoundation  
**Kind**: method

Tells the delegate that new samples are about to arrive.

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
optional func outputMediaDataWillChange(_ sender: AVPlayerItemOutput)
```

#### Discussion

You can use this method to prepare for any new sample data. This method is called at some point after a call to your video output object’s `requestNotificationOfMediaDataChangeWithAdvanceInterval:` method.

## Parameters

- `sender`: The output object that sent the message.

## See Also

- [func outputSequenceWasFlushed(AVPlayerItemOutput)](avplayeritemoutputpulldelegate/outputsequencewasflushed(_:).md)
  Tells the delegate that a new sample sequence is commencing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayeritemoutputpulldelegate/outputmediadatawillchange(_:))*