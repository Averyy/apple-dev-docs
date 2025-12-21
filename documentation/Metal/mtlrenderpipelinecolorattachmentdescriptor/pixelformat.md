# pixelFormat

**Framework**: Metal  
**Kind**: property

The pixel format of the color attachment’s texture.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
var pixelFormat: MTLPixelFormat { get set }
```

## Mentions

- [Using the Metal 4 compilation API](using-the-metal-4-compilation-api.md)

#### Discussion

The pixel format of the rendering pipeline state needs to be set to match the pixel format of the texture used by the selected color attachment; otherwise, an error occurs.

## See Also

- [Metal Shading Language Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Metal/Reference/MetalShadingLanguageGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40014364)
- [Metal Programming Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Miscellaneous/Conceptual/MetalProgrammingGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40014221)
- [var writeMask: MTLColorWriteMask](mtlrenderpipelinecolorattachmentdescriptor/writemask.md)
  A bitmask that restricts which color channels are written into the texture.
- [struct MTLColorWriteMask](mtlcolorwritemask.md)
  Values used to specify a mask to permit or restrict writing to color channels of a color value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrenderpipelinecolorattachmentdescriptor/pixelformat)*