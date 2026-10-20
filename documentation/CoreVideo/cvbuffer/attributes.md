# CVBuffer.Attributes

**Framework**: Core Video  
**Kind**: struct  
**Role**: Structure

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
struct Attributes
```

## Topics

### Initializers
- [init(CVBuffer.CreationAttributes)](./attributes/init%28_%29.md)
  Convert CreationAttributes to Attributes
- [init?(merging: [CVBuffer.Attributes])](./attributes/init%28merging%29.md)
  Resolve multiple attribute specifications into a single instance.
- [init(pixelFormatTypes: [CVPixelFormatType]?, size: CVImageSize?, compatibility: CVPixelFormatDescription.Compatibility, bytesPerRowAlignment: Int?, planeAlignment: Int?, extendedPixels: CVPixelBufferPadding?)](./attributes/init%28pixelformattypes,size,compatibility,bytesperrowalignment,planealignment,extendedpixels%29.md)
- [init(rawAttributes: [String : any Sendable])](./attributes/init%28rawattributes%29.md)
  Create an instance using a freeform attribute dictionary
### Instance Properties
- [var pixelFormatTypes: [CVPixelFormatType]?](./attributes/pixelformattypes.md)
  Allow multiple pixel formats to be specified in attributes
- [var rawAttributes: [String : any Sendable]](./attributes/rawattributes.md)
### Subscripts
- [subscript(dynamicMember _: WritableKeyPath<CVBuffer.CreationAttributes, CVBuffer.CreationAttributes.Backing>) -> CVBuffer.CreationAttributes.Backing](./attributes/subscript%28dynamicmember%29-1c1om.md)
- [subscript(dynamicMember _: WritableKeyPath<CVBuffer.CreationAttributes, CVPixelFormatDescription?>) -> CVPixelFormatDescription?](./attributes/subscript%28dynamicmember%29-1o2ji.md)
- [subscript(dynamicMember _: WritableKeyPath<CVBuffer.CreationAttributes, Bool>) -> Bool?](./attributes/subscript%28dynamicmember%29-21rr.md)
- [subscript(dynamicMember _: WritableKeyPath<CVBuffer.CreationAttributes, Int?>) -> Int?](./attributes/subscript%28dynamicmember%29-3c1w8.md)
- [subscript(dynamicMember _: WritableKeyPath<CVBuffer.CreationAttributes, CVPixelFormatDescription.Compatibility>) -> CVPixelFormatDescription.Compatibility](./attributes/subscript%28dynamicmember%29-5m9xn.md)
- [subscript(dynamicMember _: WritableKeyPath<CVBuffer.CreationAttributes, CVPixelFormatType>) -> CVPixelFormatType?](./attributes/subscript%28dynamicmember%29-6jvmi.md)
- [subscript(dynamicMember _: WritableKeyPath<CVBuffer.CreationAttributes, CVPixelBufferPadding?>) -> CVPixelBufferPadding?](./attributes/subscript%28dynamicmember%29-7bidb.md)
- [subscript(dynamicMember _: WritableKeyPath<CVBuffer.CreationAttributes, CVImageSize>) -> CVImageSize?](./attributes/subscript%28dynamicmember%29-9n8bh.md)

## Relationships

### Conforms To
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvbuffer/attributes)*