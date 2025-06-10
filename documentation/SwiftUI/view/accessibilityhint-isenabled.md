# accessibilityHint(_:isEnabled:)

**Framework**: SwiftUI  
**Kind**: method

Communicates to the user what happens after performing the view’s action.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
nonisolated
func accessibilityHint(_ hint: LocalizedStringResource, isEnabled: Bool) -> ModifiedContent<Self, AccessibilityAttachmentModifier>
```

#### Discussion

Provide a hint in the form of a brief phrase, like “Purchases the item” or “Downloads the attachment”.

## Parameters

- `hint`: The accessibility hint to apply.
- `isEnabled`: If true the accessibility hint is applied; otherwise the   accessibility hint is unchanged.

## See Also

- [func accessibilityHint(_:)](view/accessibilityhint(_:).md)
  Communicates to the user what happens after performing the view’s action.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/accessibilityhint(_:isenabled:))*