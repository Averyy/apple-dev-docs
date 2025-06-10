# accessibilityLabel(_:)

**Framework**: FamilyControls  
**Kind**: method

Adds a label to the view that describes its contents.

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
func accessibilityLabel(_ label: LocalizedStringResource) -> ModifiedContent<Self, AccessibilityAttachmentModifier>
```

#### Discussion

Use this method to provide an accessibility label for a view that doesn’t display text, like an icon. For example, you could use this method to label a button that plays music with the text “Play”. Don’t include text in the label that repeats information that users already have. For example, don’t use the label “Play button” because a button already has a trait that identifies it as a button.


---

*[View on Apple Developer](https://developer.apple.com/documentation/familycontrols/familyactivitypicker/accessibilitylabel(_:)-87lk3)*