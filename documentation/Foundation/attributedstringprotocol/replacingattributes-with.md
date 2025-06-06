# replacingAttributes(_:with:)

**Framework**: Foundation  
**Kind**: method

Returns an attributed string by replacing occurrences of attributes in one attribute container with those in another attribute container.

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
func replacingAttributes(_ attributes: AttributeContainer, with others: AttributeContainer) -> AttributedString
```

#### Return Value

An attributed string created by replacing occurrences of attributes in one attribute container with those in another attribute container.

## Parameters

- `attributes`: The existing attributes to replace.
- `others`: The new attributes to apply.

## See Also

- [func settingAttributes(AttributeContainer) -> AttributedString](attributedstringprotocol/settingattributes(_:).md)
  Returns an attributed string by setting the attributed string’s attributes to those in a specified attribute container.
- [func mergingAttributes(AttributeContainer, mergePolicy: AttributedString.AttributeMergePolicy) -> AttributedString](attributedstringprotocol/mergingattributes(_:mergepolicy:).md)
  Returns an attributed string by merging the attributed string’s attributes with those in a specified attribute container.
- [AttributedString.AttributeMergePolicy](attributedstring/attributemergepolicy.md)
  An enumeration of behaviors to apply when merging attributes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/attributedstringprotocol/replacingattributes(_:with:))*