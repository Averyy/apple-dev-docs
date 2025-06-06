# UIInputViewAudioFeedback

**Framework**: UIKit  
**Kind**: protocol

A property that enables a custom input or keyboard accessory view to play standard keyboard input clicks.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
@MainActor
protocol UIInputViewAudioFeedback : NSObjectProtocol
```

#### Overview

Implement this protocol in your custom subclass of [`UIView`](uiview.md) that you associate with your custom input nib file. For more information, see [`Text Programming Guide for iOS`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/StringsTextFonts/Conceptual/TextAndWebiPhoneOS/Introduction/Introduction.html#//apple_ref/doc/uid/TP40009542).

Implementation of this protocol is optional but expected.

## Topics

### Enabling input clicks
- [var enableInputClicksWhenVisible: Bool](uiinputviewaudiofeedback/enableinputclickswhenvisible.md)
  Specifies whether or not an input view enables input clicks.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [protocol UITextDocumentProxy](uitextdocumentproxy.md)
  An object that provides textual context to a custom keyboard.
- [class UIInputViewController](uiinputviewcontroller.md)
  The primary view controller for a custom keyboard app extension.
- [class UILexicon](uilexicon.md)
  A read-only array of term pairs, each in a lexicon entry object, for a custom keyboard.
- [class UILexiconEntry](uilexiconentry.md)
  A read-only term pair, available within a lexicon object, for a custom keyboard.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiinputviewaudiofeedback)*