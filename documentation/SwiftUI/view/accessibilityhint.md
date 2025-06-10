# accessibilityHint(_:)

**Framework**: SwiftUI  
**Kind**: method

Communicates to the user what happens after performing the view’s action.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
nonisolated
func accessibilityHint(_ hint: LocalizedStringResource) -> ModifiedContent<Self, AccessibilityAttachmentModifier>
```

#### Discussion

Provide a hint in the form of a brief phrase, like “Purchases the item” or “Downloads the attachment”.

## See Also

- [func accessibilityHint(_:isEnabled:)](view/accessibilityhint(_:isenabled:).md)
  Communicates to the user what happens after performing the view’s action.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/accessibilityhint(_:))*