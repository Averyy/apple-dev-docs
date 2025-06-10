# accessibilityLabel(_:isEnabled:)

**Framework**: SwiftUI  
**Kind**: method

Adds a label to the view that describes its contents.

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
func accessibilityLabel(_ label: LocalizedStringResource, isEnabled: Bool) -> ModifiedContent<Self, AccessibilityAttachmentModifier>
```

#### Discussion

Use this method to provide an accessibility label for a view that doesn’t display text, like an icon. For example, you could use this method to label a button that plays music with the text “Play”. Don’t include text in the label that repeats information that users already have. For example, don’t use the label “Play button” because a button already has a trait that identifies it as a button.

## Parameters

- `label`: The accessibility label to apply.
- `isEnabled`: If true the accessibility label is applied; otherwise   the accessibility label is unchanged.

## See Also

- [func accessibilityLabel(_:)](view/accessibilitylabel(_:).md)
  Adds a label to the view that describes its contents.
- [func accessibilityLabel<V>(content: (PlaceholderContentView<Self>) -> V) -> some View](view/accessibilitylabel(content:).md)
  Adds a label to the view that describes its contents.
- [func accessibilityInputLabels(_:)](view/accessibilityinputlabels(_:).md)
  Sets alternate input labels with which users identify a view.
- [func accessibilityInputLabels(_:isEnabled:)](view/accessibilityinputlabels(_:isenabled:).md)
  Sets alternate input labels with which users identify a view.
- [func accessibilityLabeledPair<ID>(role: AccessibilityLabeledPairRole, id: ID, in: Namespace.ID) -> some View](view/accessibilitylabeledpair(role:id:in:).md)
  Pairs an accessibility element representing a label with the element for the matching content.
- [enum AccessibilityLabeledPairRole](accessibilitylabeledpairrole.md)
  The role of an accessibility element in a label / content pair.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/accessibilitylabel(_:isenabled:))*