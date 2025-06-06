# accessibilityCustomContent(_:_:importance:)

**Framework**: Financekitui  
**Kind**: method

Add additional accessibility information to the view.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- watchOS 8.0+

## Declaration

```swift
nonisolated
func accessibilityCustomContent(_ key: AccessibilityCustomContentKey, _ value: Text?, importance: AXCustomContent.Importance = .default) -> ModifiedContent<Self, AccessibilityAttachmentModifier>
```

#### Discussion

Use this method to add information you want accessibility users to be able to access about this element, beyond the basics of label, value, and hint. For example, `accessibilityCustomContent` can be used to add information about the orientation of a photograph, or the number of people found in the picture.

> **Note**: Repeated calls of `accessibilityCustomContent` with `key`s having different identifiers will create new entries of additional information. Calling `accessibilityAdditionalContent` repeatedly with `key`s having matching identifiers will replace the previous entry.

## Parameters

- `key`: Key used to specify the identifier and label of the   of the additional accessibility information entry.
- `value`: Text value for the additional accessibility   information. For example: “landscape.” A value of   will remove   any entry of additional information added earlier for any   with   the same identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/financekitui/addordertowalletbutton/accessibilitycustomcontent(_:_:importance:)-7ld6t)*