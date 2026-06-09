# replaceAttributes(_:with:)

**Framework**: Foundation  
**Kind**: method

Replaces occurrences of attributes in one attribute container with those in another attribute container.

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
mutating func replaceAttributes(_ attributes: AttributeContainer, with others: AttributeContainer)
```

## Parameters

- `attributes`: The existing attributes to replace.
- `others`: The new attributes to apply.

## See Also

- [func setAttributes(AttributeContainer)](attributedstring/setattributes(_:).md)
  Sets the attributed string’s attributes to those in a specified attribute container.
- [func mergeAttributes(AttributeContainer, mergePolicy: AttributedString.AttributeMergePolicy)](attributedstring/mergeattributes(_:mergepolicy:).md)
  Merges the attributed string’s attributes with those in a specified attribute container.
- [AttributedString.AttributeMergePolicy](attributedstring/attributemergepolicy.md)
  An enumeration of behaviors to apply when merging attributes.
- [protocol AttributedStringAttributeMutation](attributedstringattributemutation.md)
  A protocol that defines in-place mutations for attributes in an attributed string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/attributedstring/replaceattributes(_:with:))*