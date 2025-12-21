# isDeferredStartSupported

**Framework**: AVFoundation  
**Kind**: property

A `BOOL` value that indicates whether the preview layer supports deferred start.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+

## Declaration

```swift
var isDeferredStartSupported: Bool { get }
```

#### Discussion

You can only set the [`isDeferredStartEnabled`](avcapturevideopreviewlayer/isdeferredstartenabled.md) property to `true` if the preview layer supports deferred start.

## See Also

- [var isDeferredStartEnabled: Bool](avcapturevideopreviewlayer/isdeferredstartenabled.md)
  A `BOOL` value that indicates whether to defer starting this preview layer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturevideopreviewlayer/isdeferredstartsupported)*