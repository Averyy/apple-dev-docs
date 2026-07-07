# setOffset(_:)

**Framework**: RealityKit  
**Kind**: method

Updates the byte offset of this slice.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
mutating func setOffset(_ offset: Int) throws(LowLevelRenderContextError)
```

#### Discussion

Throws [`LowLevelRenderContextError`](lowlevelrendercontexterror.md) if the new offset falls outside the buffer’s allocated capacity.

> **Note**: [`LowLevelRenderContextError`](lowlevelrendercontexterror.md) if the new offset falls outside the buffer’s allocated capacity.

## Parameters

- `offset`: The new byte offset into `buffer` at which this slice begins.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelbufferslice/setoffset(_:))*