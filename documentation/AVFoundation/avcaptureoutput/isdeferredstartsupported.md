# isDeferredStartSupported

**Framework**: AVFoundation  
**Kind**: property

A `BOOL` value that indicates whether the output supports deferred start.

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

You can only set the [`isDeferredStartEnabled`](avcaptureoutput/isdeferredstartenabled.md) property value to `true` if the output supports deferred start.

## See Also

- [var isDeferredStartEnabled: Bool](avcaptureoutput/isdeferredstartenabled.md)
  A Boolean value that indicates whether to defer starting this capture output.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcaptureoutput/isdeferredstartsupported)*