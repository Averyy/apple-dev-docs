# Accessibility fundamentals

**Framework**: SwiftUI

Make your SwiftUI apps accessible to everyone, including people with disabilities.

#### Overview

Like all Apple UI frameworks, SwiftUI comes with built-in accessibility support. The framework introspects common elements like navigation views, lists, text fields, sliders, buttons, and so on, and provides basic accessibility labels and values by default. You don’t have to do any extra work to enable these standard accessibility features.

![None](https://docs-assets.developer.apple.com/published/3e38dd74355b2499d9edb9d09f567c62/accessibility-fundamentals-hero%402x.png)

SwiftUI also provides tools to help you enhance the accessibility of your app. To find out what enhancements you need, try using your app with accessibility features like VoiceOver, Voice Control, and Switch Control, or get feedback from users of your app that regularly use these features. Then use the accessibility view modifiers that SwiftUI provides to improve the experience. For example, you can explicitly add accessibility labels to elements in your UI using the [`accessibilityLabel(_:)`](view/accessibilitylabel(_:).md) or the [`accessibilityValue(_:)`](view/accessibilityvalue(_:).md) view modifier.

Customize your use of accessibility modifiers for all the platforms that your app runs on. For example, you may need to adjust the accessibility elements for a companion Apple Watch app that shares a common code base with an iOS app. If you integrate AppKit or UIKit controls in SwiftUI, expose any accessibility labels and make them accessible from your [`NSViewRepresentable`](nsviewrepresentable.md) or [`UIViewRepresentable`](uiviewrepresentable.md) views, or provide custom accessibility information if the underlying accessibility labels aren’t available.

For design guidance, see [`Accessibility`](https://developer.apple.com/design/Human-Interface-Guidelines/accessibility) in the Human Interface Guidelines.

## Topics

### Essentials
- [Creating accessible views](creating-accessible-views.md)
  Make your app accessible to everyone by applying accessibility modifiers to your SwiftUI views.
### Creating accessible elements
- [func accessibilityElement(children: AccessibilityChildBehavior) -> some View](view/accessibilityelement(children:).md)
  Creates a new accessibility element, or modifies the [`AccessibilityChildBehavior`](accessibilitychildbehavior.md) of the existing accessibility element.
- [func accessibilityChildren<V>(children: () -> V) -> some View](view/accessibilitychildren(children:).md)
  Replaces the existing accessibility element’s children with one or more new synthetic accessibility elements.
- [func accessibilityRepresentation<V>(representation: () -> V) -> some View](view/accessibilityrepresentation(representation:).md)
  Replaces one or more accessibility elements for this view with new accessibility elements.
- [struct AccessibilityChildBehavior](accessibilitychildbehavior.md)
  Defines the behavior for the child elements of the new parent element.
### Identifying elements
- [func accessibilityIdentifier(String) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](view/accessibilityidentifier(_:).md)
  Uses the string you specify to identify the view.
- [func accessibilityIdentifier(String, isEnabled: Bool) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](view/accessibilityidentifier(_:isenabled:).md)
  Uses the string you specify to identify the view.
### Hiding elements
- [func accessibilityHidden(Bool) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](view/accessibilityhidden(_:).md)
  Specifies whether to hide this view from system accessibility features.
- [func accessibilityHidden(Bool, isEnabled: Bool) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](view/accessibilityhidden(_:isenabled:).md)
  Specifies whether to hide this view from system accessibility features.
### Supporting types
- [struct AccessibilityTechnologies](accessibilitytechnologies.md)
  Accessibility technologies available to the system.
- [struct AccessibilityAttachmentModifier](accessibilityattachmentmodifier.md)
  A view modifier that adds accessibility properties to the view

## See Also

- [Accessible appearance](accessible-appearance.md)
  Enhance the legibility of content in your app’s interface.
- [Accessible controls](accessible-controls.md)
  Improve access to actions that your app can undertake.
- [Accessible descriptions](accessible-descriptions.md)
  Describe interface elements to help people understand what they represent.
- [Accessible navigation](accessible-navigation.md)
  Enable users to navigate to specific user interface elements using rotors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/accessibility-fundamentals)*