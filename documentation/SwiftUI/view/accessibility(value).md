# accessibility(value:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Adds a textual description of the value that the view contains.

**Availability**:
- iOS 13.0+ - Deprecated in 27.2 (renamed: accessibilityValue(_:))
- iPadOS 13.0+ - Deprecated in 27.2 (renamed: accessibilityValue(_:))
- Mac Catalyst 13.0+ - Deprecated in 27.2 (renamed: accessibilityValue(_:))
- macOS 10.15+ - Deprecated in 27.2 (renamed: accessibilityValue(_:))
- tvOS 13.0+ - Deprecated in 27.2 (renamed: accessibilityValue(_:))
- visionOS 1.0+ - Deprecated in 27.2 (renamed: accessibilityValue(_:))
- watchOS 6.0+ - Deprecated in 27.2 (renamed: accessibilityValue(_:))

> **Deprecated**: Use [`accessibilityValue(_:)`](./accessibilityvalue%28_%29-z9mo.md) instead.

## Declaration

```swift
nonisolated
func accessibility(value: Text) -> ModifiedContent<Self, AccessibilityAttachmentModifier>
```

## Discussion

Use this method to describe the value represented by a view, but only if that’s different than the view’s label. For example, for a slider that you label as “Volume” using [`accessibility(label:)`](./accessibility%28label%29.md), you can provide the current volume setting, like “60%”, using [`accessibility(value:)`](./accessibility%28value%29.md).

## See Also

### Accessibility modifiers
- [func accessibility(label: Text) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](./accessibility%28label%29.md)
  Adds a label to the view that describes its contents.
- [func accessibility(hidden: Bool) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](./accessibility%28hidden%29.md)
  Specifies whether to hide this view from system accessibility features.
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

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/accessibility(value:))*