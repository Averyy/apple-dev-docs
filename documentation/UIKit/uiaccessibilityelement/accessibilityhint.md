# accessibilityHint

**Framework**: UIKit  
**Kind**: property

A string that briefly describes the result of performing an action on the accessibility element.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var accessibilityHint: String? { get set }
```

## Mentions

- [Supporting VoiceOver in your app](supporting-voiceover-in-your-app.md)

#### Discussion

The hint is a brief, localized description of the result of performing an action on the element without identifying the element or the action. For example, the hint for a table row that contains an email message might be “Selects the message,” but not “Tap this row to select the message.”

By default, standard UIKit controls and views have system-provided hints. If you provide a custom control or view, however, you need to set this property appropriately so that assistive applications can supply accurate information to users with disabilities.

## See Also

- [var accessibilityLabel: String?](uiaccessibilityelement/accessibilitylabel.md)
  A string that succinctly identifies the accessibility element.
- [var accessibilityValue: String?](uiaccessibilityelement/accessibilityvalue.md)
  A string that represents the current value of the accessibility element.
- [var accessibilityFrame: CGRect](uiaccessibilityelement/accessibilityframe.md)
  The frame of the accessibility element, in screen coordinates.
- [var accessibilityFrameInContainerSpace: CGRect](uiaccessibilityelement/accessibilityframeincontainerspace.md)
  The frame of the accessibility element, in the coordinate space of its container view.
- [var accessibilityTraits: UIAccessibilityTraits](uiaccessibilityelement/accessibilitytraits.md)
  The combination of traits that best characterize the accessibility element.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiaccessibilityelement/accessibilityhint)*