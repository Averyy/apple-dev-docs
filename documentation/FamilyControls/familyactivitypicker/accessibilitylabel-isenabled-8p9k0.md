# accessibilityLabel(_:isEnabled:)

**Framework**: FamilyControls  
**Kind**: method

Adds a label to the view that describes its contents.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
nonisolated
func accessibilityLabel<S>(_ label: S, isEnabled: Bool) -> ModifiedContent<Self, AccessibilityAttachmentModifier> where S : StringProtocol
```

#### Discussion

Use this method to provide an accessibility label for a view that doesn’t display text, like an icon. For example, you could use this method to label a button that plays music with the text “Play”. Don’t include text in the label that repeats information that users already have. For example, don’t use the label “Play button” because a button already has a trait that identifies it as a button.

## Parameters

- `label`: The accessibility label to apply.
- `isEnabled`: If true the accessibility label is applied; otherwise   the accessibility label is unchanged.


---

*[View on Apple Developer](https://developer.apple.com/documentation/familycontrols/familyactivitypicker/accessibilitylabel(_:isenabled:)-8p9k0)*