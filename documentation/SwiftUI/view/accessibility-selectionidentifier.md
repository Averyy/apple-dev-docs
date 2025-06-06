# accessibility(selectionIdentifier:)

**Framework**: SwiftUI  
**Kind**: method

Sets a selection identifier for this view’s accessibility element.

**Availability**:
- iOS 13.0+ - Deprecated
- iPadOS 13.0+ - Deprecated
- Mac Catalyst 13.0+ - Deprecated
- macOS 10.15+ - Deprecated
- tvOS 13.0+ - Deprecated
- visionOS 1.0+
- watchOS 6.0+ - Deprecated

## Declaration

```swift
nonisolated
func accessibility(selectionIdentifier: AnyHashable) -> ModifiedContent<Self, AccessibilityAttachmentModifier>
```

#### Discussion

Picker uses the value to determine what node to use for the accessibility value.

## See Also

- [func accessibility(label: Text) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](view/accessibility(label:).md)
  Adds a label to the view that describes its contents.
- [func accessibility(value: Text) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](view/accessibility(value:).md)
  Adds a textual description of the value that the view contains.
- [func accessibility(hidden: Bool) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](view/accessibility(hidden:).md)
  Specifies whether to hide this view from system accessibility features.
- [func accessibility(identifier: String) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](view/accessibility(identifier:).md)
  Uses the specified string to identify the view.
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
- [func accessibility(sortPriority: Double) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](view/accessibility(sortpriority:).md)
  Sets the sort priority order for this view’s accessibility element, relative to other elements at the same level.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/accessibility(selectionidentifier:))*