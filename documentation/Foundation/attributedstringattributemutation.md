# AttributedStringAttributeMutation

**Framework**: Foundation  
**Kind**: protocol  
**Role**: Protocol

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
- [func setAttributes(AttributeContainer)](./attributedstringattributemutation/setattributes%28_%29.md)
  Sets the attributed string’s attributes to those in a specified attribute container.
- [func mergeAttributes(AttributeContainer, mergePolicy: AttributedString.AttributeMergePolicy)](./attributedstringattributemutation/mergeattributes%28_,mergepolicy%29.md)
  Merges the attributed string’s attributes with those in a specified attribute container.
- [func replaceAttributes(AttributeContainer, with: AttributeContainer)](./attributedstringattributemutation/replaceattributes%28_,with%29.md)
  Replaces the attributed string’s attributes with those in a specified attribute container.

## Relationships

### Inherited By
- [AttributedStringProtocol](./attributedstringprotocol.md)
### Conforming Types
- [AttributedString](./attributedstring.md)
- [AttributedSubstring](./attributedsubstring.md)
- [DiscontiguousAttributedSubstring](./discontiguousattributedsubstring.md)

## See Also

### Applying and Modifying Attributes
- [func setAttributes(AttributeContainer)](./attributedstring/setattributes%28_%29.md)
  Sets the attributed string’s attributes to those in a specified attribute container.
- [func mergeAttributes(AttributeContainer, mergePolicy: AttributedString.AttributeMergePolicy)](./attributedstring/mergeattributes%28_,mergepolicy%29.md)
  Merges the attributed string’s attributes with those in a specified attribute container.
- [AttributedString.AttributeMergePolicy](./attributedstring/attributemergepolicy.md)
  An enumeration of behaviors to apply when merging attributes.
- [func replaceAttributes(AttributeContainer, with: AttributeContainer)](./attributedstring/replaceattributes%28_,with%29.md)
  Replaces occurrences of attributes in one attribute container with those in another attribute container.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/attributedstringattributemutation)*