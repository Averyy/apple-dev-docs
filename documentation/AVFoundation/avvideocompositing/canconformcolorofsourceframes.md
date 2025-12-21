# canConformColorOfSourceFrames

**Framework**: AVFoundation  
**Kind**: property

A Boolean value that indicates whether the compositor conforms the color space of source frames to the composition color space.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
optional var canConformColorOfSourceFrames: Bool { get }
```

#### Discussion

A custom compositor indicates its processing requirements through the [`sourcePixelBufferAttributes`](avvideocompositing/sourcepixelbufferattributes.md) and [`supportsWideColorSourceFrames`](avvideocompositing/supportswidecolorsourceframes.md) properties. By default, the composition engine prepares source frames by converting them to meet the compositor’s configuration.

When this property value is true, the engine doesn’t convert source pixel buffers that meet the compositor’s processing requirements. However, it does convert buffers that don’t meet the processing requirements, which includes the following cases:

- The values of [`supportsWideColorSourceFrames`](avvideocompositing/supportswidecolorsourceframes.md) and [`supportsHDRSourceFrames`](avvideocompositing/supportshdrsourceframes.md) are [`false`](https://developer.apple.com/documentation/Swift/false), but the source buffers contain wide color. In this case, the engine converts the color space of source pixel buffers to BT.709 color space. Note that when [`supportsHDRSourceFrames`](avvideocompositing/supportshdrsourceframes.md) is [`true`](https://developer.apple.com/documentation/Swift/true), the engine also assumes [`supportsWideColorSourceFrames`](avvideocompositing/supportswidecolorsourceframes.md) is [`true`](https://developer.apple.com/documentation/Swift/true).
- The value of [`supportsHDRSourceFrames`](avvideocompositing/supportshdrsourceframes.md) is [`false`](https://developer.apple.com/documentation/Swift/false) and source buffers contain HDR color. In this case, the engine converts the color space of source pixel buffers to the composition color space.
- The pixel format of the source buffers isn’t specified in [`sourcePixelBufferAttributes`](avvideocompositing/sourcepixelbufferattributes.md). In this case, the engine converts the pixel format to a supported format and converts the color space to the composition color space.

## See Also

- [var sourcePixelBufferAttributes: [String : any Sendable]?](avvideocompositing/sourcepixelbufferattributes.md)
  The pixel buffer attributes that the compositor accepts for source frames.
- [var requiredPixelBufferAttributesForRenderContext: [String : any Sendable]](avvideocompositing/requiredpixelbufferattributesforrendercontext.md)
  The pixel buffer attributes that the compositor requires for pixel buffers that it creates.
- [var supportsHDRSourceFrames: Bool](avvideocompositing/supportshdrsourceframes.md)
  A Boolean value that indicates whether the compositor handles source frames that contain high dynamic range (HDR) properties.
- [var supportsWideColorSourceFrames: Bool](avvideocompositing/supportswidecolorsourceframes.md)
  A Boolean value that indicates whether the compositor handles source frames that contains wide color properties.
- [var supportsSourceTaggedBuffers: Bool](avvideocompositing/supportssourcetaggedbuffers.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avvideocompositing/canconformcolorofsourceframes)*