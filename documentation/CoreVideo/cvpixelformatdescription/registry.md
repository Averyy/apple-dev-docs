# CVPixelFormatDescription.Registry

**Framework**: Core Video  
**Kind**: class

Registry of all pixel formats.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
final class Registry
```

## Topics

### Instance Properties
- [var formatDescriptions: [CVPixelFormatDescription]](cvpixelformatdescription/registry/formatdescriptions.md)
  Get all registered pixel format descriptions.
### Instance Methods
- [func register(CVPixelFormatDescription)](cvpixelformatdescription/registry/register(_:).md)
  Register a new pixel format with CoreVideo.
### Subscripts
- [subscript(CVPixelFormatType) -> CVPixelFormatDescription?](cvpixelformatdescription/registry/subscript(_:).md)
  Get the pixel format description for specified format.
### Type Properties
- [static let shared: CVPixelFormatDescription.Registry](cvpixelformatdescription/registry/shared.md)
  Global pixel format registry.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvpixelformatdescription/registry)*