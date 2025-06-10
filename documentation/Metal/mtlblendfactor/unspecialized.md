# MTLBlendFactor.unspecialized

**Framework**: Metal  
**Kind**: case

Defers assigning the blend factor.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
case unspecialized
```

#### Discussion

Until you specialize this value in the pipeline state, it:

- behaves as `MTLBlendFactorOne` for `sourceRGBBlendFactor` and `sourceAlphaBlendFactor`
- behaves as `MTLBlendFactorZero` for `destinationRGBBlendFactor` and `destinationAlphaBlendFactor`


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlblendfactor/unspecialized)*