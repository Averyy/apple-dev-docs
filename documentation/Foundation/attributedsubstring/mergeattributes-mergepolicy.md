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

- [func setAttributes(AttributeContainer)](attributedsubstring/setattributes(_:).md)
  Sets the attributed substring’s attributes to those in a specified attribute container.
- [AttributedString.AttributeMergePolicy](attributedstring/attributemergepolicy.md)
  An enumeration of behaviors to apply when merging attributes.
- [func replaceAttributes(AttributeContainer, with: AttributeContainer)](attributedsubstring/replaceattributes(_:with:).md)
  Replaces the attributed substring’s attributes with those in a specified attribute container.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/attributedsubstring/mergeattributes(_:mergepolicy:))*