# Text input and output

**Framework**: SwiftUI

Display formatted text and get text input from the user.

#### Overview

To display read-only text, or read-only text paired with an image, use the built-in [`Text`](text.md) or [`Label`](label.md) views, respectively. When you need to collect text input from the user, use an appropriate text input view, like [`TextField`](textfield.md) or [`TextEditor`](texteditor.md).

![None](https://docs-assets.developer.apple.com/published/a8d0f352ff6dabd1c3d1e3fdfb577250/text-input-and-output-hero%402x.png)

You add view modifiers to control the text’s font, selectability, alignment, layout direction, and so on. These modifiers also affect other views that display text, like the labels on controls, even if you don’t define an explicit [`Text`](text.md) view.

For design guidance, see [`Typography`](https://developer.apple.com/design/Human-Interface-Guidelines/typography) in the Human Interface Guidelines.

## Topics

### Displaying text
- [struct Text](text.md)
  A view that displays one or more lines of read-only text.
- [struct Label](label.md)
  A standard label for user interface items, consisting of an icon with a title.
- [func labelStyle<S>(S) -> some View](view/labelstyle(_:).md)
  Sets the style for labels within this view.
### Getting text input
- [Building rich SwiftUI text experiences](building-rich-swiftui-text-experiences.md)
  Build an editor for formatted text using SwiftUI text editor views and attributed strings.
- [struct TextField](textfield.md)
  A control that displays an editable text interface.
- [func textFieldStyle<S>(S) -> some View](view/textfieldstyle(_:).md)
  Sets the style for text fields within this view.
- [struct SecureField](securefield.md)
  A control into which people securely enter private text.
- [struct TextEditor](texteditor.md)
  A view that can display and edit long-form text.
### Selecting text
- [func textSelection<S>(S) -> some View](view/textselection(_:).md)
  Controls whether people can select text within this view.
- [protocol TextSelectability](textselectability.md)
  A type that describes the ability to select text.
- [struct TextSelection](textselection.md)
  Represents a selection of text.
- [func textSelectionAffinity(TextSelectionAffinity) -> some View](view/textselectionaffinity(_:).md)
  Sets the direction of a selection or cursor relative to a text character.
- [var textSelectionAffinity: TextSelectionAffinity](environmentvalues/textselectionaffinity.md)
  A representation of the direction or association of a selection or cursor relative to a text character. This concept becomes much more prominent when dealing with bidirectional text (text that contains both LTR and RTL scripts, like English and Arabic combined).
- [enum TextSelectionAffinity](textselectionaffinity.md)
  A representation of the direction or association of a selection or cursor relative to a text character. This concept becomes much more prominent when dealing with bidirectional text (text that contains both LTR and RTL scripts, like English and Arabic combined).
- [struct AttributedTextSelection](attributedtextselection.md)
  Represents a selection of attributed text.
### Setting a font
- [Applying custom fonts to text](applying-custom-fonts-to-text.md)
  Add and use a font in your app that scales with Dynamic Type.
- [func font(Font?) -> some View](view/font(_:).md)
  Sets the default font for text in this view.
- [func fontDesign(Font.Design?) -> some View](view/fontdesign(_:).md)
  Sets the font design of the text in this view.
- [func fontWeight(Font.Weight?) -> some View](view/fontweight(_:).md)
  Sets the font weight of the text in this view.
- [func fontWidth(Font.Width?) -> some View](view/fontwidth(_:).md)
  Sets the font width of the text in this view.
- [var font: Font?](environmentvalues/font.md)
  The default font of this environment.
- [struct Font](font.md)
  An environment-dependent font.
### Adjusting text size
- [func textScale(Text.Scale, isEnabled: Bool) -> some View](view/textscale(_:isenabled:).md)
  Applies a text scale to text in the view.
- [func dynamicTypeSize(_:)](view/dynamictypesize(_:).md)
  Sets the Dynamic Type size within the view to the given value.
- [var dynamicTypeSize: DynamicTypeSize](environmentvalues/dynamictypesize.md)
  The current Dynamic Type size.
- [enum DynamicTypeSize](dynamictypesize.md)
  A Dynamic Type size, which specifies how large scalable content should be.
- [struct ScaledMetric](scaledmetric.md)
  A dynamic property that scales a numeric value.
- [protocol TextVariantPreference](textvariantpreference.md)
  A protocol for controlling the size variant of text views.
- [struct FixedTextVariant](fixedtextvariant.md)
  The default text variant preference that chooses the largest available variant.
- [struct SizeDependentTextVariant](sizedependenttextvariant.md)
  The size dependent variant preference allows the text to take the available space into account when choosing the variant to display.
### Controlling text style
- [func bold(Bool) -> some View](view/bold(_:).md)
  Applies a bold font weight to the text in this view.
- [func italic(Bool) -> some View](view/italic(_:).md)
  Applies italics to the text in this view.
- [func underline(Bool, pattern: Text.LineStyle.Pattern, color: Color?) -> some View](view/underline(_:pattern:color:).md)
  Applies an underline to the text in this view.
- [func strikethrough(Bool, pattern: Text.LineStyle.Pattern, color: Color?) -> some View](view/strikethrough(_:pattern:color:).md)
  Applies a strikethrough to the text in this view.
- [func textCase(Text.Case?) -> some View](view/textcase(_:).md)
  Sets a transform for the case of the text contained in this view when displayed.
- [var textCase: Text.Case?](environmentvalues/textcase.md)
  A stylistic override to transform the case of `Text` when displayed, using the environment’s locale.
- [func monospaced(Bool) -> some View](view/monospaced(_:).md)
  Modifies the fonts of all child views to use the fixed-width variant of the current font, if possible.
- [func monospacedDigit() -> some View](view/monospaceddigit.md)
  Modifies the fonts of all child views to use fixed-width digits, if possible, while leaving other characters proportionally spaced.
- [protocol AttributedTextFormattingDefinition](attributedtextformattingdefinition.md)
  A protocol for defining how text can be styled in a certain context, e.g. a `TextEditor`.
- [protocol AttributedTextValueConstraint](attributedtextvalueconstraint.md)
  A protocol for defining a constraint on the value of a certain attribute.
- [enum AttributedTextFormatting](attributedtextformatting.md)
  A namespace for types related to attributed text formatting definitions.
### Managing text layout
- [func truncationMode(Text.TruncationMode) -> some View](view/truncationmode(_:).md)
  Sets the truncation mode for lines of text that are too long to fit in the available space.
- [var truncationMode: Text.TruncationMode](environmentvalues/truncationmode.md)
  A value that indicates how the layout truncates the last line of text to fit into the available space.
- [func allowsTightening(Bool) -> some View](view/allowstightening(_:).md)
  Sets whether text in this view can compress the space between characters when necessary to fit text in a line.
- [var allowsTightening: Bool](environmentvalues/allowstightening.md)
  A Boolean value that indicates whether inter-character spacing should tighten to fit the text into the available space.
- [func minimumScaleFactor(CGFloat) -> some View](view/minimumscalefactor(_:).md)
  Sets the minimum amount that text in this view scales down to fit in the available space.
- [var minimumScaleFactor: CGFloat](environmentvalues/minimumscalefactor.md)
  The minimum permissible proportion to shrink the font size to fit the text into the available space.
- [func baselineOffset(CGFloat) -> some View](view/baselineoffset(_:).md)
  Sets the vertical offset for the text relative to its baseline in this view.
- [func kerning(CGFloat) -> some View](view/kerning(_:).md)
  Sets the spacing, or kerning, between characters for the text in this view.
- [func tracking(CGFloat) -> some View](view/tracking(_:).md)
  Sets the tracking for the text in this view.
- [func flipsForRightToLeftLayoutDirection(Bool) -> some View](view/flipsforrighttoleftlayoutdirection(_:).md)
  Sets whether this view mirrors its contents horizontally when the layout direction is right-to-left.
- [enum TextAlignment](textalignment.md)
  An alignment position for text along the horizontal axis.
### Rendering text
- [Creating visual effects with SwiftUI](creating-visual-effects-with-swiftui.md)
  Add scroll effects, rich color treatments, custom transitions, and advanced effects using shaders and a text renderer.
- [protocol TextAttribute](textattribute.md)
  A value that you can attach to text views and that text renderers can query.
- [func textRenderer<T>(T) -> some View](view/textrenderer(_:).md)
  Returns a new view such that any text views within it will use `renderer` to draw themselves.
- [protocol TextRenderer](textrenderer.md)
  A value that can replace the default text view rendering behavior.
- [struct TextProxy](textproxy.md)
  A proxy for a text view that custom text renderers use.
### Limiting line count for multiline text
- [func lineLimit(_:)](view/linelimit(_:).md)
  Sets to a closed range the number of lines that text can occupy in this view.
- [func lineLimit(Int, reservesSpace: Bool) -> some View](view/linelimit(_:reservesspace:).md)
  Sets a limit for the number of lines text can occupy in this view.
- [var lineLimit: Int?](environmentvalues/linelimit.md)
  The maximum number of lines that text can occupy in a view.
### Formatting multiline text
- [func lineSpacing(CGFloat) -> some View](view/linespacing(_:).md)
  Sets the amount of space between lines of text in this view.
- [var lineSpacing: CGFloat](environmentvalues/linespacing.md)
  The distance in points between the bottom of one line fragment and the top of the next.
- [func multilineTextAlignment(TextAlignment) -> some View](view/multilinetextalignment(_:).md)
  Sets the alignment of a text view that contains multiple lines of text.
- [var multilineTextAlignment: TextAlignment](environmentvalues/multilinetextalignment.md)
  An environment value that indicates how a text view aligns its lines when the content wraps or contains newlines.
### Formatting date and time
- [enum SystemFormatStyle](systemformatstyle.md)
  A namespace for format styles that implement designs used across Apple’s platformes.
- [struct TimeDataSource](timedatasource.md)
  A source of time related data.
### Managing text entry
- [func autocorrectionDisabled(Bool) -> some View](view/autocorrectiondisabled(_:).md)
  Sets whether to disable autocorrection for this view.
- [var autocorrectionDisabled: Bool](environmentvalues/autocorrectiondisabled.md)
  A Boolean value that determines whether the view hierarchy has auto-correction enabled.
- [func keyboardType(UIKeyboardType) -> some View](view/keyboardtype(_:).md)
  Sets the keyboard type for this view.
- [func scrollDismissesKeyboard(ScrollDismissesKeyboardMode) -> some View](view/scrolldismisseskeyboard(_:).md)
  Configures the behavior in which scrollable content interacts with the software keyboard.
- [func textContentType(_:)](view/textcontenttype(_:).md)
  Sets the text content type for this view, which the system uses to offer suggestions while the user enters text on macOS.
- [func textInputAutocapitalization(TextInputAutocapitalization?) -> some View](view/textinputautocapitalization(_:).md)
  Sets how often the shift key in the keyboard is automatically enabled.
- [struct TextInputAutocapitalization](textinputautocapitalization.md)
  The kind of autocapitalization behavior applied during text input.
- [func textInputCompletion(String) -> some View](view/textinputcompletion(_:).md)
  Associates a fully formed string with the value of this view when used as a text input suggestion
- [func textInputSuggestions<S>(() -> S) -> some View](view/textinputsuggestions(_:).md)
  Configures the text input suggestions for this view.
- [func textInputSuggestions<Data, Content>(Data, content: (Data.Element) -> Content) -> some View](view/textinputsuggestions(_:content:).md)
  Configures the text input suggestions for this view.
- [func textInputSuggestions<Data, ID, Content>(Data, id: KeyPath<Data.Element, ID>, content: (Data.Element) -> Content) -> some View](view/textinputsuggestions(_:id:content:).md)
  Configures the text input suggestions for this view.
- [func textContentType(WKTextContentType?) -> some View](view/textcontenttype(_:)-4dqqb.md)
  Sets the text content type for this view, which the system uses to offer suggestions while the user enters text on a watchOS device.
- [func textContentType(NSTextContentType?) -> some View](view/textcontenttype(_:)-6fic1.md)
  Sets the text content type for this view, which the system uses to offer suggestions while the user enters text on macOS.
- [func textContentType(UITextContentType?) -> some View](view/textcontenttype(_:)-ufdv.md)
  Sets the text content type for this view, which the system uses to offer suggestions while the user enters text on an iOS or tvOS device.
- [struct TextInputFormattingControlPlacement](textinputformattingcontrolplacement.md)
  A structure defining the system text formatting controls available on each platform.
### Dictating text
- [func searchDictationBehavior(TextInputDictationBehavior) -> some View](view/searchdictationbehavior(_:).md)
  Configures the dictation behavior for any search fields configured by the searchable modifier.
- [struct TextInputDictationActivation](textinputdictationactivation.md)
- [struct TextInputDictationBehavior](textinputdictationbehavior.md)
### Configuring the Writing Tools behavior
- [func writingToolsBehavior(WritingToolsBehavior) -> some View](view/writingtoolsbehavior(_:).md)
  Specifies the Writing Tools behavior for text and text input in the environment.
- [struct WritingToolsBehavior](writingtoolsbehavior.md)
  The Writing Tools editing experience for text and text input.
### Specifying text equivalents
- [func typeSelectEquivalent(_:)](view/typeselectequivalent(_:).md)
  Sets an explicit type select equivalent text in a collection, such as a list or table.
### Localizing text
- [Preparing views for localization](preparing-views-for-localization.md)
  Specify hints and add strings to localize your SwiftUI views.
- [struct LocalizedStringKey](localizedstringkey.md)
  The key used to look up an entry in a strings file or strings dictionary file.
- [var locale: Locale](environmentvalues/locale.md)
  The current locale that views should use.
- [func typesettingLanguage(_:isEnabled:)](view/typesettinglanguage(_:isenabled:).md)
  Specifies the language for typesetting.
- [struct TypesettingLanguage](typesettinglanguage.md)
  Defines how typesetting language is determined for text.
### Deprecated types
- [enum ContentSizeCategory](contentsizecategory.md)
  The sizes that you can specify for content.

## See Also

- [View fundamentals](view-fundamentals.md)
  Define the visual elements of your app using a hierarchy of views.
- [View configuration](view-configuration.md)
  Adjust the characteristics of views in a hierarchy.
- [View styles](view-styles.md)
  Apply built-in and custom appearances and behaviors to different types of views.
- [Animations](animations.md)
  Create smooth visual updates in response to state changes.
- [Images](images.md)
  Add images and symbols to your app’s user interface.
- [Controls and indicators](controls-and-indicators.md)
  Display values and get user selections.
- [Menus and commands](menus-and-commands.md)
  Provide space-efficient, context-dependent access to commands and controls.
- [Shapes](shapes.md)
  Trace and fill built-in and custom shapes with a color, gradient, or other pattern.
- [Drawing and graphics](drawing-and-graphics.md)
  Enhance your views with graphical effects and customized drawings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/text-input-and-output)*