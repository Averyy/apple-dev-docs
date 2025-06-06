# Text and symbol modifiers

**Framework**: SwiftUI

Manage the rendering, selection, and entry of text in your view.

#### Overview

SwiftUI provides built-in views that display text to the user, like [`Text`](text.md) and [`Label`](label.md), or that collect text from the user, like [`TextField`](textfield.md) and [`TextEditor`](texteditor.md). Use text and symbol modifiers to control how SwiftUI displays and manages that text. For example, you can set a font, specify text layout parameters, and indicate what kind of input to expect.

To learn more about the kinds of views that you use to display text and the ways in which you can configure those views, see [`Text input and output`](text-input-and-output.md).

## Topics

### Fonts
- [func font(Font?) -> some View](view/font(_:).md)
  Sets the default font for text in this view.
### Dynamic type
- [func dynamicTypeSize(_:)](view/dynamictypesize(_:).md)
  Sets the Dynamic Type size within the view to the given value.
### Text style
- [func bold(Bool) -> some View](view/bold(_:).md)
  Applies a bold font weight to the text in this view.
- [func fontDesign(Font.Design?) -> some View](view/fontdesign(_:).md)
  Sets the font design of the text in this view.
- [func fontWeight(Font.Weight?) -> some View](view/fontweight(_:).md)
  Sets the font weight of the text in this view.
- [func fontWidth(Font.Width?) -> some View](view/fontwidth(_:).md)
  Sets the font width of the text in this view.
- [func italic(Bool) -> some View](view/italic(_:).md)
  Applies italics to the text in this view.
- [func monospaced(Bool) -> some View](view/monospaced(_:).md)
  Modifies the fonts of all child views to use the fixed-width variant of the current font, if possible.
- [func monospacedDigit() -> some View](view/monospaceddigit.md)
  Modifies the fonts of all child views to use fixed-width digits, if possible, while leaving other characters proportionally spaced.
- [func strikethrough(Bool, pattern: Text.LineStyle.Pattern, color: Color?) -> some View](view/strikethrough(_:pattern:color:).md)
  Applies a strikethrough to the text in this view.
- [func textCase(Text.Case?) -> some View](view/textcase(_:).md)
  Sets a transform for the case of the text contained in this view when displayed.
- [func textScale(Text.Scale, isEnabled: Bool) -> some View](view/textscale(_:isenabled:).md)
  Applies a text scale to text in the view.
- [func underline(Bool, pattern: Text.LineStyle.Pattern, color: Color?) -> some View](view/underline(_:pattern:color:).md)
  Applies an underline to the text in this view.
### Text layout
- [func allowsTightening(Bool) -> some View](view/allowstightening(_:).md)
  Sets whether text in this view can compress the space between characters when necessary to fit text in a line.
- [func baselineOffset(CGFloat) -> some View](view/baselineoffset(_:).md)
  Sets the vertical offset for the text relative to its baseline in this view.
- [func flipsForRightToLeftLayoutDirection(Bool) -> some View](view/flipsforrighttoleftlayoutdirection(_:).md)
  Sets whether this view mirrors its contents horizontally when the layout direction is right-to-left.
- [func kerning(CGFloat) -> some View](view/kerning(_:).md)
  Sets the spacing, or kerning, between characters for the text in this view.
- [func minimumScaleFactor(CGFloat) -> some View](view/minimumscalefactor(_:).md)
  Sets the minimum amount that text in this view scales down to fit in the available space.
- [func tracking(CGFloat) -> some View](view/tracking(_:).md)
  Sets the tracking for the text in this view.
- [func truncationMode(Text.TruncationMode) -> some View](view/truncationmode(_:).md)
  Sets the truncation mode for lines of text that are too long to fit in the available space.
- [func typesettingLanguage(_:isEnabled:)](view/typesettinglanguage(_:isenabled:).md)
  Specifies the language for typesetting.
### Multiline text
- [func lineLimit(_:)](view/linelimit(_:).md)
  Sets to a closed range the number of lines that text can occupy in this view.
- [func lineLimit(Int, reservesSpace: Bool) -> some View](view/linelimit(_:reservesspace:).md)
  Sets a limit for the number of lines text can occupy in this view.
- [func lineSpacing(CGFloat) -> some View](view/linespacing(_:).md)
  Sets the amount of space between lines of text in this view.
- [func multilineTextAlignment(TextAlignment) -> some View](view/multilinetextalignment(_:).md)
  Sets the alignment of a text view that contains multiple lines of text.
### Text selection
- [func textSelection<S>(S) -> some View](view/textselection(_:).md)
  Controls whether people can select text within this view.
### Text entry
- [func autocorrectionDisabled(Bool) -> some View](view/autocorrectiondisabled(_:).md)
  Sets whether to disable autocorrection for this view.
- [func keyboardType(UIKeyboardType) -> some View](view/keyboardtype(_:).md)
  Sets the keyboard type for this view.
- [func scrollDismissesKeyboard(ScrollDismissesKeyboardMode) -> some View](view/scrolldismisseskeyboard(_:).md)
  Configures the behavior in which scrollable content interacts with the software keyboard.
- [func textInputAutocapitalization(TextInputAutocapitalization?) -> some View](view/textinputautocapitalization(_:).md)
  Sets how often the shift key in the keyboard is automatically enabled.
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
### Find and replace
- [func findNavigator(isPresented: Binding<Bool>) -> some View](view/findnavigator(ispresented:).md)
  Programmatically presents the find and replace interface for text editor views.
- [func findDisabled(Bool) -> some View](view/finddisabled(_:).md)
  Prevents find and replace operations in a text editor.
- [func replaceDisabled(Bool) -> some View](view/replacedisabled(_:).md)
  Prevents replace operations in a text editor.
### Symbol appearance
- [func symbolRenderingMode(SymbolRenderingMode?) -> some View](view/symbolrenderingmode(_:).md)
  Sets the rendering mode for symbol images within this view.
- [func symbolVariant(SymbolVariants) -> some View](view/symbolvariant(_:).md)
  Makes symbols within the view show a particular variant.

## See Also

- [Accessibility modifiers](view-accessibility.md)
  Make your SwiftUI apps accessible to everyone, including people with disabilities.
- [Appearance modifiers](view-appearance.md)
  Configure a view’s foreground and background styles, controls, and visibility.
- [Auxiliary view modifiers](view-auxiliary-views.md)
  Add and configure supporting views, like toolbars and context menus.
- [Chart view modifiers](view-chart-view.md)
  Configure charts that you declare with Swift Charts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view-text-and-symbols)*