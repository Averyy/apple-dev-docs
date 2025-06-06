# replaceAttributes(_:with:)

**Framework**: Foundation  
**Kind**: method  
**Required**: Yes

Replaces the attributed string’s attributes with those in a specified attribute container.

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

- [func setAttributes(AttributeContainer)](attributedstringattributemutation/setattributes(_:).md)
  Sets the attributed string’s attributes to those in a specified attribute container.
- [func mergeAttributes(AttributeContainer, mergePolicy: AttributedString.AttributeMergePolicy)](attributedstringattributemutation/mergeattributes(_:mergepolicy:).md)
  Merges the attributed string’s attributes with those in a specified attribute container.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/attributedstringattributemutation/replaceattributes(_:with:))*