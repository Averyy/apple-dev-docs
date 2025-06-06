# outputSequenceWasFlushed(_:)

**Framework**: AVFoundation  
**Kind**: method

Tells the delegate that the output is starting a new sequence of media data.

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

This method is invoked after any seeking and change in playback direction. If you are maintaining any queued future media data, you may want to discard those objects after receiving this message.

## Parameters

- `output`: The   object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayeritemoutputpushdelegate/outputsequencewasflushed(_:))*