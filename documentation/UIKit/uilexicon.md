# UILexicon

**Framework**: UIKit  
**Kind**: class

A read-only array of term pairs, each in a lexicon entry object, for a custom keyboard.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class UILexicon
```

## Mentions

- [Configuring a custom keyboard interface](configuring-a-custom-keyboard-interface.md)

#### Overview

To obtain the lexicon, call the [`requestSupplementaryLexicon(completion:)`](uiinputviewcontroller/requestsupplementarylexicon(completion:).md) method of the [`UIInputViewController`](uiinputviewcontroller.md) class. This method can be called only from a custom keyboard app extension. A lexicon contains words from various sources, including:

- Unpaired first names and last names from the user’s Address Book database
- Text shortcuts defined in the Settings > General > Keyboard > Shortcuts list
- A common words dictionary

Apple intends for you to consider the words in a lexicon object as supplementary to an autocorrection/suggestion lexicon of your own design. For information on custom keyboards, see [`Custom Keyboard`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/General/Conceptual/ExtensibilityPG/CustomKeyboard.html#//apple_ref/doc/uid/TP40014214-CH16) in [`App Extension Programming Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/General/Conceptual/ExtensibilityPG/index.html#//apple_ref/doc/uid/TP40014214).

## Topics

### Accessing the lexicon
- [var entries: [UILexiconEntry]](uilexicon/entries.md)
  A read-only array of term pairs for use by a custom keyboard.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [protocol UITextDocumentProxy](uitextdocumentproxy.md)
  An object that provides textual context to a custom keyboard.
- [protocol UIInputViewAudioFeedback](uiinputviewaudiofeedback.md)
  A property that enables a custom input or keyboard accessory view to play standard keyboard input clicks.
- [class UIInputViewController](uiinputviewcontroller.md)
  The primary view controller for a custom keyboard app extension.
- [class UILexiconEntry](uilexiconentry.md)
  A read-only term pair, available within a lexicon object, for a custom keyboard.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uilexicon)*