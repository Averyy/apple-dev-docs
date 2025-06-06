# Accessible navigation

**Framework**: SwiftUI

Enable users to navigate to specific user interface elements using rotors.

#### Overview

An accessibility rotor is a shortcut that enables users to quickly navigate to specific elements of the user interface, and, optionally, to specific ranges of text within those elements.

![None](https://docs-assets.developer.apple.com/published/5ceef0267b3475033df3fcff2a12dd25/accessible-navigation-hero%402x.png)

The system automatically provides rotors for many navigable elements, but you can supply additional rotors for specific purposes, or replace system rotors when they don’t automatically pick up off-screen elements, like those far down in a [`LazyVStack`](lazyvstack.md) or a [`List`](list.md).

For design guidance, see [`Accessibility`](https://developer.apple.com/design/Human-Interface-Guidelines/accessibility) in the Accessibility section of the Human Interface Guidelines.

## Topics

### Working with rotors
- [func accessibilityRotor(_:entries:)](view/accessibilityrotor(_:entries:).md)
  Create an Accessibility Rotor with the specified user-visible label, and entries generated from the content closure.
- [func accessibilityRotor(_:entries:entryID:entryLabel:)](view/accessibilityrotor(_:entries:entryid:entrylabel:).md)
  Create an Accessibility Rotor with the specified user-visible label and entries.
- [func accessibilityRotor(_:entries:entryLabel:)](view/accessibilityrotor(_:entries:entrylabel:).md)
  Create an Accessibility Rotor with the specified user-visible label and entries.
- [func accessibilityRotor(_:textRanges:)](view/accessibilityrotor(_:textranges:).md)
  Create an Accessibility Rotor with the specified user-visible label and entries for each of the specified ranges. The Rotor will be attached to the current Accessibility element, and each entry will go the specified range of that element.
### Creating rotors
- [protocol AccessibilityRotorContent](accessibilityrotorcontent.md)
  Content within an accessibility rotor.
- [struct AccessibilityRotorContentBuilder](accessibilityrotorcontentbuilder.md)
  Result builder you use to generate rotor entry content.
- [struct AccessibilityRotorEntry](accessibilityrotorentry.md)
  A struct representing an entry in an Accessibility Rotor.
### Replacing system rotors
- [struct AccessibilitySystemRotor](accessibilitysystemrotor.md)
  Designates a Rotor that replaces one of the automatic, system-provided Rotors with a developer-provided Rotor.
### Configuring rotors
- [func accessibilityRotorEntry<ID>(id: ID, in: Namespace.ID) -> some View](view/accessibilityrotorentry(id:in:).md)
  Defines an explicit identifier tying an Accessibility element for this view to an entry in an Accessibility Rotor.
- [func accessibilityLinkedGroup<ID>(id: ID, in: Namespace.ID) -> some View](view/accessibilitylinkedgroup(id:in:).md)
  Links multiple accessibility elements so that the user can quickly navigate from one element to another, even when the elements are not near each other in the accessibility hierarchy.
- [func accessibilitySortPriority(Double) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](view/accessibilitysortpriority(_:).md)
  Sets the sort priority order for this view’s accessibility element, relative to other elements at the same level.

## See Also

- [Accessibility fundamentals](accessibility-fundamentals.md)
  Make your SwiftUI apps accessible to everyone, including people with disabilities.
- [Accessible appearance](accessible-appearance.md)
  Enhance the legibility of content in your app’s interface.
- [Accessible controls](accessible-controls.md)
  Improve access to actions that your app can undertake.
- [Accessible descriptions](accessible-descriptions.md)
  Describe interface elements to help people understand what they represent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/accessible-navigation)*