# UIKeyInput

**Framework**: UIKit  
**Kind**: protocol

A set of methods a responder uses to implement simple text entry.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
@MainActor
protocol UIKeyInput : UITextInputTraits
```

## Mentions

- [Handling text interactions in custom keyboards](handling-text-interactions-in-custom-keyboards.md)

#### Overview

Adopt this protocol in a subclass of [`UIResponder`](uiresponder.md) to support text entry. When instances of this subclass are the first responder, the system keyboard displays. Only a small subset of the available keyboards and languages are available to classes that adopt this protocol.

## Topics

### Inserting and deleting text
- [func insertText(String)](uikeyinput/inserttext(_:).md)
  Inserts a character into the displayed text.
- [func deleteBackward()](uikeyinput/deletebackward.md)
  Deletes a character from the displayed text.
- [var hasText: Bool](uikeyinput/hastext.md)
  A Boolean value that indicates whether the text-entry object has any text.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [UITextInputTraits](uitextinputtraits.md)
### Inherited By
- [UITextDocumentProxy](uitextdocumentproxy.md)
- [UITextDraggable](uitextdraggable.md)
- [UITextDroppable](uitextdroppable.md)
- [UITextInput](uitextinput.md)
### Conforming Types
- [UISearchTextField](uisearchtextfield.md)
- [UITextField](uitextfield.md)
- [UITextView](uitextview.md)

## See Also

- [protocol UITextInput](uitextinput.md)
  A set of methods for interacting with the text input system and enabling features in documents.
- [protocol UITextInputDelegate](uitextinputdelegate.md)
  An intermediary between a document and the text input system.
- [protocol UITextInputTraits](uitextinputtraits.md)
  A set of methods that defines features for keyboard input to a text object.
- [class UITextInputContext](uitextinputcontext.md)
  An object that reports the type of input your app receives.
- [class UITextInputMode](uitextinputmode.md)
  The current text input mode.
- [class UITextInputAssistantItem](uitextinputassistantitem.md)
  An object that manages custom bar button items that you add to the shortcuts bar above the keyboard on iPad.
- [class UIDictationPhrase](uidictationphrase.md)
  An object that represents the textual interpretation of a spoken phrase that the user dictates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uikeyinput)*