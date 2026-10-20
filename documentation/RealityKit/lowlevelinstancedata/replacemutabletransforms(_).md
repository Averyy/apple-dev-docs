# replaceMutableTransforms(_:)

**Framework**: RealityKit  
**Kind**: method

Replaces the per instance transform data synchronously on the CPU.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
final func replaceMutableTransforms(_ callback: (UnsafeMutableBufferPointer<float4x4>) -> Void)
```

#### Discussion

The transform buffer’s contents are unspecified, and it is the caller’s responsibility to populate the buffer with valid data. The transform buffer provided is only valid for the lifetime of the callback.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelinstancedata/replacemutabletransforms(_:))*