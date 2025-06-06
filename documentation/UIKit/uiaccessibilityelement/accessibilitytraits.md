# accessibilityTraits

**Framework**: UIKit  
**Kind**: property

The combination of traits that best characterize the accessibility element.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var accessibilityTraits: UIAccessibilityTraits { get set }
```

#### Discussion

A trait describes a single aspect of an element’s behavior, state, or usage. Several traits are combined in this property (using an OR operation) to give a complete picture of the element to an assistive application. See “Accessibility Traits” in [`UIAccessibility`](uiaccessibility-protocol.md) for a complete list of traits.

UIKit provides an appropriate combination of traits for all standard controls and views. When combining traits for a custom accessibility element, be sure to:

- Use common sense. Don’t combine traits that characterize the element in mutually exclusive ways, such as combining the button and search-field traits.
- Combine the traits you select with the superclass’s traits. Specifically, always combine your custom traits with `[super accessibilityTraits]` in the method you use to set a custom element’s traits.

## See Also

- [var accessibilityLabel: String?](uiaccessibilityelement/accessibilitylabel.md)
  A string that succinctly identifies the accessibility element.
- [var accessibilityHint: String?](uiaccessibilityelement/accessibilityhint.md)
  A string that briefly describes the result of performing an action on the accessibility element.
- [var accessibilityValue: String?](uiaccessibilityelement/accessibilityvalue.md)
  A string that represents the current value of the accessibility element.
- [var accessibilityFrame: CGRect](uiaccessibilityelement/accessibilityframe.md)
  The frame of the accessibility element, in screen coordinates.
- [var accessibilityFrameInContainerSpace: CGRect](uiaccessibilityelement/accessibilityframeincontainerspace.md)
  The frame of the accessibility element, in the coordinate space of its container view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiaccessibilityelement/accessibilitytraits)*