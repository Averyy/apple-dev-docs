# accessibility(sortPriority:)

**Framework**: SwiftUI  
**Kind**: method

Sets the sort priority order for this view’s accessibility element, relative to other elements at the same level.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
nonisolated
func accessibility(sortPriority: Double) -> ModifiedContent<Self, AccessibilityAttachmentModifier>
```

#### Discussion

Higher numbers are sorted first. The default sort priority is zero.

## See Also

- [func accessibility(label: Text) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](view/accessibility(label:).md)
  Adds a label to the view that describes its contents.
- [func accessibility(value: Text) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](view/accessibility(value:).md)
  Adds a textual description of the value that the view contains.
- [func accessibility(hidden: Bool) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](view/accessibility(hidden:).md)
  Specifies whether to hide this view from system accessibility features.
- [func accessibility(identifier: String) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](view/accessibility(identifier:).md)
  Uses the specified string to identify the view.
- [func accessibility(selectionIdentifier: AnyHashable) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](view/accessibility(selectionidentifier:).md)
  Sets a selection identifier for this view’s accessibility element.
- [func accessibility(hint: Text) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](view/accessibility(hint:).md)
  Communicates to the user what happens after performing the view’s action.
- [func accessibility(activationPoint:)](view/accessibility(activationpoint:).md)
  Specifies the point where activations occur in the view.
- [func accessibility(inputLabels: [Text]) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](view/accessibility(inputlabels:).md)
  Sets alternate input labels with which users identify a view.
- [func accessibility(addTraits: AccessibilityTraits) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](view/accessibility(addtraits:).md)
  Adds the given traits to the view.
- [func accessibility(removeTraits: AccessibilityTraits) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](view/accessibility(removetraits:).md)
  Removes the given traits from this view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/accessibility(sortpriority:))*