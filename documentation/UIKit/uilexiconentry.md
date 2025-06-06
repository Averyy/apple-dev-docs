# UILexiconEntry

**Framework**: UIKit  
**Kind**: class

A read-only term pair, available within a lexicon object, for a custom keyboard.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class UILexiconEntry
```

#### Overview

You can employ a lexicon entry by matching user input against the entry’s [`userInput`](uilexiconentry/userinput.md) value, and then inserting into the current text input object the corresponding [`documentText`](uilexiconentry/documenttext.md) value. For example, if the user typed the string “iphone”, the lexicon entry with that exact, case-sensitive string in the [`userInput`](uilexiconentry/userinput.md) property has the string “iPhone” in the corresponding [`documentText`](uilexiconentry/documenttext.md) property.

In some cases, the [`documentText`](uilexiconentry/documenttext.md) string is in a different text script than the [`userInput`](uilexiconentry/userinput.md) string.

For information on custom keyboards, which are based on the [`UIInputViewController`](uiinputviewcontroller.md) class, see [`Creating a custom keyboard`](creating-a-custom-keyboard.md).

## Topics

### Accessing a lexicon entry
- [var documentText: String](uilexiconentry/documenttext.md)
  Text to be inserted into a text input object by a custom keyboard, corresponding to the user input value in the same lexicon entry.
- [var userInput: String](uilexiconentry/userinput.md)
  Text to match, during user input, to provide appropriate output to a text document from the document text value in the same lexicon entry.

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
- [class UILexicon](uilexicon.md)
  A read-only array of term pairs, each in a lexicon entry object, for a custom keyboard.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uilexiconentry)*