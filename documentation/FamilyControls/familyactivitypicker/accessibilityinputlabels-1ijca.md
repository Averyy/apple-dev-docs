# accessibilityInputLabels(_:)

**Framework**: FamilyControls  
**Kind**: method

Sets alternate input labels with which users identify a view.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- watchOS 7.0+

## Declaration

```swift
nonisolated
func accessibilityInputLabels(_ inputLabelKeys: [LocalizedStringKey]) -> ModifiedContent<Self, AccessibilityAttachmentModifier>
```

#### Discussion

Provide labels in descending order of importance. Voice Control and Full Keyboard Access use the input labels.

> **Note**: If you don’t specify any input labels, the user can still refer to the view using the accessibility label that you add with the `accessibilityLabel()` modifier.

## See Also

- [func accessibilityLabel<S>(S) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](familyactivitypicker/accessibilitylabel(_:)-1ee7a.md)
  Adds a label to the view that describes its contents.
- [func accessibilityLabel(Text) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](familyactivitypicker/accessibilitylabel(_:)-1ug11.md)
  Adds a label to the view that describes its contents.
- [func accessibilityLabel(LocalizedStringKey) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](familyactivitypicker/accessibilitylabel(_:)-1goip.md)
  Adds a label to the view that describes its contents.
- [func accessibilityInputLabels([Text]) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](familyactivitypicker/accessibilityinputlabels(_:)-8dgot.md)
  Sets alternate input labels with which users identify a view.
- [func accessibilityInputLabels<S>([S]) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](familyactivitypicker/accessibilityinputlabels(_:)-9t208.md)
  Sets alternate input labels with which users identify a view.
- [func accessibilityLabeledPair<ID>(role: AccessibilityLabeledPairRole, id: ID, in: Namespace.ID) -> some View](familyactivitypicker/accessibilitylabeledpair(role:id:in:).md)
  Pairs an accessibility element representing a label with the element for the matching content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/familycontrols/familyactivitypicker/accessibilityinputlabels(_:)-1ijca)*