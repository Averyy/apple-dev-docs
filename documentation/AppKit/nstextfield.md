# NSTextField

**Framework**: AppKit  
**Kind**: class

Text the user can select or edit to send an action message to a target when the user presses the Return key.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
class NSTextField
```

## Mentions

- [Adopting the system text cursor in custom text views](adopting-the-system-text-cursor-in-custom-text-views.md)
- [Adding Writing Tools support to a custom AppKit view](adding-writing-tools-support-to-a-custom-nsview.md)
- [Customizing Writing Tools behavior for AppKit views](customizing-writing-tools-behavior-for-system-views.md)

#### Overview

The [`NSTextField`](nstextfield.md) class uses the [`NSTextFieldCell`](nstextfieldcell.md) class to implement its user interface. Text fields display text either as a static label or as an editable input field. The content of a text field is either plain text or a rich-text attributed string. Text fields also support line wrapping to display multiline text, and a variety of truncation styles if the content doesn’t fit the available space.

The parent class, [`NSControl`](nscontrol.md), provides the methods for setting the values of the text field, such as [`stringValue`](nscontrol/stringvalue.md) and [`doubleValue`](nscontrol/doublevalue.md). There are corresponding methods to retrieve values.

In macOS 12 and later, if you explicitly call the `layoutManager` property on your text field, the framework will revert to a compatibility mode that uses [`NSLayoutManager`](nslayoutmanager.md). The text view also switches to this compatibility mode when it encounters text content that’s not yet supported.

## Topics

### Creating Text Fields
- [convenience init(labelWithAttributedString: NSAttributedString)](nstextfield/init(labelwithattributedstring:).md)
  Creates a text field for use as a static label that displays styled text, doesn’t wrap, and doesn’t have selectable text.
- [convenience init(labelWithString: String)](nstextfield/init(labelwithstring:).md)
  Initializes a text field for use as a static label that uses the system default font, doesn’t wrap, and doesn’t have selectable text.
- [convenience init(string: String)](nstextfield/init(string:).md)
  Initializes a single-line editable text field for user input using the system default font and standard visual appearance.
- [convenience init(wrappingLabelWithString: String)](nstextfield/init(wrappinglabelwithstring:).md)
  Initializes a text field for use as a multiline static label with selectable text that uses the system default font.
### Controlling Selection and Editing
- [var isSelectable: Bool](nstextfield/isselectable.md)
  A Boolean value that determines whether the user can select the content of the text field.
- [var isEditable: Bool](nstextfield/iseditable.md)
  A Boolean value that controls whether the user can edit the value in the text field.
### Controlling Rich Text Behavior
- [var allowsEditingTextAttributes: Bool](nstextfield/allowseditingtextattributes.md)
  A Boolean value that controls whether the user can change font attributes of the text field’s string.
- [var importsGraphics: Bool](nstextfield/importsgraphics.md)
  A Boolean value that controls whether the user can drag image files into the text field.
### Setting Placeholder Text
- [var placeholderString: String?](nstextfield/placeholderstring.md)
  The string the text field displays when empty to help the user understand the text field’s purpose.
- [var placeholderAttributedString: NSAttributedString?](nstextfield/placeholderattributedstring.md)
  The attributed string the text field displays when empty to help the user understand the text field’s purpose.
### Configuring Line Wrapping
- [var lineBreakStrategy: NSParagraphStyle.LineBreakStrategy](nstextfield/linebreakstrategy.md)
  The strategy that the system uses to break lines when laying out multiple lines of text.
- [var allowsDefaultTighteningForTruncation: Bool](nstextfield/allowsdefaulttighteningfortruncation.md)
  A Boolean value that controls whether single-line text fields tighten intercharacter spacing before truncating the text.
- [var maximumNumberOfLines: Int](nstextfield/maximumnumberoflines.md)
  The maximum number of lines a wrapping text field displays before clipping or truncating the text.
### Sizing with Auto Layout
- [var preferredMaxLayoutWidth: CGFloat](nstextfield/preferredmaxlayoutwidth.md)
  The maximum width of the text field’s intrinsic content size.
### Setting the Text Color
- [var textColor: NSColor?](nstextfield/textcolor.md)
  The color of the text field’s content.
### Controlling the Background
- [var backgroundColor: NSColor?](nstextfield/backgroundcolor.md)
  The color of the background the text field’s cell draws behind the text.
- [var drawsBackground: Bool](nstextfield/drawsbackground.md)
  A Boolean value that controls whether the text field’s cell draws a background color behind the text.
- [var isBezeled: Bool](nstextfield/isbezeled.md)
  A Boolean value that controls whether the text field draws a bezeled background around its contents.
- [var bezelStyle: NSTextField.BezelStyle](nstextfield/bezelstyle-swift.property.md)
  The text field’s bezel style, square or rounded.
- [NSTextField.BezelStyle](nstextfield/bezelstyle-swift.enum.md)
  The style of bezel the text field displays.
### Setting a Border
- [var isBordered: Bool](nstextfield/isbordered.md)
  A Boolean value that controls whether the text field draws a solid black border around its contents.
### Selecting the Text
- [func selectText(Any?)](nstextfield/selecttext(_:).md)
  Ends editing in the text field and, if it’s selectable, selects the entire text content.
### Working with the Responder Chain
- [var acceptsFirstResponder: Bool](nstextfield/acceptsfirstresponder.md)
  A Boolean value that indicates whether the text field is editable and accepts first responder status.
### Using Keyboard Interface Control
- [var allowsCharacterPickerTouchBarItem: Bool](nstextfield/allowscharacterpickertouchbaritem.md)
  A Boolean value that controls whether the Touch Bar displays the character picker item for rich text fields.
### Supporting Text Completion
- [var isAutomaticTextCompletionEnabled: Bool](nstextfield/isautomatictextcompletionenabled.md)
  A Boolean value that indicates whether the text field automatically completes text as the user types.
### Setting the Delegate
- [var delegate: (any NSTextFieldDelegate)?](nstextfield/delegate.md)
  The text field’s delegate.
### Implementing Delegate Methods
- [func textShouldBeginEditing(NSText) -> Bool](nstextfield/textshouldbeginediting(_:).md)
  Requests permission to begin editing a text object.
- [func textDidBeginEditing(Notification)](nstextfield/textdidbeginediting(_:).md)
  Posts a notification to the default notification center that the text is about to go into edit mode.
- [func textDidChange(Notification)](nstextfield/textdidchange(_:).md)
  Posts a notification when the text changes, and forwards the message to the text field’s cell if it responds.
- [func textShouldEndEditing(NSText) -> Bool](nstextfield/textshouldendediting(_:).md)
  Performs validation on the text field’s new value.
- [func textDidEndEditing(Notification)](nstextfield/textdidendediting(_:).md)
  Posts a notification when the text is no longer in edit mode.
### Instance Properties
- [var allowsCharacterPickerTouchBarItem: Bool](nstextfield/allowscharacterpickertouchbaritem.md)
  A Boolean value that controls whether the Touch Bar displays the character picker item for rich text fields.
- [var allowsWritingTools: Bool](nstextfield/allowswritingtools.md)
- [var allowsWritingToolsAffordance: Bool](nstextfield/allowswritingtoolsaffordance.md)
- [var suggestionsDelegate: (any NSTextSuggestionsDelegate)?](nstextfield/suggestionsdelegate.md)
  The delegate that provides text suggestions for the receiving text field and responds to the user highlighting and selecting items.

## Relationships

### Inherits From
- [NSControl](nscontrol.md)
### Inherited By
- [NSComboBox](nscombobox.md)
- [NSSearchField](nssearchfield.md)
- [NSSecureTextField](nssecuretextfield.md)
- [NSTokenField](nstokenfield.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSAccessibilityElementProtocol](nsaccessibilityelementprotocol.md)
- [NSAccessibilityNavigableStaticText](nsaccessibilitynavigablestatictext.md)
- [NSAccessibilityProtocol](nsaccessibilityprotocol.md)
- [NSAccessibilityStaticText](nsaccessibilitystatictext.md)
- [NSAnimatablePropertyContainer](nsanimatablepropertycontainer.md)
- [NSAppearanceCustomization](nsappearancecustomization.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSDraggingDestination](nsdraggingdestination.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSStandardKeyBindingResponding](nsstandardkeybindingresponding.md)
- [NSTextContent](nstextcontent.md)
- [NSTouchBarProvider](nstouchbarprovider.md)
- [NSUserActivityRestoring](nsuseractivityrestoring.md)
- [NSUserInterfaceItemIdentification](nsuserinterfaceitemidentification.md)
- [NSUserInterfaceValidations](nsuserinterfacevalidations.md)
- [Sendable](../Swift/Sendable.md)

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextfield)*