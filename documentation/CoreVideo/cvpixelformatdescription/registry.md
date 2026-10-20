# CVPixelFormatDescription.Registry

**Framework**: Core Video  
**Kind**: class  
**Role**: Class

Registry of all pixel formats.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
final class Registry
```

## Topics

### Instance Properties
- [var formatDescriptions: [CVPixelFormatDescription]](./registry/formatdescriptions.md)
  Get all registered pixel format descriptions.
### Instance Methods
- [func register(CVPixelFormatDescription)](./registry/register%28_%29.md)
  Register a new pixel format with CoreVideo.
### Subscripts
- [subscript(CVPixelFormatType) -> CVPixelFormatDescription?](./registry/subscript%28_%29.md)
  Get the pixel format description for specified format.
### Type Properties
- [static let shared: CVPixelFormatDescription.Registry](./registry/shared.md)
  Global pixel format registry.

## Relationships

### Conforms To
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvpixelformatdescription/registry)*