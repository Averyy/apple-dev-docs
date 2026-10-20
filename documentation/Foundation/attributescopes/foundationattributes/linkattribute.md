# AttributeScopes.FoundationAttributes.LinkAttribute

**Framework**: Foundation  
**Kind**: enum  
**Role**: Enumeration

A type for using a link as an attribute.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
@frozen
enum LinkAttribute
```

## Topics

### Accessing the Attribute Name and Value
- [static var name: String](./linkattribute/name.md)
  The name of the link attribute.
- [static func value(for: NSObject) throws -> URL](./linkattribute/value%28for%29.md)
  Returns the URL value of the specified object.
- [AttributeScopes.FoundationAttributes.LinkAttribute.Value](./linkattribute/value.md)
  The type of the link attribute’s value.
- [static func objectiveCValue(for: URL) throws -> NSObject](./linkattribute/objectivecvalue%28for%29.md)
  Returns an object for a specified URL value.
- [AttributeScopes.FoundationAttributes.LinkAttribute.ObjectiveCValue](./linkattribute/objectivecvalue.md)
  The type of the link attribute’s value when calling it from Objective-C.
### Default Implementations
- [ObjectiveCConvertibleAttributedStringKey Implementations](./linkattribute/objectivecconvertibleattributedstringkey-implementations.md)

## Relationships

### Conforms To
- [AttributedStringKey](../../attributedstringkey.md)
- [BitwiseCopyable](../../../Swift/bitwisecopyable.md)
- [Copyable](../../../Swift/copyable.md)
- [DecodableAttributedStringKey](../../decodableattributedstringkey.md)
- [EncodableAttributedStringKey](../../encodableattributedstringkey.md)
- [Escapable](../../../Swift/escapable.md)
- [ObjectiveCConvertibleAttributedStringKey](../../objectivecconvertibleattributedstringkey.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)

## See Also

### Using URL attributes
- [let imageURL: AttributeScopes.FoundationAttributes.ImageURLAttribute](./imageurl.md)
  A property for accessing an image URL attribute.
- [AttributeScopes.FoundationAttributes.ImageURLAttribute](./imageurlattribute.md)
  A type for using an image URL as an attribute.
- [let link: AttributeScopes.FoundationAttributes.LinkAttribute](./link.md)
  A property for accessing the link attribute.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/attributescopes/foundationattributes/linkattribute)*