# canConformColorOfSourceFrames

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic, readonly) BOOL canConformColorOfSourceFrames;
```

#### Discussion

A custom compositor indicates its processing requirements through the [`sourcePixelBufferAttributes`](./sourcepixelbufferattributes.md) and [`supportsWideColorSourceFrames`](./supportswidecolorsourceframes.md) properties. By default, the composition engine prepares source frames by converting them to meet the compositor’s configuration.

When this property value is true, the engine doesn’t convert source pixel buffers that meet the compositor’s processing requirements. However, it does convert buffers that don’t meet the processing requirements, which includes the following cases:

- The values of [`supportsWideColorSourceFrames`](./supportswidecolorsourceframes.md) and [`supportsHDRSourceFrames`](./supportshdrsourceframes.md) are [`false`](../../Swift/false.md), but the source buffers contain wide color. In this case, the engine converts the color space of source pixel buffers to BT.709 color space. Note that when [`supportsHDRSourceFrames`](./supportshdrsourceframes.md) is [`true`](../../Swift/true.md), the engine also assumes [`supportsWideColorSourceFrames`](./supportswidecolorsourceframes.md) is [`true`](../../Swift/true.md).
- The value of [`supportsHDRSourceFrames`](./supportshdrsourceframes.md) is [`false`](../../Swift/false.md) and source buffers contain HDR color. In this case, the engine converts the color space of source pixel buffers to the composition color space.
- The pixel format of the source buffers isn’t specified in [`sourcePixelBufferAttributes`](./sourcepixelbufferattributes.md). In this case, the engine converts the pixel format to a supported format and converts the color space to the composition color space.

## See Also

### Inspecting processing requirements
- [var sourcePixelBufferAttributes: [String : any Sendable]?](./sourcepixelbufferattributes.md)
  The pixel buffer attributes that the compositor accepts for source frames.
- [var requiredPixelBufferAttributesForRenderContext: [String : any Sendable]](./requiredpixelbufferattributesforrendercontext.md)
  The pixel buffer attributes that the compositor requires for pixel buffers that it creates.
- [var supportsHDRSourceFrames: Bool](./supportshdrsourceframes.md)
  A Boolean value that indicates whether the compositor handles source frames that contain high dynamic range (HDR) properties.
- [var supportsWideColorSourceFrames: Bool](./supportswidecolorsourceframes.md)
  A Boolean value that indicates whether the compositor handles source frames that contains wide color properties.
- [var supportsSourceTaggedBuffers: Bool](./supportssourcetaggedbuffers.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avvideocompositing/canconformcolorofsourceframes)*