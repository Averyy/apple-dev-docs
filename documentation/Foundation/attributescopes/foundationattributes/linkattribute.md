# AttributeScopes.FoundationAttributes.LinkAttribute

**Framework**: Foundation  
**Kind**: enum

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
- [static var name: String](attributescopes/foundationattributes/linkattribute/name.md)
  The name of the link attribute.
- [static func value(for: NSObject) throws -> URL](attributescopes/foundationattributes/linkattribute/value(for:).md)
  Returns the URL value of the specified object.
- [AttributeScopes.FoundationAttributes.LinkAttribute.Value](attributescopes/foundationattributes/linkattribute/value.md)
  The type of the link attribute’s value.
- [static func objectiveCValue(for: URL) throws -> NSObject](attributescopes/foundationattributes/linkattribute/objectivecvalue(for:).md)
  Returns an object for a specified URL value.
- [AttributeScopes.FoundationAttributes.LinkAttribute.ObjectiveCValue](attributescopes/foundationattributes/linkattribute/objectivecvalue.md)
  The type of the link attribute’s value when calling it from Objective-C.
### Default Implementations
- [ObjectiveCConvertibleAttributedStringKey Implementations](attributescopes/foundationattributes/linkattribute/objectivecconvertibleattributedstringkey-implementations.md)

## Relationships

### Conforms To
- [AttributedStringKey](attributedstringkey.md)
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Copyable](../Swift/Copyable.md)
- [DecodableAttributedStringKey](decodableattributedstringkey.md)
- [EncodableAttributedStringKey](encodableattributedstringkey.md)
- [Escapable](../Swift/Escapable.md)
- [ObjectiveCConvertibleAttributedStringKey](objectivecconvertibleattributedstringkey.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [let imageURL: AttributeScopes.FoundationAttributes.ImageURLAttribute](attributescopes/foundationattributes/imageurl.md)
  A property for accessing an image URL attribute.
- [AttributeScopes.FoundationAttributes.ImageURLAttribute](attributescopes/foundationattributes/imageurlattribute.md)
  A type for using an image URL as an attribute.
- [let link: AttributeScopes.FoundationAttributes.LinkAttribute](attributescopes/foundationattributes/link.md)
  A property for accessing the link attribute.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/attributescopes/foundationattributes/linkattribute)*