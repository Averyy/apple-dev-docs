# startsMediaSession

**Framework**: UIKit  
**Kind**: property  
**Role**: Type Property

The accessibility element starts a media session when the user activates it.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
nonisolated
static let startsMediaSession: UIAccessibilityTraits
```

```c
extern const UIAccessibilityTraits UIAccessibilityTraitStartsMediaSession;
```

#### Discussion

Use this trait to silence the audio output of an assistive app, such as VoiceOver, during a media session that you don’t want to interrupt. For example, you might use this trait to silence VoiceOver speech while the user is recording audio.

## See Also

### Constants
- [static let none: UIAccessibilityTraits](./none.md)
  The accessibility element has no traits.
- [static let button: UIAccessibilityTraits](./button.md)
  The accessibility element behaves like a button.
- [static let link: UIAccessibilityTraits](./link.md)
  The accessibility element behaves like a link.
- [static let image: UIAccessibilityTraits](./image.md)
  The accessibility element behaves like an image.
- [static let searchField: UIAccessibilityTraits](./searchfield.md)
  The accessibility element behaves like a search field.
- [static let toggleButton: UIAccessibilityTraits](./togglebutton.md)
  The accessibility element behaves like a toggle button.
- [static let keyboardKey: UIAccessibilityTraits](./keyboardkey.md)
  The accessibility element behaves like a keyboard key.
- [static let staticText: UIAccessibilityTraits](./statictext.md)
  The accessibility element behaves like static text that can’t change.
- [static let header: UIAccessibilityTraits](./header.md)
  The accessibility element is a header that divides content into sections, such as the title of a navigation bar.
- [static let tabBar: UIAccessibilityTraits](./tabbar.md)
  The accessibility element behaves like a tab bar.
- [static let summaryElement: UIAccessibilityTraits](./summaryelement.md)
  The accessibility element provides summary information when the app starts.
- [static let selected: UIAccessibilityTraits](./selected.md)
  The accessibility element is currently in a selected state.
- [static let notEnabled: UIAccessibilityTraits](./notenabled.md)
  The accessibility element isn’t in an enabled state and doesn’t respond to user interaction.
- [static let adjustable: UIAccessibilityTraits](./adjustable.md)
  The accessibility element allows continuous adjustment through a range of values.
- [static let allowsDirectInteraction: UIAccessibilityTraits](./allowsdirectinteraction.md)
  The accessibility element allows direct touch interaction for VoiceOver users.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiaccessibilitytraits/startsmediasession)*