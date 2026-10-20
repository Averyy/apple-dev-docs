# CVPixelBufferAttributes

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
struct CVPixelBufferAttributes
```

## Topics

### Initializers
- [init(CVPixelBufferCreationAttributes)](./cvpixelbufferattributes/init%28_%29.md)
  Convert CreationAttributes to Attributes
- [init?(merging: [CVPixelBufferAttributes])](./cvpixelbufferattributes/init%28merging%29.md)
  Resolve multiple attribute specifications into a single instance.
- [init(pixelFormatTypes: [CVPixelFormatType]?, size: CVImageSize?, compatibility: CVPixelFormatDescription.Compatibility, bytesPerRowAlignment: Int?, planeAlignment: Int?, extendedPixels: CVPixelBufferPadding?)](./cvpixelbufferattributes/init%28pixelformattypes,size,compatibility,bytesperrowalignment,planealignment,extendedpixels%29.md)
- [init(rawAttributes: [String : any Sendable])](./cvpixelbufferattributes/init%28rawattributes%29.md)
  Create an instance using a freeform attribute dictionary
### Instance Properties
- [var attachments: CVAttachmentContainer<CVPixelBufferAttachmentKeyDefinitions>?](./cvpixelbufferattributes/attachments.md)
  Attachments to set on the pixel buffer.
- [var pixelFormatTypes: [CVPixelFormatType]?](./cvpixelbufferattributes/pixelformattypes.md)
  Allow multiple pixel formats to be specified in attributes
- [var rawAttributes: [String : any Sendable]](./cvpixelbufferattributes/rawattributes.md)
### Subscripts
- [subscript(dynamicMember _: WritableKeyPath<CVPixelBufferCreationAttributes, Int?>) -> Int?](./cvpixelbufferattributes/subscript%28dynamicmember%29-16n5o.md)
- [subscript(dynamicMember _: WritableKeyPath<CVPixelBufferCreationAttributes, CVPixelFormatDescription?>) -> CVPixelFormatDescription?](./cvpixelbufferattributes/subscript%28dynamicmember%29-2fcvp.md)
- [subscript(dynamicMember _: WritableKeyPath<CVPixelBufferCreationAttributes, CVPixelBufferPadding?>) -> CVPixelBufferPadding?](./cvpixelbufferattributes/subscript%28dynamicmember%29-2kg2b.md)
- [subscript(dynamicMember _: WritableKeyPath<CVPixelBufferCreationAttributes, CVPixelFormatDescription.Compatibility>) -> CVPixelFormatDescription.Compatibility](./cvpixelbufferattributes/subscript%28dynamicmember%29-4r0es.md)
- [subscript(dynamicMember _: WritableKeyPath<CVPixelBufferCreationAttributes, CVPixelFormatType>) -> CVPixelFormatType?](./cvpixelbufferattributes/subscript%28dynamicmember%29-63jp4.md)
- [subscript(dynamicMember _: WritableKeyPath<CVPixelBufferCreationAttributes, Bool>) -> Bool?](./cvpixelbufferattributes/subscript%28dynamicmember%29-7nhki.md)
- [subscript(dynamicMember _: WritableKeyPath<CVPixelBufferCreationAttributes, CVImageSize>) -> CVImageSize?](./cvpixelbufferattributes/subscript%28dynamicmember%29-95xgt.md)
- [subscript(dynamicMember _: WritableKeyPath<CVPixelBufferCreationAttributes, CVPixelBufferCreationAttributes.Backing>) -> CVPixelBufferCreationAttributes.Backing](./cvpixelbufferattributes/subscript%28dynamicmember%29-jo6l.md)

## Relationships

### Conforms To
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Swift overlay types
- [class CVReadOnlyPixelBuffer](./cvreadonlypixelbuffer.md)
  CVReadOnlyPixelBuffer provides an immutable view of the pixel data held by the pixel buffer.
- [struct CVMutablePixelBuffer](./cvmutablepixelbuffer.md)
  CVMutablePixelBuffer provides read-write access to the pixel data and attachments.
- [struct CVPixelBufferCreationAttributes](./cvpixelbuffercreationattributes.md)
  Attributes needed for creating a pixel buffer.
- [struct CVPixelBufferPadding](./cvpixelbufferpadding.md)
  Padding pixels around the CVPixelBuffer
- [struct CVPixelBufferPlaneProperties](./cvpixelbufferplaneproperties.md)
  Properties of a plane of pixels in pixel buffer
- [struct CVProResRawMetadata](./cvproresrawmetadata.md)
  Metadata associated with ProRes RAW images.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvpixelbufferattributes)*