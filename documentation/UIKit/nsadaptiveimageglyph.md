# NSAdaptiveImageGlyph

**Framework**: UIKit  
**Kind**: class

A data object for an emoji-like image that can appear in attributed text.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
class NSAdaptiveImageGlyph
```

#### Overview

An [`NSAdaptiveImageGlyph`](nsadaptiveimageglyph.md) contains an image that automatically adapts to different sizes and resolutions. The text system creates instances of this type to represent custom emojis that people create using the system interfaces. This type manages multiple images, along with metadata describing how to adapt those images correctly to different fonts and font attributes.

Typically, you receive new [`NSAdaptiveImageGlyph`](nsadaptiveimageglyph.md) objects only from the text-input system. When someone creates a new emoji and inserts it into their text, TextKit creates an instance of this type to represent it. If your app examines or changes the attributes of attributed strings, preserve the doc://com.apple.documentation/documentation/foundation/nsattributedstring/key/4395176-adaptiveimageglyph attribute in Swift or the [`NSAdaptiveImageGlyphAttributeName`](nsadaptiveimageglyphattributename.md) attribute in Objective-C when making any changes. For example, if you filter unknown attributes in a custom text-storage object, update your code to preserve this attribute. The value of the attribute is an [`NSAdaptiveImageGlyph`](nsadaptiveimageglyph.md) containing the emoji data. You can save the image data with the rest of your content and use the data to recreate the type later.

## Topics

### Creating an adaptive image glyph
- [init(imageContent: Data)](nsadaptiveimageglyph/init(imagecontent:).md)
  Create an adaptive image glyph from the previously saved data.
- [init(coder: NSCoder)](nsadaptiveimageglyph/init(coder:).md)
### Getting the image data
- [var imageContent: Data](nsadaptiveimageglyph/imagecontent.md)
  The raw data for the image.
### Getting the content metadata
- [var contentIdentifier: String](nsadaptiveimageglyph/contentidentifier.md)
  A unique identifier for this image.
- [var contentDescription: String](nsadaptiveimageglyph/contentdescription.md)
  An alternate textual description of the image contents.
- [class var contentType: UTType](nsadaptiveimageglyph/contenttype.md)
  The image data format to use for this image type.
### Initializers
- [convenience init(AttributedString.AdaptiveImageGlyph)](nsadaptiveimageglyph/init(_:).md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CTAdaptiveImageProviding](../CoreText/CTAdaptiveImageProviding.md)
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class NSTextAttachment](nstextattachment.md)
  The values for the attachment characteristics of attributed strings and related objects.
- [class NSTextAttachmentViewProvider](nstextattachmentviewprovider.md)
  A container object that associates a text attachment at a particular document location with a view object.
- [protocol NSTextAttachmentContainer](nstextattachmentcontainer.md)
  A set of methods that defines the interface to text attachment objects from a layout manager.
- [protocol NSTextAttachmentLayout](nstextattachmentlayout.md)
  A set of methods that defines the interface to attachment objects from a text layout manager.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nsadaptiveimageglyph)*