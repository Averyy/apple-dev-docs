# setFrontFacing(_:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Configures the vertex winding order that determines which face of a geometric primitive is the front one.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
func setFrontFacing(_ frontFacingWinding: MTLWinding)
```

## Parameters

- `frontFacingWinding`: A   value that determines which side of a primitive the render pipeline   interprets as front facing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4rendercommandencoder/setfrontfacing(_:))*