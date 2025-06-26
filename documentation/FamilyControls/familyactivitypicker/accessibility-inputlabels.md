# accessibility(inputLabels:)

**Framework**: FamilyControls  
**Kind**: method

Sets alternate input labels with which users identify a view.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
nonisolated
func accessibility(inputLabels: [Text]) -> ModifiedContent<Self, AccessibilityAttachmentModifier>
```

#### Discussion

Provide labels in descending order of importance. Voice Control and Full Keyboard Access use the input labels.

> **Note**: If you don’t specify any input labels, the user can still refer to the view using the accessibility label that you add with the [`accessibility(label:)`](familyactivitypicker/accessibility(label:).md) modifier.

## Parameters

- `inputLabels`: An array of Text elements to use as input labels.

## See Also

- [func accessibility(label: Text) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](familyactivitypicker/accessibility(label:).md)
  Adds a label to the view that describes its contents.
- [func accessibility(value: Text) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](familyactivitypicker/accessibility(value:).md)
  Adds a textual description of the value that the view contains.
- [func accessibility(hidden: Bool) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](familyactivitypicker/accessibility(hidden:).md)
  Specifies whether to hide this view from system accessibility features.
- [func accessibility(identifier: String) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](familyactivitypicker/accessibility(identifier:).md)
  Uses the specified string to identify the view.
- [func accessibility(selectionIdentifier: AnyHashable) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](familyactivitypicker/accessibility(selectionidentifier:).md)
  Sets a selection identifier for this view’s accessibility element.
- [func accessibility(hint: Text) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](familyactivitypicker/accessibility(hint:).md)
  Communicates to the user what happens after performing the view’s action.
- [func accessibility(activationPoint: CGPoint) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](familyactivitypicker/accessibility(activationpoint:)-34miz.md)
  Specifies the point where activations occur in the view.
- [func accessibility(activationPoint: UnitPoint) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](familyactivitypicker/accessibility(activationpoint:)-ci2b.md)
  Specifies the unit point where activations occur in the view.
- [func accessibility(addTraits: AccessibilityTraits) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](familyactivitypicker/accessibility(addtraits:).md)
  Adds the given traits to the view.
- [func accessibility(removeTraits: AccessibilityTraits) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](familyactivitypicker/accessibility(removetraits:).md)
  Removes the given traits from this view.
- [func accessibility(sortPriority: Double) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](familyactivitypicker/accessibility(sortpriority:).md)
  Sets the sort priority order for this view’s accessibility element, relative to other elements at the same level.
- [func accessibilityCustomContent<L, V>(L, V, importance: AXCustomContent.Importance) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](familyactivitypicker/accessibilitycustomcontent(_:_:importance:)-8480d.md)
  Add additional accessibility information to the view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/familycontrols/familyactivitypicker/accessibility(inputlabels:))*