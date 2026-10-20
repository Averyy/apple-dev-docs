# UIDictationPhrase

**Framework**: UIKit  
**Kind**: class  
**Role**: Class

An object that represents the textual interpretation of a spoken phrase that the user dictates.

**Availability**:
- iOS 5.1+
- iPadOS 5.1+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
@MainActor
class UIDictationPhrase
```

```objc
@interface UIDictationPhrase : NSObject
```

#### Overview

When the user chooses dictation input on a supported device, the system automatically inserts recognized phrases into the current text view. You can use an object of the [`UIDictationPhrase`](./uidictationphrase.md) class to obtain a string representing a phrase a user has dictated. In the case of ambiguous dictation results, a dictation phrase object provides an array containing alternative strings. Methods in the [`UITextInput`](./uitextinput.md) protocol allow your app to respond to the completion of dictation.

## Topics

### Obtaining textual interpretations of spoken text
- [var alternativeInterpretations: [String]?](./uidictationphrase/alternativeinterpretations.md)
  An array of alternative textual interpretations of a dictated phrase.
- [var text: String](./uidictationphrase/text.md)
  The most likely textual interpretation of a dictated phrase.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../Swift/sendable.md)

## See Also

### Text input
- [protocol UITextInput](./uitextinput.md)
  A set of methods for interacting with the text input system and enabling features in documents.
- [protocol UITextInputDelegate](./uitextinputdelegate.md)
  An intermediary between a document and the text input system.
- [protocol UIKeyInput](./uikeyinput.md)
  A set of methods a responder uses to implement simple text entry.
- [protocol UITextInputTraits](./uitextinputtraits.md)
  A set of methods that defines features for keyboard input to a text object.
- [class UITextInputContext](./uitextinputcontext.md)
  An object that reports the type of input your app receives.
- [class UITextInputMode](./uitextinputmode.md)
  The current text input mode.
- [class UITextInputAssistantItem](./uitextinputassistantitem.md)
  An object that manages custom bar button items that you add to the shortcuts bar above the keyboard on iPad.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidictationphrase)*