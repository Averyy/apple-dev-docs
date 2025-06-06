# accessibilityCustomContent(_:_:importance:)

**Framework**: Musickit  
**Kind**: method

Add additional accessibility information to the view.

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
nonisolated
func accessibilityCustomContent(_ labelKey: LocalizedStringKey, _ value: Text, importance: AXCustomContent.Importance = .default) -> ModifiedContent<Self, AccessibilityAttachmentModifier>
```

#### Discussion

Use this method to add information you want accessibility users to be able to access about this element, beyond the basics of label, value, and hint. For example: `accessibilityCustomContent` can be used to add information about the orientation of a photograph, or the number of people found in the picture.

> **Note**: Repeated calls of `accessibilityCustomContent` with different labels will create new entries of additional information. Calling `accessibilityAdditionalContent` repeatedly with the same label will instead replace the previous value and importance.

## Parameters

- `label`: Localized text describing to the user what   is contained in this additional information entry. For example:   “orientation”.
- `value`: Text value for the additional accessibility   information. For example: “landscape.”
- `importance`: Importance of the accessibility information.   High-importance information gets read out immediately, while   default-importance information must be explicitly asked for by the   user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/musickit/artworkimage/accessibilitycustomcontent(_:_:importance:)-jy7u)*