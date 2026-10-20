# accessibility(selectionIdentifier:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Sets a selection identifier for this view’s accessibility element.

**Availability**:
- iOS 13.0+ - Deprecated
- iPadOS 13.0+ - Deprecated
- Mac Catalyst 13.0+ - Deprecated
- macOS 10.15+ - Deprecated
- tvOS 13.0+ - Deprecated
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 6.0+ - Deprecated

> **Deprecated**: This functionality is no longer available.

## Declaration

```swift
nonisolated
func accessibility(selectionIdentifier: AnyHashable) -> ModifiedContent<Self, AccessibilityAttachmentModifier>
```

#### Discussion

Picker uses the value to determine what node to use for the accessibility value.

## See Also

### Accessibility modifiers
- [func accessibility(label: Text) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](./accessibility%28label%29.md)
  Adds a label to the view that describes its contents.
- [func accessibility(value: Text) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](./accessibility%28value%29.md)
  Adds a textual description of the value that the view contains.
- [func accessibility(hidden: Bool) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](./accessibility%28hidden%29.md)
  Specifies whether to hide this view from system accessibility features.
- [func accessibility(identifier: String) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](./accessibility%28identifier%29.md)
  Uses the specified string to identify the view.
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

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/accessibility(selectionidentifier:))*