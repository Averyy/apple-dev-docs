# Keyboards and input

**Framework**: UIKit

Configure the system keyboard, create your own keyboards to handle input, or detect key presses on a physical keyboard.

## Topics

### Text input
- [protocol UITextInput](uitextinput.md)
  A set of methods for interacting with the text input system and enabling features in documents.
- [protocol UITextInputDelegate](uitextinputdelegate.md)
  An intermediary between a document and the text input system.
- [protocol UIKeyInput](uikeyinput.md)
  A set of methods a responder uses to implement simple text entry.
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
### Text interactions
- [class UITextInteraction](uitextinteraction.md)
  An interaction that provides text selection gestures and UI to custom text views.
- [protocol UITextInteractionDelegate](uitextinteractiondelegate.md)
  An interface that an object implements to receive information about text interaction events.
- [enum UITextInteractionMode](uitextinteractionmode.md)
  Modes that determine the selection behaviors that a text interaction provides.
### Custom text selection
- [Adopting system selection UI in custom text views](adopting-system-selection-ui-in-custom-text-views.md)
  Incorporate the system text-selection experience into your custom text UI in UIKit.
- [class UITextSelectionDisplayInteraction](uitextselectiondisplayinteraction.md)
  An object that provides the system UI for displaying text selection.
- [protocol UITextSelectionHighlightView](uitextselectionhighlightview.md)
  An interface you use to provide a custom highlight UI behind the selected text.
- [protocol UITextSelectionHandleView](uitextselectionhandleview.md)
  An interface you use to draw custom the selection handles for ranges of text.
- [protocol UITextCursorView](uitextcursorview.md)
  An interface you use to draw the insertion point in a piece of text.
- [class UIStandardTextCursorView](uistandardtextcursorview.md)
  A view that draws the standard system insertion point in a piece of text.
- [class UITextCursorDropPositionAnimator](uitextcursordroppositionanimator.md)
- [class UITextLoupeSession](uitextloupesession.md)
  An object that manages the presentation of the system magnifier at the location you specify.
### Text actions and menus
- [class UITextItem](uitextitem.md)
  An object for attaching custom actions and menus to links, text attachments, or other specific text in a text view.
- [UITextItem.MenuConfiguration](uitextitem/menuconfiguration.md)
  An object that describes what type of menu and preview to show for a text item.
- [protocol UITextViewDelegate](uitextviewdelegate.md)
  The methods for receiving editing-related messages for text view objects.
### Smart Reply for messaging
- [Adopting Smart Reply in your messaging or email app](adopting-smart-reply-in-your-messaging-or-email-app.md)
  Generate reply suggestions by using Apple Intelligence and put selected text into your text UI.
- [class UIConversationContext](uiconversationcontext.md)
  A base class that represents a conversation between participants, such as in an email or messaging app.
- [UIConversationContext.Entry](uiconversationcontext/entry.md)
  A base class that represents a message in a conversation.
- [class UIMailConversationContext](uimailconversationcontext.md)
  A class that represents an email conversation.
- [UIMailConversationContext.MailEntry](uimailconversationcontext/mailentry.md)
  A class that represents a specific email in an email thread.
- [class UIMessageConversationContext](uimessageconversationcontext.md)
  A class that represents a message conversation.
- [UIMessageConversationContext.MessageEntry](uimessageconversationcontext/messageentry.md)
  A class that represents a message in a message conversation.
- [class UIInputSuggestion](uiinputsuggestion.md)
  A base class you use to handle suggestions from the keyboard or system.
- [class UISmartReplySuggestion](uismartreplysuggestion.md)
  A class you use to handle a Smart Reply suggestion.
### Text tokenizer
- [protocol UITextInputTokenizer](uitextinputtokenizer.md)
  A tokenizer, which is an object that allows the text input system to evaluate text units of different granularities.
- [class UITextInputStringTokenizer](uitextinputstringtokenizer.md)
  A base implementation of the text-input tokenizer protocol.
### Keyboard layout
- [Adjusting your layout with keyboard layout guide](adjusting-your-layout-with-keyboard-layout-guide.md)
  Respond dynamically to keyboard movement by using the tracking features of the keyboard layout guide.
- [class UIKeyboardLayoutGuide](uikeyboardlayoutguide.md)
  A layout guide that represents the space the keyboard occupies in your app’s layout.
- [class UITrackingLayoutGuide](uitrackinglayoutguide.md)
  A layout guide that automatically activates and deactivates layout constraints depending on its proximity to edges.
### Custom keyboards
- [Creating a custom keyboard](creating-a-custom-keyboard.md)
  Add an extension to your Xcode project to provide systemwide customized text input.
- [class UIInputViewController](uiinputviewcontroller.md)
  The primary view controller for a custom keyboard app extension.
- [class UIInputView](uiinputview.md)
  An object that displays and manages custom input for a view when that view becomes the first responder.
- [class UILexicon](uilexicon.md)
  A read-only array of term pairs, each in a lexicon entry object, for a custom keyboard.
- [class UILexiconEntry](uilexiconentry.md)
  A read-only term pair, available within a lexicon object, for a custom keyboard.
- [protocol UITextDocumentProxy](uitextdocumentproxy.md)
  An object that provides textual context to a custom keyboard.
### Physical keyboards
- [Handling key presses made on a physical keyboard](handling-key-presses-made-on-a-physical-keyboard.md)
  Detect when someone presses and releases keys on a physical keyboard.
- [Navigating an app’s user interface using a keyboard](navigating-an-app-s-user-interface-using-a-keyboard.md)
  Navigate between user interface elements using a keyboard and focusable UI elements in iPad apps and apps built with Mac Catalyst.
- [Adding hardware keyboard support to your app](adding-hardware-keyboard-support-to-your-app.md)
  Enhance interactions with your app by handling raw keyboard events, writing custom keyboard shortcuts, and working with gesture recognizers.
- [class UIKey](uikey.md)
  An object that provides information about the state of a keyboard key.
- [enum UIKeyboardHIDUsage](uikeyboardhidusage.md)
  A set of HID usage codes that identify the keys of a USB keyboard.

## See Also

- [Text display and fonts](text-display-and-fonts.md)
  Display text, manage fonts, and check spelling.
- [TextKit](textkit.md)
  Manage text storage and perform custom layout of text-based content in your app’s views.
- [Writing Tools](writing-tools.md)
  Add support for Writing Tools to your app’s text views.
- [Handwriting recognition](handwriting-recognition.md)
  Configure text fields and custom views that accept text to handle input from Apple Pencil.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/keyboards-and-input)*