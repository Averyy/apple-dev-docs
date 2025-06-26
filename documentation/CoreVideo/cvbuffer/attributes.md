# CVBuffer.Attributes

**Framework**: Core Video  
**Kind**: struct

A partial set of pixel buffer creation attributes. This struct is useful for conveying partial requirements for pixel buffers to clients. This struct makes all properties of `CVPixelBuffer/CreationAttributes` optional.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)
- Unknown ?+ - Deprecated

## Declaration

```swift
@dynamicMemberLookup
struct Attributes
```

## Topics

### Initializers
- [init(CVBuffer.CreationAttributes)](cvbuffer/attributes/init(_:).md)
  Convert CreationAttributes to Attributes
- [init?(merging: [CVBuffer.Attributes])](cvbuffer/attributes/init(merging:).md)
  Resolve multiple attribute specifications into a single instance.
- [init(pixelFormatTypes: [CVPixelFormatType]?, size: CVImageSize?, compatibility: CVPixelFormatDescription.Compatibility, bytesPerRowAlignment: Int?, planeAlignment: Int?, extendedPixels: CVPixelBufferPadding?)](cvbuffer/attributes/init(pixelformattypes:size:compatibility:bytesperrowalignment:planealignment:extendedpixels:).md)
- [init(rawAttributes: [String : any Sendable])](cvbuffer/attributes/init(rawattributes:).md)
  Create an instance using a freeform attribute dictionary
### Instance Properties
- [var pixelFormatTypes: [CVPixelFormatType]?](cvbuffer/attributes/pixelformattypes.md)
  Allow multiple pixel formats to be specified in attributes
- [var rawAttributes: [String : any Sendable]](cvbuffer/attributes/rawattributes.md)
### Subscripts
- [subscript(dynamicMember _: WritableKeyPath<CVBuffer.CreationAttributes, CVBuffer.CreationAttributes.Backing>) -> CVBuffer.CreationAttributes.Backing](cvbuffer/attributes/subscript(dynamicmember:)-1c1om.md)
- [subscript(dynamicMember _: WritableKeyPath<CVBuffer.CreationAttributes, CVPixelFormatDescription?>) -> CVPixelFormatDescription?](cvbuffer/attributes/subscript(dynamicmember:)-1o2ji.md)
- [subscript(dynamicMember _: WritableKeyPath<CVBuffer.CreationAttributes, Bool>) -> Bool?](cvbuffer/attributes/subscript(dynamicmember:)-21rr.md)
- [subscript(dynamicMember _: WritableKeyPath<CVBuffer.CreationAttributes, Int?>) -> Int?](cvbuffer/attributes/subscript(dynamicmember:)-3c1w8.md)
- [subscript(dynamicMember _: WritableKeyPath<CVBuffer.CreationAttributes, CVPixelFormatDescription.Compatibility>) -> CVPixelFormatDescription.Compatibility](cvbuffer/attributes/subscript(dynamicmember:)-5m9xn.md)
- [subscript(dynamicMember _: WritableKeyPath<CVBuffer.CreationAttributes, CVPixelFormatType>) -> CVPixelFormatType?](cvbuffer/attributes/subscript(dynamicmember:)-6jvmi.md)
- [subscript(dynamicMember _: WritableKeyPath<CVBuffer.CreationAttributes, CVPixelBufferPadding?>) -> CVPixelBufferPadding?](cvbuffer/attributes/subscript(dynamicmember:)-7bidb.md)
- [subscript(dynamicMember _: WritableKeyPath<CVBuffer.CreationAttributes, CVImageSize>) -> CVImageSize?](cvbuffer/attributes/subscript(dynamicmember:)-9n8bh.md)

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvbuffer/attributes)*