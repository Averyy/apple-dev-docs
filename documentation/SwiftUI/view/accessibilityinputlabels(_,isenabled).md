# accessibilityInputLabels(_:isEnabled:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Sets alternate input labels with which users identify a view.

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
func accessibilityInputLabels(_ inputLabelKeys: [LocalizedStringKey], isEnabled: Bool) -> ModifiedContent<Self, AccessibilityAttachmentModifier>
```

**Other overloads**:

```swift
nonisolated
func accessibilityInputLabels(_ inputLabels: [Text], isEnabled: Bool) -> ModifiedContent<Self, AccessibilityAttachmentModifier>
```

```swift
nonisolated
func accessibilityInputLabels<S>(_ inputLabels: [S], isEnabled: Bool) -> ModifiedContent<Self, AccessibilityAttachmentModifier> where S : StringProtocol
```

## Discussion

Provide labels in descending order of importance. Voice Control and Full Keyboard Access use the input labels.

> **Note**: If you don’t specify any input labels, the user can still refer to the view using the accessibility label that you add with the `accessibilityLabel()` modifier.

## Parameters

- `inputLabelKeys`: The accessibility input labels to apply.
- `isEnabled`: If true the accessibility input labels are applied; otherwise the accessibility input labels are unchanged.

## See Also

### Applying labels
- [func accessibilityLabel(_:)](./accessibilitylabel%28_%29.md)
  Adds a label to the view that describes its contents.
- [func accessibilityLabel(_:isEnabled:)](./accessibilitylabel%28_,isenabled%29.md)
  Adds a label to the view that describes its contents.
- [func accessibilityLabel<V>(content: (PlaceholderContentView<Self>) -> V) -> some View](./accessibilitylabel%28content%29.md)
  Adds a label to the view that describes its contents.
- [func accessibilityInputLabels(_:)](./accessibilityinputlabels%28_%29.md)
  Sets alternate input labels with which users identify a view.
- [func accessibilityLabeledPair<ID>(role: AccessibilityLabeledPairRole, id: ID, in: Namespace.ID) -> some View](./accessibilitylabeledpair%28role,id,in%29.md)
  Pairs an accessibility element representing a label with the element for the matching content.
- [enum AccessibilityLabeledPairRole](../accessibilitylabeledpairrole.md)
  The role of an accessibility element in a label / content pair.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/accessibilityinputlabels(_:isenabled:))*