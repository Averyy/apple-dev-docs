# accessibilityHint(_:)

**Framework**: ManagedAppDistribution  
**Kind**: method

Communicates to the user what happens after performing the view’s action.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- macOS 13.0+
- tvOS 16.0+
- watchOS 9.0+

## Declaration

```swift
nonisolated
func accessibilityHint(_ hint: LocalizedStringResource) -> ModifiedContent<Self, AccessibilityAttachmentModifier>
```

#### Discussion

Provide a hint in the form of a brief phrase, like “Purchases the item” or “Downloads the attachment”.


---

*[View on Apple Developer](https://developer.apple.com/documentation/managedappdistribution/managedcontentview/accessibilityhint(_:)-38znu)*