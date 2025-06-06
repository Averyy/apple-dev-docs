# accessibilityHint(_:isEnabled:)

**Framework**: FamilyControls  
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
func accessibilityHint(_ hintKey: LocalizedStringKey, isEnabled: Bool) -> ModifiedContent<Self, AccessibilityAttachmentModifier>
```

#### Discussion

Provide a hint in the form of a brief phrase, like “Purchases the item” or “Downloads the attachment”.

## Parameters

- `hintKey`: The accessibility hint to apply.
- `isEnabled`: If true the accessibility hint is applied; otherwise the   accessibility hint is unchanged.


---

*[View on Apple Developer](https://developer.apple.com/documentation/familycontrols/familyactivitypicker/accessibilityhint(_:isenabled:)-5vt3k)*