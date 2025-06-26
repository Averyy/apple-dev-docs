# accessibilityElement(children:)

**Framework**: FamilyControls  
**Kind**: method

Creates a new accessibility element, or modifies the `AccessibilityChildBehavior` of the existing accessibility element.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- macOS 10.15+
- tvOS 13.0+
- watchOS 6.0+

## Declaration

```swift
nonisolated
func accessibilityElement(children: AccessibilityChildBehavior = .ignore) -> some View
```

#### Discussion

See also:

- `AccessibilityChildBehavior/ignore`
- `AccessibilityChildBehavior/combine`
- `AccessibilityChildBehavior/contain`

## Parameters

- `children`: The behavior to use when creating or   transforming an accessibility element.   The default is 

## See Also

- [func accessibilityChildren<V>(children: () -> V) -> some View](familyactivitypicker/accessibilitychildren(children:).md)
  Replaces the existing accessibility element’s children with one or more new synthetic accessibility elements.
- [func accessibilityHidden(Bool) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](familyactivitypicker/accessibilityhidden(_:).md)
  Specifies whether to hide this view from system accessibility features.


---

*[View on Apple Developer](https://developer.apple.com/documentation/familycontrols/familyactivitypicker/accessibilityelement(children:))*