# accessibilityHint(_:)

**Framework**: PermissionKit  
**Kind**: method

Communicates to the user what happens after performing the view’s action.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 26.0+ (Beta)
- watchOS 7.0+

## Declaration

```swift
nonisolated
func accessibilityHint(_ hintKey: LocalizedStringKey) -> ModifiedContent<Self, AccessibilityAttachmentModifier>
```

#### Discussion

Provide a hint in the form of a brief phrase, like “Purchases the item” or “Downloads the attachment”.


---

*[View on Apple Developer](https://developer.apple.com/documentation/permissionkit/communicationlimitsbutton/accessibilityhint(_:)-25l3a)*