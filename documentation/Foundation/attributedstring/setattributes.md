# setAttributes(_:)

**Framework**: Foundation  
**Kind**: method

Sets the attributed string’s attributes to those in a specified attribute container.

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
mutating func setAttributes(_ attributes: AttributeContainer)
```

## Parameters

- `attributes`: The attribute container with the attributes to apply.

## See Also

- [func mergeAttributes(AttributeContainer, mergePolicy: AttributedString.AttributeMergePolicy)](attributedstring/mergeattributes(_:mergepolicy:).md)
  Merges the attributed string’s attributes with those in a specified attribute container.
- [AttributedString.AttributeMergePolicy](attributedstring/attributemergepolicy.md)
  An enumeration of behaviors to apply when merging attributes.
- [func replaceAttributes(AttributeContainer, with: AttributeContainer)](attributedstring/replaceattributes(_:with:).md)
  Replaces occurrences of attributes in one attribute container with those in another attribute container.
- [protocol AttributedStringAttributeMutation](attributedstringattributemutation.md)
  A protocol that defines in-place mutations for attributes in an attributed string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/attributedstring/setattributes(_:))*