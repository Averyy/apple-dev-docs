# setStencilReferenceValue(_:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Configures this encoder with a reference value for stencil testing.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
func setStencilReferenceValue(_ referenceValue: UInt32)
```

#### Discussion

The render pipeline applies this reference value to both front-facing and back-facing primitives.

## Parameters

- `referenceValue`: A stencil test comparison value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4rendercommandencoder/setstencilreferencevalue(_:))*