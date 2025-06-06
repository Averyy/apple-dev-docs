# accessibilityLabel(content:)

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
func accessibilityLabel<V>(@ViewBuilder content: (PlaceholderContentView<Self>) -> V) -> some View where V : View
```

#### Discussion

Use this method to append content to the accessibility label for a view. For example, you could use this method to label a badge or alert that is custom drawn without removing the existing accessibility label.

## Parameters

- `content`: A view builder closure that takes a proxy   value representing the modified view. You can combine the modified   view with other content to create a new accessibility label for   the original view.

## See Also

- [func accessibilityLabel(_:)](view/accessibilitylabel(_:).md)
  Adds a label to the view that describes its contents.
- [func accessibilityLabel(_:isEnabled:)](view/accessibilitylabel(_:isenabled:).md)
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

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/accessibilitylabel(content:))*