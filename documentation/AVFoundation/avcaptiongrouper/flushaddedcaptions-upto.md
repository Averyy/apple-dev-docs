# flushAddedCaptions(upTo:)

**Framework**: AVFoundation  
**Kind**: method

Creates caption groups for the captions you enqueue up to the time.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 15.0+
- macOS 12.0+

## Declaration

```swift
func flushAddedCaptions(upTo upToTime: CMTime) -> [AVCaptionGroup]
```

#### Return Value

An array of zero or more caption groups.

## Parameters

- `upToTime`: The time up to which the system flushes the queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcaptiongrouper/flushaddedcaptions(upto:))*