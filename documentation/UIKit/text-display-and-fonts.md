# Text display and fonts

**Framework**: UIKit

Display text, manage fonts, and check spelling.

## Topics

### Text views
- [class UILabel](uilabel.md)
  A view that displays one or more lines of informational text.
- [class UITextField](uitextfield.md)
  An object that displays an editable text area in your interface.
- [class UITextView](uitextview.md)
  A scrollable, multiline text region.
- [Drag and drop customization](drag-and-drop-customization.md)
  Extend the standard drag and drop support for text views to include custom types of content.
### Text bounds sizing
- [protocol UILetterformAwareAdjusting](uiletterformawareadjusting.md)
  The typographic bounds-sizing behavior to handle text with fonts that contain oversize characters.
### Text formatting
- [class UITextFormattingCoordinator](uitextformattingcoordinator.md)
  An object that coordinates text formatting using the standard Mac font panel.
- [typealias UITextAttributesConversionHandler](uitextattributesconversionhandler.md)
  A handler for updating text with current font panel settings.
### Fonts
- [Scaling Fonts Automatically](scaling-fonts-automatically.md)
  Scale text in your interface automatically using Dynamic Type.
- [Adding a Custom Font to Your App](adding-a-custom-font-to-your-app.md)
  Add a custom font to your app and use it in your app’s interface.
- [class UIFont](uifont.md)
  An object that provides access to the font’s characteristics.
- [class UIFontDescriptor](uifontdescriptor.md)
  A collection of attributes that describes a font.
- [UIFontDescriptor.SymbolicTraits](uifontdescriptor/symbolictraits-swift.struct.md)
  Constants that describe the stylistic aspects of a font.
- [class UIFontMetrics](uifontmetrics.md)
  A utility object for obtaining custom fonts that scale to support Dynamic Type.
### Font picker
- [class UIFontPickerViewController](uifontpickerviewcontroller.md)
  A view controller that manages the interface for selecting a font that the system provides or the user installs.
- [protocol UIFontPickerViewControllerDelegate](uifontpickerviewcontrollerdelegate.md)
  A set of optional methods for receiving messages about the user’s interaction with the font picker.
- [UIFontPickerViewController.Configuration](uifontpickerviewcontroller/configuration-swift.class.md)
  The filters and display settings a font picker view controller uses to set up a font picker.
### Spell checking
- [class UITextChecker](uitextchecker.md)
  An object to check a string (usually the text of a document) for misspelled words.
### Text manipulations
- [init(NSTextAlignment)](../CoreText/CTTextAlignment/init(_:).md)
  Converts a UIKit text alignment constant value to the matching constant value that Core Text uses.
- [init(CTTextAlignment)](nstextalignment/init(_:).md)
  Converts a Core Text alignment constant value to the matching constant value in UIKit.
### Metrics
- [class UITextPosition](uitextposition.md)
  A position in a text container—that is, an index into the backing string in a text-display view.
- [class UITextRange](uitextrange.md)
  A range of characters in a text container with a starting index and an ending index in string backing a text-entry object.
- [class UITextSelectionRect](uitextselectionrect.md)
  An encapsulation of information about a selected range of text in a document.

## See Also

- [TextKit](textkit.md)
  Manage text storage and perform custom layout of text-based content in your app’s views.
- [Keyboards and input](keyboards-and-input.md)
  Configure the system keyboard, create your own keyboards to handle input, or detect key presses on a physical keyboard.
- [Writing Tools](writing-tools.md)
  Add support for Writing Tools to your app’s text views.
- [Handwriting recognition](handwriting-recognition.md)
  Configure text fields and custom views that accept text to handle input from Apple Pencil.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/text-display-and-fonts)*