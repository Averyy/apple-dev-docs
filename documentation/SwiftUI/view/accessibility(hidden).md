# accessibility(hidden:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Specifies whether to hide this view from system accessibility features.

**Availability**:
- iOS 13.0+ - Deprecated in 27.2 (renamed: accessibilityHidden(_:))
- iPadOS 13.0+ - Deprecated in 27.2 (renamed: accessibilityHidden(_:))
- Mac Catalyst 13.0+ - Deprecated in 27.2 (renamed: accessibilityHidden(_:))
- macOS 10.15+ - Deprecated in 27.2 (renamed: accessibilityHidden(_:))
- tvOS 13.0+ - Deprecated in 27.2 (renamed: accessibilityHidden(_:))
- visionOS 1.0+ - Deprecated in 27.2 (renamed: accessibilityHidden(_:))
- watchOS 6.0+ - Deprecated in 27.2 (renamed: accessibilityHidden(_:))

> **Deprecated**: Use [`accessibilityHidden(_:)`](./accessibilityhidden%28_%29.md) instead.

## Declaration

```swift
nonisolated
func accessibility(hidden: Bool) -> ModifiedContent<Self, AccessibilityAttachmentModifier>
```

## See Also

### Accessibility modifiers
- [func accessibility(label: Text) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](./accessibility%28label%29.md)
  Adds a label to the view that describes its contents.
- [func accessibility(value: Text) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](./accessibility%28value%29.md)
  Adds a textual description of the value that the view contains.
- [func accessibility(identifier: String) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](./accessibility%28identifier%29.md)
  Uses the specified string to identify the view.
- [func accessibility(selectionIdentifier: AnyHashable) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](./accessibility%28selectionidentifier%29.md)
  Sets a selection identifier for this view’s accessibility element.
- [func accessibility(hint: Text) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](./accessibility%28hint%29.md)
  Communicates to the user what happens after performing the view’s action.
- [func accessibility(activationPoint:)](./accessibility%28activationpoint%29.md)
  Specifies the point where activations occur in the view.
- [func accessibility(inputLabels: [Text]) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](./accessibility%28inputlabels%29.md)
  Sets alternate input labels with which users identify a view.
- [func accessibility(addTraits: AccessibilityTraits) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](./accessibility%28addtraits%29.md)
  Adds the given traits to the view.
- [func accessibility(removeTraits: AccessibilityTraits) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](./accessibility%28removetraits%29.md)
  Removes the given traits from this view.
- [func accessibility(sortPriority: Double) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](./accessibility%28sortpriority%29.md)
  Sets the sort priority order for this view’s accessibility element, relative to other elements at the same level.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/accessibility(hidden:))*