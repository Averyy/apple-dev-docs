# CVPixelBufferAttributes

**Framework**: Core Video  
**Kind**: struct

A partial set of pixel buffer creation attributes. This struct is useful for conveying partial requirements for pixel buffers to clients. This struct makes all properties of `CVPixelBuffer/CreationAttributes` optional.

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
@dynamicMemberLookup
struct CVPixelBufferAttributes
```

## Topics

### Initializers
- [init(CVPixelBufferCreationAttributes)](cvpixelbufferattributes/init(_:).md)
  Convert CreationAttributes to Attributes
- [init?(merging: [CVPixelBufferAttributes])](cvpixelbufferattributes/init(merging:).md)
  Resolve multiple attribute specifications into a single instance.
- [init(pixelFormatTypes: [CVPixelFormatType]?, size: CVImageSize?, compatibility: CVPixelFormatDescription.Compatibility, bytesPerRowAlignment: Int?, planeAlignment: Int?, extendedPixels: CVPixelBufferPadding?)](cvpixelbufferattributes/init(pixelformattypes:size:compatibility:bytesperrowalignment:planealignment:extendedpixels:).md)
- [init(rawAttributes: [String : any Sendable])](cvpixelbufferattributes/init(rawattributes:).md)
  Create an instance using a freeform attribute dictionary
### Instance Properties
- [var pixelFormatTypes: [CVPixelFormatType]?](cvpixelbufferattributes/pixelformattypes.md)
  Allow multiple pixel formats to be specified in attributes
- [var rawAttributes: [String : any Sendable]](cvpixelbufferattributes/rawattributes.md)
### Subscripts
- [subscript(dynamicMember _: WritableKeyPath<CVPixelBufferCreationAttributes, Int?>) -> Int?](cvpixelbufferattributes/subscript(dynamicmember:)-16n5o.md)
- [subscript(dynamicMember _: WritableKeyPath<CVPixelBufferCreationAttributes, CVPixelFormatDescription?>) -> CVPixelFormatDescription?](cvpixelbufferattributes/subscript(dynamicmember:)-2fcvp.md)
- [subscript(dynamicMember _: WritableKeyPath<CVPixelBufferCreationAttributes, CVPixelBufferPadding?>) -> CVPixelBufferPadding?](cvpixelbufferattributes/subscript(dynamicmember:)-2kg2b.md)
- [subscript(dynamicMember _: WritableKeyPath<CVPixelBufferCreationAttributes, CVPixelFormatDescription.Compatibility>) -> CVPixelFormatDescription.Compatibility](cvpixelbufferattributes/subscript(dynamicmember:)-4r0es.md)
- [subscript(dynamicMember _: WritableKeyPath<CVPixelBufferCreationAttributes, CVPixelFormatType>) -> CVPixelFormatType?](cvpixelbufferattributes/subscript(dynamicmember:)-63jp4.md)
- [subscript(dynamicMember _: WritableKeyPath<CVPixelBufferCreationAttributes, Bool>) -> Bool?](cvpixelbufferattributes/subscript(dynamicmember:)-7nhki.md)
- [subscript(dynamicMember _: WritableKeyPath<CVPixelBufferCreationAttributes, CVImageSize>) -> CVImageSize?](cvpixelbufferattributes/subscript(dynamicmember:)-95xgt.md)
- [subscript(dynamicMember _: WritableKeyPath<CVPixelBufferCreationAttributes, CVPixelBufferCreationAttributes.Backing>) -> CVPixelBufferCreationAttributes.Backing](cvpixelbufferattributes/subscript(dynamicmember:)-jo6l.md)

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvpixelbufferattributes)*