# Text and symbol modifiers

**Framework**: SwiftUI  
**Role**: API Collection

Manage the rendering, selection, and entry of text in your view.

#### Overview

SwiftUI provides built-in views that display text to the user, like [`Text`](./text.md) and [`Label`](./label.md), or that collect text from the user, like [`TextField`](./textfield.md) and [`TextEditor`](./texteditor.md). Use text and symbol modifiers to control how SwiftUI displays and manages that text. For example, you can set a font, specify text layout parameters, and indicate what kind of input to expect.

To learn more about the kinds of views that you use to display text and the ways in which you can configure those views, see [Text input and output](./text-input-and-output.md).

## Topics

### Fonts
- [func font(Font?) -> some View](./view/font%28_%29.md)
  Sets the default font for text in this view.
### Dynamic type
- [func dynamicTypeSize(_:)](./view/dynamictypesize%28_%29.md)
  Sets the Dynamic Type size within the view to the given value.
### Text style
- [func bold(Bool) -> some View](./view/bold%28_%29.md)
  Applies a bold font weight to the text in this view.
- [func fontDesign(Font.Design?) -> some View](./view/fontdesign%28_%29.md)
  Sets the font design of the text in this view.
- [func fontWeight(Font.Weight?) -> some View](./view/fontweight%28_%29.md)
  Sets the font weight of the text in this view.
- [func fontWidth(Font.Width?) -> some View](./view/fontwidth%28_%29.md)
  Sets the font width of the text in this view.
- [func italic(Bool) -> some View](./view/italic%28_%29.md)
  Applies italics to the text in this view.
- [func monospaced(Bool) -> some View](./view/monospaced%28_%29.md)
  Modifies the fonts of all child views to use the fixed-width variant of the current font, if possible.
- [func monospacedDigit() -> some View](./view/monospaceddigit%28%29.md)
  Modifies the fonts of all child views to use fixed-width digits, if possible, while leaving other characters proportionally spaced.
- [func strikethrough(Bool, pattern: Text.LineStyle.Pattern, color: Color?) -> some View](./view/strikethrough%28_,pattern,color%29.md)
  Applies a strikethrough to the text in this view.
- [func textCase(Text.Case?) -> some View](./view/textcase%28_%29.md)
  Sets a transform for the case of the text contained in this view when displayed.
- [func textScale(Text.Scale, isEnabled: Bool) -> some View](./view/textscale%28_,isenabled%29.md)
  Applies a text scale to text in the view.
- [func textRenderer<T>(T) -> some View](./view/textrenderer%28_%29.md)
  Returns a new view such that any text views within it will use `renderer` to draw themselves.
- [func underline(Bool, pattern: Text.LineStyle.Pattern, color: Color?) -> some View](./view/underline%28_,pattern,color%29.md)
  Applies an underline to the text in this view.
- [func attributedTextFormattingDefinition(_:)](./view/attributedtextformattingdefinition%28_%29.md)
  Apply a text formatting definition to nested views.
### Label configuration
- [func labelIconToTitleSpacing(CGFloat) -> some View](./view/labelicontotitlespacing%28_%29.md)
  Set the spacing between the icon and title in labels.
- [func labelReservedIconWidth(CGFloat) -> some View](./view/labelreservediconwidth%28_%29.md)
  Set the width reserved for icons in labels.
### Text layout
- [func allowsTightening(Bool) -> some View](./view/allowstightening%28_%29.md)
  Sets whether text in this view can compress the space between characters when necessary to fit text in a line.
- [func baselineOffset(CGFloat) -> some View](./view/baselineoffset%28_%29.md)
  Sets the vertical offset for the text relative to its baseline in this view.
- [func flipsForRightToLeftLayoutDirection(Bool) -> some View](./view/flipsforrighttoleftlayoutdirection%28_%29.md)
  Sets whether this view mirrors its contents horizontally when the layout direction is right-to-left.
- [func kerning(CGFloat) -> some View](./view/kerning%28_%29.md)
  Sets the spacing, or kerning, between characters for the text in this view.
- [func lineHeight(AttributedString.LineHeight?) -> some View](./view/lineheight%28_%29.md)
  A modifier for the default line height in the view hierarchy.
- [func minimumScaleFactor(CGFloat) -> some View](./view/minimumscalefactor%28_%29.md)
  Sets the minimum amount that text in this view scales down to fit in the available space.
- [func tracking(CGFloat) -> some View](./view/tracking%28_%29.md)
  Sets the tracking for the text in this view.
- [func truncationMode(Text.TruncationMode) -> some View](./view/truncationmode%28_%29.md)
  Sets the truncation mode for lines of text that are too long to fit in the available space.
- [func typesettingLanguage(_:isEnabled:)](./view/typesettinglanguage%28_,isenabled%29.md)
  Specifies the language for typesetting.
- [func writingDirection(strategy: Text.WritingDirectionStrategy) -> some View](./view/writingdirection%28strategy%29.md)
  A modifier for the default text writing direction strategy in the view hierarchy.
### Multiline text
- [func lineLimit(_:)](./view/linelimit%28_%29.md)
  Sets to a closed range the number of lines that text can occupy in this view.
- [func lineLimit(Int, reservesSpace: Bool) -> some View](./view/linelimit%28_,reservesspace%29.md)
  Sets a limit for the number of lines text can occupy in this view.
- [func lineSpacing(CGFloat) -> some View](./view/linespacing%28_%29.md)
  Sets the amount of space between lines of text in this view.
- [func multilineTextAlignment(TextAlignment) -> some View](./view/multilinetextalignment%28_%29.md)
  Sets the alignment of a text view that contains multiple lines of text.
