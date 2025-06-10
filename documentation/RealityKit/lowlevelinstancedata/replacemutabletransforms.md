# replaceMutableTransforms(_:)

**Framework**: RealityKit  
**Kind**: method

Replace the per instance transform data synchronously on the CPU.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
func replaceMutableTransforms(_ callback: (UnsafeMutableBufferPointer<float4x4>) -> Void)
```

#### Discussion

The transform buffer’s contents are unspecified, and it is the caller’s responsibility to populate the buffer with valid data. The transform buffer provided is only valid for the lifetime of the callback.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelinstancedata/replacemutabletransforms(_:))*