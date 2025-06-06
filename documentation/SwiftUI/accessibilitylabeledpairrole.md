# AccessibilityLabeledPairRole

**Framework**: SwiftUI  
**Kind**: enum

The role of an accessibility element in a label / content pair.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
@frozen
enum AccessibilityLabeledPairRole
```

## Topics

### Getting roles
- [AccessibilityLabeledPairRole.content](accessibilitylabeledpairrole/content.md)
  This element represents the content part of the label / content pair.
- [AccessibilityLabeledPairRole.label](accessibilitylabeledpairrole/label.md)
  This element represents the label part of the label / content pair.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [func accessibilityLabel(_:)](view/accessibilitylabel(_:).md)
  Adds a label to the view that describes its contents.
- [func accessibilityLabel(_:isEnabled:)](view/accessibilitylabel(_:isenabled:).md)
  Adds a label to the view that describes its contents.
- [func accessibilityLabel<V>(content: (PlaceholderContentView<Self>) -> V) -> some View](view/accessibilitylabel(content:).md)
  Adds a label to the view that describes its contents.
- [func accessibilityInputLabels(_:)](view/accessibilityinputlabels(_:).md)
  Sets alternate input labels with which users identify a view.
- [func accessibilityInputLabels(_:isEnabled:)](view/accessibilityinputlabels(_:isenabled:).md)
  Sets alternate input labels with which users identify a view.
- [func accessibilityLabeledPair<ID>(role: AccessibilityLabeledPairRole, id: ID, in: Namespace.ID) -> some View](view/accessibilitylabeledpair(role:id:in:).md)
  Pairs an accessibility element representing a label with the element for the matching content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/accessibilitylabeledpairrole)*