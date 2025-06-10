# setStencilReferenceValue(front:back:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Configures the encoder with different stencil test reference values for front-facing and back-facing primitives.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
func setStencilReferenceValue(front frontReferenceValue: UInt32, back backReferenceValue: UInt32)
```

#### Discussion

The render pipeline applies `frontReferenceValue` to front-facing primitives and `backReferenceValue` to back-facing primitives.

## Parameters

- `frontReferenceValue`: A stencil test comparison value the render pipeline applies   to front-facing primitives.
- `backReferenceValue`: A stencil test comparison value the render pipeline applies   to back-facing primitives.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4rendercommandencoder/setstencilreferencevalue(front:back:))*