# mergeAttributes(_:mergePolicy:)

**Framework**: Foundation  
**Kind**: method

Merges the attributed string’s attributes with those in a specified attribute container.

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
mutating func mergeAttributes(_ attributes: AttributeContainer, mergePolicy: AttributedString.AttributeMergePolicy = .keepNew)
```

## Parameters

- `attributes`: The attribute container with the attributes to merge.
- `mergePolicy`: A policy to use when resolving conflicts between this string’s attributes and those in `attributes`.

## See Also

- [func setAttributes(AttributeContainer)](attributedstring/setattributes(_:).md)
  Sets the attributed string’s attributes to those in a specified attribute container.
- [AttributedString.AttributeMergePolicy](attributedstring/attributemergepolicy.md)
  An enumeration of behaviors to apply when merging attributes.
- [func replaceAttributes(AttributeContainer, with: AttributeContainer)](attributedstring/replaceattributes(_:with:).md)
  Replaces occurrences of attributes in one attribute container with those in another attribute container.
- [protocol AttributedStringAttributeMutation](attributedstringattributemutation.md)
  A protocol that defines in-place mutations for attributes in an attributed string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/attributedstring/mergeattributes(_:mergepolicy:))*