# setBlendColor(red:green:blue:alpha:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Configures each pixel component value, including alpha, for the render pipeline’s constant blend color.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
func setBlendColor(red: Float, green: Float, blue: Float, alpha: Float)
```

## Parameters

- `red`: A value for the red component for the blend color constant.
- `green`: A value for the green component for the blend color constant.
- `blue`: A value for the blue component for the blend color constant.
- `alpha`: A value for the alpha component for the blend color constant.

## See Also

- [func setColorAttachmentMap(MTLLogicalToPhysicalColorAttachmentMap?)](mtl4rendercommandencoder/setcolorattachmentmap(_:).md)
  Sets the mapping from logical shader color output to physical render pass color attachments.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4rendercommandencoder/setblendcolor(red:green:blue:alpha:))*