- [func multilineTextAlignment(strategy: Text.AlignmentStrategy) -> some View](./view/multilinetextalignment%28strategy%29.md)
  A modifier for the default text alignment strategy in the view hierarchy.
### Text selection
- [func textSelection<S>(S) -> some View](./view/textselection%28_%29.md)
  Controls whether people can select text within this view.
- [func textSelectionAffinity(TextSelectionAffinity) -> some View](./view/textselectionaffinity%28_%29.md)
  Sets the direction of a selection or cursor relative to a text character.
### Data detection
- [func dataDetection(DataDetector.MatchType, options: DataDetector.Options) -> some View](./view/datadetection%28_,options%29.md)
  Asynchronously detects data in the view’s content and styles them to indicate they are clickable.
### Text entry
- [func autocorrectionDisabled(Bool) -> some View](./view/autocorrectiondisabled%28_%29.md)
  Sets whether to disable autocorrection for this view.
- [func keyboardType(UIKeyboardType) -> some View](./view/keyboardtype%28_%29.md)
  Sets the keyboard type for this view.
- [func scrollDismissesKeyboard(ScrollDismissesKeyboardMode) -> some View](./view/scrolldismisseskeyboard%28_%29.md)
  Configures the behavior in which scrollable content interacts with the software keyboard.
- [func textInputAutocapitalization(TextInputAutocapitalization?) -> some View](./view/textinputautocapitalization%28_%29.md)
  Sets how often the shift key in the keyboard is automatically enabled.
- [func textInputBorderShape(TextInputBorderShape) -> some View](./view/textinputbordershape%28_%29.md)
  Sets the border shape for text input controls in the view hierarchy.
- [func textInputCompletion(String) -> some View](./view/textinputcompletion%28_%29.md)
  Associates a fully formed string with the value of this view when used as a text input suggestion
- [func textInputSuggestions<S>(() -> S) -> some View](./view/textinputsuggestions%28_%29.md)
  Configures the text input suggestions for this view.
- [func textInputSuggestions<Data, Content>(Data, content: (Data.Element) -> Content) -> some View](./view/textinputsuggestions%28_,content%29.md)
  Configures the text input suggestions for this view.
- [func textInputSuggestions<Data, ID, Content>(Data, id: KeyPath<Data.Element, ID>, content: (Data.Element) -> Content) -> some View](./view/textinputsuggestions%28_,id,content%29.md)
  Configures the text input suggestions for this view.
- [func textContentType(_:)](./view/textcontenttype%28_%29.md)
  Sets the text content type for this view, which the system uses to offer suggestions while the user enters text on macOS.
- [func textContentType(WKTextContentType?) -> some View](./view/textcontenttype%28_%29-4dqqb.md)
  Sets the text content type for this view, which the system uses to offer suggestions while the user enters text on a watchOS device.
- [func textContentType(NSTextContentType?) -> some View](./view/textcontenttype%28_%29-6fic1.md)
  Sets the text content type for this view, which the system uses to offer suggestions while the user enters text on macOS.
- [func textContentType(UITextContentType?) -> some View](./view/textcontenttype%28_%29-ufdv.md)
  Sets the text content type for this view, which the system uses to offer suggestions while the user enters text on an iOS or tvOS device.
- [func textInputFormattingControlVisibility(Visibility, for: TextInputFormattingControlPlacement.Set) -> some View](./view/textinputformattingcontrolvisibility%28_,for%29.md)
  Specifies which system text formatting controls are available for people to format text.
### Find and replace
- [func findNavigator(isPresented: Binding<Bool>) -> some View](./view/findnavigator%28ispresented%29.md)
  Programmatically presents the find and replace interface for text editor views.
- [func findDisabled(Bool) -> some View](./view/finddisabled%28_%29.md)
  Prevents find and replace operations in a text editor.
- [func replaceDisabled(Bool) -> some View](./view/replacedisabled%28_%29.md)
  Prevents replace operations in a text editor.
### Symbol appearance
- [func symbolRenderingMode(SymbolRenderingMode?) -> some View](./view/symbolrenderingmode%28_%29.md)
  Sets the rendering mode for symbol images within this view.
- [func symbolColorRenderingMode(SymbolColorRenderingMode?) -> some View](./view/symbolcolorrenderingmode%28_%29.md)
  Sets the color rendering mode for symbol images.
- [func symbolVariableValueMode(SymbolVariableValueMode?) -> some View](./view/symbolvariablevaluemode%28_%29.md)
  Sets the variable value mode mode for symbol images within this view.
- [func symbolVariant(SymbolVariants) -> some View](./view/symbolvariant%28_%29.md)
  Makes symbols within the view show a particular variant.
### Writing Tools
- [func writingToolsAffordanceVisibility(Visibility) -> some View](./view/writingtoolsaffordancevisibility%28_%29.md)
  Specifies whether the system should show the Writing Tools affordance for text input views affected by the environment.
- [func writingToolsBehavior(WritingToolsBehavior) -> some View](./view/writingtoolsbehavior%28_%29.md)
  Specifies the Writing Tools behavior for text and text input in the environment.
- [struct WritingToolsBehavior](./writingtoolsbehavior.md)
  The Writing Tools editing experience for text and text input.

## See Also

### Configuring view elements
- [Accessibility modifiers](./view-accessibility.md)
  Make your SwiftUI apps accessible to everyone, including people with disabilities.
- [Appearance modifiers](./view-appearance.md)
  Configure a view’s foreground and background styles, controls, and visibility.
- [Auxiliary view modifiers](./view-auxiliary-views.md)
  Add and configure supporting views, like toolbars and context menus.
- [Chart view modifiers](./view-chart-view.md)
  Configure charts that you declare with Swift Charts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view-text-and-symbols)*