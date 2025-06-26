# accessibilityLabeledPair(role:id:in:)

**Framework**: FamilyControls  
**Kind**: method

Pairs an accessibility element representing a label with the element for the matching content.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- macOS 11.0+
- tvOS 14.0+
- watchOS 7.0+

## Declaration

```swift
nonisolated
func accessibilityLabeledPair<ID>(role: AccessibilityLabeledPairRole, id: ID, in namespace: Namespace.ID) -> some View where ID : Hashable
```

#### Discussion

Use `accessibilityLabeledPair` with a role of `AccessibilityLabeledPairRole.label` to identify the label, and a role of `AccessibilityLabeledPairRole.content` to identify the content. This improves the behavior of accessibility features such as VoiceOver when navigating such elements, allowing users to better understand the relationship between them.

## Parameters

- `role`: Determines whether this element should be used as the label   in the pair, or the content in the pair.
- `id`: The identifier for the label / content pair. Elements with   matching identifiers within the same namespace will be paired   together.
- `namespace`: The namespace used to organize label and content. Label   and content under the same namespace with matching identifiers will   be paired together.

## See Also

- [func accessibilityLabel<S>(S) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](familyactivitypicker/accessibilitylabel(_:)-1ee7a.md)
  Adds a label to the view that describes its contents.
- [func accessibilityLabel(Text) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](familyactivitypicker/accessibilitylabel(_:)-1ug11.md)
  Adds a label to the view that describes its contents.
- [func accessibilityLabel(LocalizedStringKey) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](familyactivitypicker/accessibilitylabel(_:)-1goip.md)
  Adds a label to the view that describes its contents.
- [func accessibilityInputLabels([LocalizedStringKey]) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](familyactivitypicker/accessibilityinputlabels(_:)-1ijca.md)
  Sets alternate input labels with which users identify a view.
- [func accessibilityInputLabels([Text]) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](familyactivitypicker/accessibilityinputlabels(_:)-8dgot.md)
  Sets alternate input labels with which users identify a view.
- [func accessibilityInputLabels<S>([S]) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](familyactivitypicker/accessibilityinputlabels(_:)-9t208.md)
  Sets alternate input labels with which users identify a view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/familycontrols/familyactivitypicker/accessibilitylabeledpair(role:id:in:))*