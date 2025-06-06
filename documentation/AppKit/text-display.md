# Text Display

**Framework**: AppKit

Display text and check spelling.

#### Overview

In most cases, you can lay out your app’s text using the [`NSTextField`](nstextfield.md) or [`NSTextView`](nstextview.md) classes (or their subclasses). Use the [`NSTextField`](nstextfield.md) class to add either a label or a simple text input. Use the [`NSTextView`](nstextview.md) class to provide more comprehensive layout and editing features for larger bodies of text.

For example, [`NSTextView`](nstextview.md) supports rich text, attachments (graphics, file, and other), input management and key binding, and marked text attributes. [`NSTextView`](nstextview.md) works with the font panel and menu, rulers and paragraph styles, the Services facility (for example, the spell-checking service), and the pasteboard.

[`NSTextView`](nstextview.md) also allows customizing through delegation and notifications—you rarely need to subclass [`NSTextView`](nstextview.md). You rarely create instances of [`NSTextView`](nstextview.md) programmatically either, because objects on Interface Builder’s palettes, such as [`NSTextField`](nstextfield.md), [`NSForm`](nsform.md), and [`NSScrollView`](nsscrollview.md), already contain [`NSTextView`](nstextview.md) objects.

For even more powerful and more creative text manipulation (such as displaying text in a circle) see [`TextKit`](textkit.md).

##### Spell Checking

The [`NSSpellServer`](https://developer.apple.com/documentation/Foundation/NSSpellServer) class lets you define a spell-checking service and provide it as a service to other apps. To connect your app to a spell-checking service, use the [`NSSpellChecker`](nsspellchecker.md) class. The [`NSIgnoreMisspelledWords`](nsignoremisspelledwords.md) and [`NSChangeSpelling`](nschangespelling.md) protocols support the spell-checking mechanism.

## Topics

### Text views
- [class NSTextField](nstextfield.md)
  Text the user can select or edit to send an action message to a target when the user presses the Return key.
- [protocol NSTextFieldDelegate](nstextfielddelegate.md)
  A protocol that a text field delegate can use to control its field editor action menu.
- [class NSTextView](nstextview.md)
  A view that draws text and handles user interactions with that text.
- [protocol NSTextViewDelegate](nstextviewdelegate.md)
  A set of optional methods that text view delegates can use to manage selection, set text attributes, work with the spell checker, and more.
- [protocol NSTextDelegate](nstextdelegate.md)
  A set of optional methods implemented by the delegate of an [`NSText`](nstext.md) object to edit text and change text formats.
- [class NSText](nstext.md)
  The most general programmatic interface for objects that manage text.
### Text input
- [Adopting the system text cursor in custom text views](adopting-the-system-text-cursor-in-custom-text-views.md)
  Incorporate the system text cursor into your custom text UI in AppKit.
- [class NSTextInputContext](nstextinputcontext.md)
  An object that represents the Cocoa text input system.
- [protocol NSTextInputClient](nstextinputclient.md)
  A set of methods that text views need to implement to interact properly with the text input management system.
- [class NSTextAlternatives](nstextalternatives.md)
  A list of alternative strings for a piece of text.
- [protocol NSTextContent](nstextcontent.md)
  A protocol that describes specific kinds of input content types.
- [class NSTextInsertionIndicator](nstextinsertionindicator.md)
  A view that represents the insertion indicator in text.
- [NSTextInsertionIndicator.DisplayMode](nstextinsertionindicator/displaymode-swift.enum.md)
  Constants that determine how to display the system text cursor in a custom text UI.
- [NSTextInsertionIndicator.AutomaticModeOptions](nstextinsertionindicator/automaticmodeoptions-swift.struct.md)
  Options that affect the automatic display mode.
### Text-checking
- [class NSTextCheckingController](nstextcheckingcontroller.md)
- [protocol NSTextCheckingClient](nstextcheckingclient.md)
- [protocol NSTextInputTraits](nstextinputtraits.md)
- [enum NSTextInputTraitType](nstextinputtraittype.md)
### Spell-checking
- [class NSSpellChecker](nsspellchecker.md)
  An interface to the Cocoa spell-checking service.
- [protocol NSChangeSpelling](nschangespelling.md)
  A protocol that responder objects can implement to correct a misspelled word.
- [protocol NSIgnoreMisspelledWords](nsignoremisspelledwords.md)
  A protocol that enables the Ignore button in the Spelling panel to function properly.
### Deprecated
- [protocol NSTextInput](nstextinput.md)
  A set of methods that text views need to implement to interact properly with the text input management system.

## See Also

- [TextKit](textkit.md)
  Manage text storage and perform custom layout of text-based content in your app’s views.
- [Fonts](fonts.md)
  Manage the fonts used to display text.
- [Writing Tools](writing-tools.md)
  Add support for Writing Tools to your app’s text views.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/text-display)*