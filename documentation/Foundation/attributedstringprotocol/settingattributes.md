# settingAttributes(_:)

**Framework**: Foundation  
**Kind**: method

Returns an attributed string by setting the attributed string’s attributes to those in a specified attribute container.

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
func settingAttributes(_ attributes: AttributeContainer) -> AttributedString
```

#### Return Value

An attributed string from setting the attributed string’s attributes to those in a specified attribute container.

## Parameters

- `attributes`: The attribute container with the attributes to apply.

## See Also

- [func mergingAttributes(AttributeContainer, mergePolicy: AttributedString.AttributeMergePolicy) -> AttributedString](attributedstringprotocol/mergingattributes(_:mergepolicy:).md)
  Returns an attributed string by merging the attributed string’s attributes with those in a specified attribute container.
- [AttributedString.AttributeMergePolicy](attributedstring/attributemergepolicy.md)
  An enumeration of behaviors to apply when merging attributes.
- [func replacingAttributes(AttributeContainer, with: AttributeContainer) -> AttributedString](attributedstringprotocol/replacingattributes(_:with:).md)
  Returns an attributed string by replacing occurrences of attributes in one attribute container with those in another attribute container.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/attributedstringprotocol/settingattributes(_:))*