# AccessibilityTraits

**Framework**: SwiftUI  
**Kind**: struct

A set of accessibility traits that describe how an element behaves.

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
struct AccessibilityTraits
```

## Topics

### Getting traits
- [static let allowsDirectInteraction: AccessibilityTraits](accessibilitytraits/allowsdirectinteraction.md)
  The accessibility element allows direct touch interaction for VoiceOver users.
- [static let causesPageTurn: AccessibilityTraits](accessibilitytraits/causespageturn.md)
  The accessibility element causes an automatic page turn when VoiceOver finishes reading the text within it.
- [static let isButton: AccessibilityTraits](accessibilitytraits/isbutton.md)
  The accessibility element is a button.
- [static let isHeader: AccessibilityTraits](accessibilitytraits/isheader.md)
  The accessibility element is a header that divides content into sections, like the title of a navigation bar.
- [static let isImage: AccessibilityTraits](accessibilitytraits/isimage.md)
  The accessibility element is an image.
- [static let isKeyboardKey: AccessibilityTraits](accessibilitytraits/iskeyboardkey.md)
  The accessibility element behaves as a keyboard key.
- [static let isLink: AccessibilityTraits](accessibilitytraits/islink.md)
  The accessibility element is a link.
- [static let isModal: AccessibilityTraits](accessibilitytraits/ismodal.md)
  The accessibility element is modal.
- [static let isSearchField: AccessibilityTraits](accessibilitytraits/issearchfield.md)
  The accessibility element is a search field.
- [static let isSelected: AccessibilityTraits](accessibilitytraits/isselected.md)
  The accessibility element is currently selected.
- [static let isStaticText: AccessibilityTraits](accessibilitytraits/isstatictext.md)
  The accessibility element is a static text that cannot be modified by the user.
- [static let isSummaryElement: AccessibilityTraits](accessibilitytraits/issummaryelement.md)
  The accessibility element provides summary information when the application starts.
- [static let isToggle: AccessibilityTraits](accessibilitytraits/istoggle.md)
  The accessibility element is a toggle.
- [static let playsSound: AccessibilityTraits](accessibilitytraits/playssound.md)
  The accessibility element plays its own sound when activated.
- [static let startsMediaSession: AccessibilityTraits](accessibilitytraits/startsmediasession.md)
  The accessibility element starts a media session when it is activated.
- [static let updatesFrequently: AccessibilityTraits](accessibilitytraits/updatesfrequently.md)
  The accessibility element frequently updates its label or value.
### Type Properties
- [static let isTabBar: AccessibilityTraits](accessibilitytraits/istabbar.md)
  The accessibility element is a tab bar

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [Sendable](../Swift/Sendable.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [func accessibilityAddTraits(AccessibilityTraits) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](view/accessibilityaddtraits(_:).md)
  Adds the given traits to the view.
- [func accessibilityRemoveTraits(AccessibilityTraits) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](view/accessibilityremovetraits(_:).md)
  Removes the given traits from this view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/accessibilitytraits)*