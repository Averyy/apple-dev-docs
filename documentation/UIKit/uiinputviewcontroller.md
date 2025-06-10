# UIInputViewController

**Framework**: UIKit  
**Kind**: class

The primary view controller for a custom keyboard app extension.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class UIInputViewController
```

## Mentions

- [Handling text interactions in custom keyboards](handling-text-interactions-in-custom-keyboards.md)
- [Configuring open access for a custom keyboard](configuring-open-access-for-a-custom-keyboard.md)

#### Overview

To create a custom keyboard, first subclass the [`UIInputViewController`](uiinputviewcontroller.md) class, then add your keyboard’s user interface to the [`inputView`](uiinputviewcontroller/inputview.md) property of your subclass. In Xcode, you can start a custom keyboard by choosing the Custom Keyboard target template.

A custom keyboard can respond to user input events in the following ways:

- Add text in the form of an unattributed [`NSString`](https://developer.apple.com/documentation/Foundation/NSString) object at the insertion point in the current text input object, by calling the [`insertText(_:)`](uikeyinput/inserttext(_:).md) method on the [`textDocumentProxy`](uiinputviewcontroller/textdocumentproxy.md) property. This property provides that method through its conformance to the [`UIKeyInput`](uikeyinput.md) protocol
- Delete text in a backward direction, starting at the insertion point, by calling the [`deleteBackward()`](uikeyinput/deletebackward().md) method on the [`textDocumentProxy`](uiinputviewcontroller/textdocumentproxy.md) property.
- Switch to another keyboard in the set of user-enabled keyboards, by calling the [`advanceToNextInputMode()`](uiinputviewcontroller/advancetonextinputmode().md) method.
- Dismiss the keyboard, by calling the [`dismissKeyboard()`](uiinputviewcontroller/dismisskeyboard().md) method.

Obtain textual context around the insertion point by reading the [`textDocumentProxy`](uiinputviewcontroller/textdocumentproxy.md) properties [`documentContextBeforeInput`](uitextdocumentproxy/documentcontextbeforeinput.md) and [`documentContextAfterInput`](uitextdocumentproxy/documentcontextafterinput.md). To find out if the current text input object is empty, call the [`hasText`](uikeyinput/hastext.md) method on the [`textDocumentProxy`](uiinputviewcontroller/textdocumentproxy.md) property. You can employ this textual context by considering it along with user input, to offer context-sensitive output to a document from your keyboard.

An input view controller conforms to the [`UITextInputDelegate`](uitextinputdelegate.md) protocol, allowing you to respond to changes in document content and position of the insertion point.

To present an appropriate keyboard layout, respond to the current text input object’s [`UIKeyboardType`](uikeyboardtype.md) property. For each keyboard type trait you support, change the contents of your primary view accordingly.

For more about creating a custom keyboard, read [`Custom Keyboard`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/General/Conceptual/ExtensibilityPG/CustomKeyboard.html#//apple_ref/doc/uid/TP40014214-CH16) in [`App Extension Programming Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/General/Conceptual/ExtensibilityPG/index.html#//apple_ref/doc/uid/TP40014214).

## Topics

### Providing a user interface for a custom keyboard
- [var inputView: UIInputView?](uiinputviewcontroller/inputview.md)
  The primary view for the input view controller.
### Controlling a custom keyboard
- [func advanceToNextInputMode()](uiinputviewcontroller/advancetonextinputmode.md)
  Switches to the next keyboard in the list of user-enabled keyboards.
- [func dismissKeyboard()](uiinputviewcontroller/dismisskeyboard.md)
  Dismisses the custom keyboard from the screen.
- [func handleInputModeList(from: UIView, with: UIEvent)](uiinputviewcontroller/handleinputmodelist(from:with:).md)
  Supports interaction with the list of user-enabled keyboards.
### Interacting with a text input object
- [var textDocumentProxy: any UITextDocumentProxy](uiinputviewcontroller/textdocumentproxy.md)
  A proxy to the text input object that the custom keyboard is interacting with.
- [protocol UITextDocumentProxy](uitextdocumentproxy.md)
  An object that provides textual context to a custom keyboard.
### Obtaining a supplementary lexicon
- [func requestSupplementaryLexicon(completion: (UILexicon) -> Void)](uiinputviewcontroller/requestsupplementarylexicon(completion:).md)
  Obtains a supplementary lexicon of term pairs in a custom keyboard.
### Changing the primary language of a custom keyboard
- [var primaryLanguage: String?](uiinputviewcontroller/primarylanguage.md)
  The primary language for a custom keyboard.
### Configuring the keyboard behaviors
- [var needsInputModeSwitchKey: Bool](uiinputviewcontroller/needsinputmodeswitchkey.md)
  A Boolean value that indicates whether the keyboard must display an input switcher key.
- [var hasFullAccess: Bool](uiinputviewcontroller/hasfullaccess.md)
  A Boolean value that indicates whether the keyboard has full access.
- [var hasDictationKey: Bool](uiinputviewcontroller/hasdictationkey.md)
  A Boolean value that indicates whether the keyboard has a dictation key.

## Relationships

### Inherits From
- [UIViewController](uiviewcontroller.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSExtensionRequestHandling](../Foundation/NSExtensionRequestHandling.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSTouchBarProvider](../AppKit/NSTouchBarProvider.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [UIActivityItemsConfigurationProviding](uiactivityitemsconfigurationproviding.md)
- [UIAppearanceContainer](uiappearancecontainer.md)
- [UIContentContainer](uicontentcontainer.md)
- [UIFocusEnvironment](uifocusenvironment.md)
- [UIPasteConfigurationSupporting](uipasteconfigurationsupporting.md)
- [UIResponderStandardEditActions](uiresponderstandardeditactions.md)
- [UIStateRestoring](uistaterestoring.md)
- [UITextInputDelegate](uitextinputdelegate.md)
- [UITraitChangeObservable](uitraitchangeobservable-67e94.md)
- [UITraitEnvironment](uitraitenvironment.md)
- [UIUserActivityRestoring](uiuseractivityrestoring.md)

## See Also

- [protocol UITextDocumentProxy](uitextdocumentproxy.md)
  An object that provides textual context to a custom keyboard.
- [protocol UIInputViewAudioFeedback](uiinputviewaudiofeedback.md)
  A property that enables a custom input or keyboard accessory view to play standard keyboard input clicks.
- [class UILexicon](uilexicon.md)
  A read-only array of term pairs, each in a lexicon entry object, for a custom keyboard.
- [class UILexiconEntry](uilexiconentry.md)
  A read-only term pair, available within a lexicon object, for a custom keyboard.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiinputviewcontroller)*