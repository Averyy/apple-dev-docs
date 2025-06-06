# accessibilityHidden(_:)

**Framework**: FamilyControls  
**Kind**: method

Specifies whether to hide this view from system accessibility features.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- watchOS 7.0+

## Declaration

```swift
nonisolated
func accessibilityHidden(_ hidden: Bool) -> ModifiedContent<Self, AccessibilityAttachmentModifier>
```

## See Also

- [func accessibilityElement(children: AccessibilityChildBehavior) -> some View](familyactivitypicker/accessibilityelement(children:).md)
  Creates a new accessibility element, or modifies the `AccessibilityChildBehavior` of the existing accessibility element.
- [func accessibilityChildren<V>(children: () -> V) -> some View](familyactivitypicker/accessibilitychildren(children:).md)
  Replaces the existing accessibility element’s children with one or more new synthetic accessibility elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/familycontrols/familyactivitypicker/accessibilityhidden(_:))*