# mergeAttributes(_:mergePolicy:)

**Framework**: Foundation  
**Kind**: method  
**Required**: Yes

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
mutating func mergeAttributes(_ attributes: AttributeContainer, mergePolicy: AttributedString.AttributeMergePolicy)
```

## Parameters

- `attributes`: The attribute container with the attributes to merge.
- `mergePolicy`: A policy to use when resolving conflicts between this string’s attributes and those in  .

## See Also

- [func setAttributes(AttributeContainer)](attributedstringattributemutation/setattributes(_:).md)
  Sets the attributed string’s attributes to those in a specified attribute container.
- [func replaceAttributes(AttributeContainer, with: AttributeContainer)](attributedstringattributemutation/replaceattributes(_:with:).md)
  Replaces the attributed string’s attributes with those in a specified attribute container.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/attributedstringattributemutation/mergeattributes(_:mergepolicy:))*