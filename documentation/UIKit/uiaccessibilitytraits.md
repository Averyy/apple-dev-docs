# UIAccessibilityTraits

**Framework**: UIKit  
**Kind**: struct  
**Role**: Structure

Constants that describe how an accessibility element behaves.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- tvOS
- visionOS
- watchOS 2.0+

## Declaration

```swift
struct UIAccessibilityTraits
```

```c
typedef uint64_t UIAccessibilityTraits;
```

#### Overview

Set these traits to tell an assistive app how an accessibility element behaves or how to treat it.

## Topics

### Constants
- [static let none: UIAccessibilityTraits](./uiaccessibilitytraits/none.md)
  The accessibility element has no traits.
- [static let button: UIAccessibilityTraits](./uiaccessibilitytraits/button.md)
  The accessibility element behaves like a button.
- [static let link: UIAccessibilityTraits](./uiaccessibilitytraits/link.md)
  The accessibility element behaves like a link.
- [static let image: UIAccessibilityTraits](./uiaccessibilitytraits/image.md)
  The accessibility element behaves like an image.
- [static let searchField: UIAccessibilityTraits](./uiaccessibilitytraits/searchfield.md)
  The accessibility element behaves like a search field.
- [static let toggleButton: UIAccessibilityTraits](./uiaccessibilitytraits/togglebutton.md)
  The accessibility element behaves like a toggle button.
- [static let keyboardKey: UIAccessibilityTraits](./uiaccessibilitytraits/keyboardkey.md)
  The accessibility element behaves like a keyboard key.
- [static let staticText: UIAccessibilityTraits](./uiaccessibilitytraits/statictext.md)
  The accessibility element behaves like static text that can’t change.
- [static let header: UIAccessibilityTraits](./uiaccessibilitytraits/header.md)
  The accessibility element is a header that divides content into sections, such as the title of a navigation bar.
- [static let tabBar: UIAccessibilityTraits](./uiaccessibilitytraits/tabbar.md)
  The accessibility element behaves like a tab bar.
- [static let summaryElement: UIAccessibilityTraits](./uiaccessibilitytraits/summaryelement.md)
  The accessibility element provides summary information when the app starts.
- [static let selected: UIAccessibilityTraits](./uiaccessibilitytraits/selected.md)
  The accessibility element is currently in a selected state.
- [static let notEnabled: UIAccessibilityTraits](./uiaccessibilitytraits/notenabled.md)
  The accessibility element isn’t in an enabled state and doesn’t respond to user interaction.
- [static let adjustable: UIAccessibilityTraits](./uiaccessibilitytraits/adjustable.md)
  The accessibility element allows continuous adjustment through a range of values.
- [static let allowsDirectInteraction: UIAccessibilityTraits](./uiaccessibilitytraits/allowsdirectinteraction.md)
  The accessibility element allows direct touch interaction for VoiceOver users.
- [static let updatesFrequently: UIAccessibilityTraits](./uiaccessibilitytraits/updatesfrequently.md)
  The accessibility element frequently updates its label or value.
- [static let causesPageTurn: UIAccessibilityTraits](./uiaccessibilitytraits/causespageturn.md)
  The accessibility element causes an automatic page turn when VoiceOver finishes reading the text within it.
- [static let playsSound: UIAccessibilityTraits](./uiaccessibilitytraits/playssound.md)
  The accessibility element plays its own sound when the user activates it.
- [static let startsMediaSession: UIAccessibilityTraits](./uiaccessibilitytraits/startsmediasession.md)
  The accessibility element starts a media session when the user activates it.
- [static let supportsZoom: UIAccessibilityTraits](./uiaccessibilitytraits/supportszoom.md)
  The accessibility element supports zooming in and out on its content.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Copyable](../Swift/copyable.md)
- [Equatable](../Swift/equatable.md)
- [Escapable](../Swift/escapable.md)
- [ExpressibleByArrayLiteral](../Swift/expressiblebyarrayliteral.md)
- [Hashable](../Swift/hashable.md)
- [OptionSet](../Swift/optionset.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [SetAlgebra](../Swift/setalgebra.md)

## See Also

### Supporting basic accessibility
- [var isAccessibilityElement: Bool](../ObjectiveC/nsobject-swift.class/isaccessibilityelement.md)
- [var accessibilityLabel: String?](../ObjectiveC/nsobject-swift.class/accessibilitylabel.md)
- [var accessibilityValue: String?](../ObjectiveC/nsobject-swift.class/accessibilityvalue.md)
- [var accessibilityHint: String?](../ObjectiveC/nsobject-swift.class/accessibilityhint.md)
- [var accessibilityTraits: UIAccessibilityTraits](../ObjectiveC/nsobject-swift.class/accessibilitytraits.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiaccessibilitytraits)*