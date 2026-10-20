# stopRequestingMediaData()

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Cancels any current requestMediaDataWhenReadyOnQueue:usingBlock: call.

**Availability**:
- iOS 11.0+ - Deprecated in 27.0
- iPadOS 11.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- macOS 10.13+ - Deprecated in 27.0
- tvOS 11.0+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0

> **Deprecated**: Cancel the receiver's Task instead

## Declaration

```swift
func stopRequestingMediaData()
```

```objc
- (void) stopRequestingMediaData;
```

#### Discussion

This method may be called from outside the block or from within the block.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avsamplebuffervideorenderer/stoprequestingmediadata())*