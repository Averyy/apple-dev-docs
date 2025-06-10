# withTransforms(_:)

**Framework**: RealityKit  
**Kind**: method

Read the per instance transform data synchronously on the CPU. The transform buffer provided is only valid for the lifetime of the callback.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
func withTransforms(_ callback: (UnsafeBufferPointer<float4x4>) -> Void)
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelinstancedata/withtransforms(_:))*