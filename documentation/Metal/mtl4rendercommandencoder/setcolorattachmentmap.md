# setColorAttachmentMap(_:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Sets the mapping from logical shader color output to physical render pass color attachments.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
func setColorAttachmentMap(_ mapping: MTLLogicalToPhysicalColorAttachmentMap)
```

#### Discussion

Use this method to define how the physical color attachments you specify via [`colorAttachments`](mtl4renderpassdescriptor/colorattachments.md) map to the logical color output the fragment shader writes to.

To use this feature, make sure to set [`supportColorAttachmentMapping`](mtl4renderpassdescriptor/supportcolorattachmentmapping.md) to [`true`](https://developer.apple.com/documentation/swift/true).

## Parameters

- `mapping`: Mapping from logical shader outputs to physical outputs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4rendercommandencoder/setcolorattachmentmap(_:))*