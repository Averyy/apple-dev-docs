# MTLBlendFactor.unspecialized

**Framework**: Metal  
**Kind**: case

Defers assigning the blend factor.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

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