# setColorAttachmentMap(_:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Sets the mapping from logical shader color output to physical render pass color attachments.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
func setColorAttachmentMap(_ mapping: MTLLogicalToPhysicalColorAttachmentMap?)
```

#### Discussion

Use this method to define how the physical color attachments you specify via [`colorAttachments`](mtl4renderpassdescriptor/colorattachments.md) map to the logical color output the fragment shader writes to.

To use this feature, make sure to set [`supportColorAttachmentMapping`](mtl4renderpassdescriptor/supportcolorattachmentmapping.md) to [`true`](https://developer.apple.com/documentation/Swift/true).

## Parameters

- `mapping`: Mapping from logical shader outputs to physical outputs.

## See Also

- [func setBlendColor(red: Float, green: Float, blue: Float, alpha: Float)](mtl4rendercommandencoder/setblendcolor(red:green:blue:alpha:).md)
  Configures each pixel component value, including alpha, for the render pipeline’s constant blend color.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4rendercommandencoder/setcolorattachmentmap(_:))*