# CVPixelBufferAttachmentKeyDefinitions

**Framework**: Core Video  
**Kind**: enum

A namespace for pixel buffer attachment keys.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
enum CVPixelBufferAttachmentKeyDefinitions
```

## Topics

### Type Properties
- [static let proResRawMetadata: CVAttachmentCompositeKeyDefinition<CVPixelBufferAttachmentKeyDefinitions.ShouldPropagate, CVProResRawMetadata>](cvpixelbufferattachmentkeydefinitions/proresrawmetadata.md)
  ProRes RAW image metadata used for raw conversion.
- [static let senselArrayPattern: CVAttachmentKeyDefinition<CVPixelBufferAttachmentKeyDefinitions.ShouldNotPropagate, CVSenselArrayPattern>](cvpixelbufferattachmentkeydefinitions/senselarraypattern.md)
  Bayer pattern indicating sensel arrangement.

## Relationships

### Conforms To
- [CVAttachmentKeyDefinitions](cvattachmentkeydefinitions.md)
- [CVImageBufferAttachmentKeyDefinitions](cvimagebufferattachmentkeydefinitions.md)

## See Also

- [protocol CVPixelBufferRepresentable](cvpixelbufferrepresentable.md)
  CVPixelBufferRepresentable protocol is a sealed protocol intended to be implemented by the types in CoreVideo framework. This protocol facilitates Swift types that wrap a value of CVPixelBuffer type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvpixelbufferattachmentkeydefinitions)*