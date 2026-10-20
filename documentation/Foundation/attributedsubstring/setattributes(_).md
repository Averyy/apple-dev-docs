# setAttributes(_:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Sets the attributed substring’s attributes to those in a specified attribute container.

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

### Applying and Modifying Attributes
- [func mergeAttributes(AttributeContainer, mergePolicy: AttributedString.AttributeMergePolicy)](./mergeattributes%28_,mergepolicy%29.md)
  Merges the attributed string’s attributes with those in a specified attribute container.
- [AttributedString.AttributeMergePolicy](../attributedstring/attributemergepolicy.md)
  An enumeration of behaviors to apply when merging attributes.
- [func replaceAttributes(AttributeContainer, with: AttributeContainer)](./replaceattributes%28_,with%29.md)
  Replaces the attributed substring’s attributes with those in a specified attribute container.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/attributedsubstring/setattributes(_:))*