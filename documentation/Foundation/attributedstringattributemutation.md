# AttributedStringAttributeMutation

**Framework**: Foundation  
**Kind**: protocol

A protocol that defines in-place mutations for attributes in an attributed string.

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
protocol AttributedStringAttributeMutation
```

## Topics

### Mutating the String’s Attributes
- [func setAttributes(AttributeContainer)](attributedstringattributemutation/setattributes(_:).md)
  Sets the attributed string’s attributes to those in a specified attribute container.
- [func mergeAttributes(AttributeContainer, mergePolicy: AttributedString.AttributeMergePolicy)](attributedstringattributemutation/mergeattributes(_:mergepolicy:).md)
  Merges the attributed string’s attributes with those in a specified attribute container.
- [func replaceAttributes(AttributeContainer, with: AttributeContainer)](attributedstringattributemutation/replaceattributes(_:with:).md)
  Replaces the attributed string’s attributes with those in a specified attribute container.

## Relationships

### Inherited By
- [AttributedStringProtocol](attributedstringprotocol.md)
### Conforming Types
- [AttributedString](attributedstring.md)
- [AttributedSubstring](attributedsubstring.md)

## See Also

- [AttributedString.AttributeMergePolicy](attributedstring/attributemergepolicy.md)
  An enumeration of behaviors to apply when merging attributes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/attributedstringattributemutation)*