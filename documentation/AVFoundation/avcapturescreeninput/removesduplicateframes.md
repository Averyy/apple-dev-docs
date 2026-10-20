# removesDuplicateFrames

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

A Boolean value that specifies whether the capture input skips duplicate frames.

**Availability**:
- macOS 10.8+ - Deprecated in 10.10

> **Deprecated**: The capture system ignores this property in macOS 10.10 and later: the capture input never removes duplicate frames. You can re-create this functionality by using [`AVCaptureVideoDataOutput`](../avcapturevideodataoutput.md) and comparing successive frames.

## Declaration

```swift
var removesDuplicateFrames: Bool { get set }
```

```objc
@property (nonatomic) BOOL removesDuplicateFrames;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturescreeninput/removesduplicateframes)*