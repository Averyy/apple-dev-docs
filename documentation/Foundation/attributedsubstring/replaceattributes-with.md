# replaceAttributes(_:with:)

**Framework**: Foundation  
**Kind**: method

Replaces the attributed substring’s attributes with those in a specified attribute container.

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

- [func setAttributes(AttributeContainer)](attributedsubstring/setattributes(_:).md)
  Sets the attributed substring’s attributes to those in a specified attribute container.
- [func mergeAttributes(AttributeContainer, mergePolicy: AttributedString.AttributeMergePolicy)](attributedsubstring/mergeattributes(_:mergepolicy:).md)
  Merges the attributed string’s attributes with those in a specified attribute container.
- [AttributedString.AttributeMergePolicy](attributedstring/attributemergepolicy.md)
  An enumeration of behaviors to apply when merging attributes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/attributedsubstring/replaceattributes(_:with:))*