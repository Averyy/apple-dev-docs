# accessibilityCustomContent(_:_:importance:)

**Framework**: FinanceKitUI  
**Kind**: method

Add additional accessibility information to the view.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- watchOS 9.0+

## Declaration

```swift
nonisolated
func accessibilityCustomContent(_ key: AccessibilityCustomContentKey, _ valueResource: LocalizedStringResource, importance: AXCustomContent.Importance = .default) -> ModifiedContent<Self, AccessibilityAttachmentModifier>
```

#### Discussion

Use this method to add information you want accessibility users to be able to access about this element, beyond the basics of label, value, and hint. For example, `accessibilityCustomContent` can be used to add information about the orientation of a photograph, or the number of people found in the picture.

> **Note**: Repeated calls of `accessibilityCustomContent` with `key`s having different identifiers will create new entries of additional information. Calling `accessibilityCustomContent` repeatedly with `key`s having matching identifiers will replace the previous entry.

## Parameters

- `key`: Key used to specify the identifier and label of the   of the additional accessibility information entry.
- `valueResource`: Text resource for the additional   accessibility information. For example: “landscape.” A value of    will remove any entry of additional information added earlier for any    withthe same identifier.
- `importance`: Importance of the accessibility information.   High-importance information gets read out immediately, while   default-importance information must be explicitly asked for by the   user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/financekitui/transactionpicker/accessibilitycustomcontent(_:_:importance:)-7yc8t)*