# Text

**Framework**: SwiftUI  
**Kind**: struct  
**Role**: Structure

A view that displays one or more lines of read-only text.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
@frozen
struct Text
```

## Mentions

- [Configuring views](./configuring-views.md)
- [Building layouts with stack views](./building-layouts-with-stack-views.md)
- [Declaring a custom view](./declaring-a-custom-view.md)
- [Laying out a simple view](./laying-out-a-simple-view.md)
- [Displaying data in lists](./displaying-data-in-lists.md)
- [Performing a search operation](./performing-a-search-operation.md)
- [Preparing views for localization](./preparing-views-for-localization.md)
- [Adding a search interface to your app](./adding-a-search-interface-to-your-app.md)
- [Grouping data with lazy stack views](./grouping-data-with-lazy-stack-views.md)
- [Populating SwiftUI menus with adaptive controls](./populating-swiftui-menus-with-adaptive-controls.md)
- [Reducing view modifier maintenance](./reducing-view-modifier-maintenance.md)
- [Suggesting search terms](./suggesting-search-terms.md)

#### Overview

A text view draws a string in your app’s user interface using a [`body`](./font/body.md) font that’s appropriate for the current platform. You can choose a different standard font, like [`title`](./font/title.md) or [`caption`](./font/caption.md), using the [`font(_:)`](./view/font%28_%29.md) view modifier.

```swift
Text("Hamlet")
    .font(.title)
```

![A text view showing the name “Hamlet” in a title](https://developer.apple.com/tutorials/images/com.apple.SwiftUI/SwiftUI-Text-title@2x.png)

If you need finer control over the styling of the text, you can use the same modifier to configure a system font or choose a custom font. You can also apply view modifiers like [`bold()`](./text/bold%28%29.md) or [`italic()`](./text/italic%28%29.md) to further adjust the formatting.

```swift
Text("by William Shakespeare")
    .font(.system(size: 12, weight: .light, design: .serif))
    .italic()
```

![A text view showing by William Shakespeare in a 12 point, light, italic,](https://developer.apple.com/tutorials/images/com.apple.SwiftUI/SwiftUI-Text-font@2x.png)

To apply styling within specific portions of the text, you can create the text view from an [`AttributedString`](../Foundation/attributedstring.md), which in turn allows you to use Markdown to style runs of text. You can mix string attributes and SwiftUI modifiers, with the string attributes taking priority.

```swift
let attributedString = try! AttributedString(
    markdown: "_Hamlet_ by William Shakespeare")

var body: some View {
    Text(attributedString)
        .font(.system(size: 12, weight: .light, design: .serif))
}
```

![A text view showing Hamlet by William Shakespeare in a 12 point, light,](https://developer.apple.com/tutorials/images/com.apple.SwiftUI/SwiftUI-Text-attributed@2x.png)

A text view always uses exactly the amount of space it needs to display its rendered contents, but you can affect the view’s layout. For example, you can use the [`frame(width:height:alignment:)`](./view/frame%28width,height,alignment%29.md) modifier to propose specific dimensions to the view. If the view accepts the proposal but the text doesn’t fit into the available space, the view uses a combination of wrapping, tightening, scaling, and truncation to make it fit. With a width of `100` points but no constraint on the height, a text view might wrap a long string:

```swift
Text("To be, or not to be, that is the question:")
    .frame(width: 100)
```

![A text view showing a quote from Hamlet split over three](https://developer.apple.com/tutorials/images/com.apple.SwiftUI/SwiftUI-Text-split@2x.png)

Use modifiers like [`lineLimit(_:)`](./view/linelimit%28_%29.md), [`allowsTightening(_:)`](./view/allowstightening%28_%29.md), [`minimumScaleFactor(_:)`](./view/minimumscalefactor%28_%29.md), and [`truncationMode(_:)`](./view/truncationmode%28_%29.md) to configure how the view handles space constraints. For example, combining a fixed width and a line limit of `1` results in truncation for text that doesn’t fit in that space:

```swift
Text("Brevity is the soul of wit.")
    .frame(width: 100)
    .lineLimit(1)
```

![A text view showing a truncated quote from Hamlet starting Brevity is t](https://developer.apple.com/tutorials/images/com.apple.SwiftUI/SwiftUI-Text-truncated@2x.png)

##### Localizing strings

If you initialize a text view with a string literal, the view uses the [`init(_:tableName:bundle:comment:)`](./text/init%28_,tablename,bundle,comment%29.md) initializer, which interprets the string as a localization key and searches for the key in the table you specify, or in the default table if you don’t specify one.

```swift
Text("pencil") // Searches the default table in the main bundle.
```

For an app localized in both English and Spanish, the above view displays “pencil” and “lápiz” for English and Spanish users, respectively. If the view can’t perform localization, it displays the key instead. For example, if the same app lacks Danish localization, the view displays “pencil” for users in that locale. Similarly, an app that lacks any localization information displays “pencil” in any locale.

To explicitly bypass localization for a string literal, use the [`init(verbatim:)`](./text/init%28verbatim%29.md) initializer.

```swift
Text(verbatim: "pencil") // Displays the string "pencil" in any locale.
```

If you initialize a text view with a variable value, the view uses the [`init(_:)`](./text/init%28_%29-9d1g4.md) initializer, which doesn’t localize the string. However, you can request localization by creating a [`LocalizedStringKey`](./localizedstringkey.md) instance first, which triggers the [`init(_:tableName:bundle:comment:)`](./text/init%28_,tablename,bundle,comment%29.md) initializer instead:

```swift
// Don't localize a string variable...
Text(writingImplement)

// ...unless you explicitly convert it to a localized string key.
Text(LocalizedStringKey(writingImplement))
```

When localizing a string variable, you can use the default table by omitting the optional initialization parameters — as in the above example — just like you might for a string literal.

When composing a complex string, where there is a need to assemble multiple pieces of text, use string interpolation:

```swift
let name: String = //…
Text("Hello, \(name)")
```

This would look up the `"Hello, %@"` localization key in the localized string file and replace the format specifier `%@` with the value of `name` before rendering the text on screen.

Using string interpolation ensures that the text in your app can be localized correctly in all locales, especially in right-to-left languages.

If you desire to style only parts of interpolated text while ensuring that the content can still be localized correctly, interpolate `Text` or [`AttributedString`](../Foundation/attributedstring.md):

```swift
let name = Text(person.name).bold()
Text("Hello, \(name)")
```

The example above uses [`appendInterpolation(_:)`](./localizedstringkey/stringinterpolation/appendinterpolation%28_%29-4qyfo.md) and will look up the `"Hello, %@"` in the localized string file and interpolate a bold text rendering the value of  `name`.

Using [`appendInterpolation(_:)`](./localizedstringkey/stringinterpolation/appendinterpolation%28_%29-5m52e.md) you can interpolate [`Image`](./image.md) in text.

## Topics

### Creating a text view
- [init(LocalizedStringKey, tableName: String?, bundle: Bundle?, comment: StaticString?)](./text/init%28_,tablename,bundle,comment%29.md)
  Creates a text view that displays localized content identified by a key.
- [init(_:)](./text/init%28_%29.md)
  Creates a text view that displays styled attributed content.
- [init(verbatim: String)](./text/init%28verbatim%29.md)
  Creates a text view that displays a string literal without localization.
- [init(Date, style: Text.DateStyle)](./text/init%28_,style%29.md)
  Creates an instance that displays localized dates and times using a specific style.
- [init(_:format:)](./text/init%28_,format%29.md)
  Creates a text view that displays the formatted representation of a nonstring type supported by a corresponding format style.
- [init(_:formatter:)](./text/init%28_,formatter%29.md)
  Creates a text view that displays the formatted representation of a Foundation object.
- [init(timerInterval: ClosedRange<Date>, pauseTime: Date?, countsDown: Bool, showsHours: Bool)](./text/init%28timerinterval,pausetime,countsdown,showshours%29.md)
  Creates an instance that displays a timer counting within the provided interval.
### Choosing a font
- [func font(Font?) -> Text](./text/font%28_%29.md)
  Sets the default font for text in the view.
- [func fontWeight(Font.Weight?) -> Text](./text/fontweight%28_%29.md)
  Sets the font weight of the text.
- [func fontDesign(Font.Design?) -> Text](./text/fontdesign%28_%29.md)
  Sets the font design of the text.
- [func fontWidth(Font.Width?) -> Text](./text/fontwidth%28_%29.md)
  Sets the font width of the text.
### Styling the view’s text
- [func foregroundStyle<S>(S) -> Text](./text/foregroundstyle%28_%29.md)
  Sets the style of the text displayed by this view.
- [func bold() -> Text](./text/bold%28%29.md)
  Applies a bold or emphasized treatment to the fonts of the text.
- [func bold(Bool) -> Text](./text/bold%28_%29.md)
  Applies a bold font weight to the text.
- [func italic() -> Text](./text/italic%28%29.md)
  Applies italics to the text.
- [func italic(Bool) -> Text](./text/italic%28_%29.md)
  Applies italics to the text.
- [func strikethrough(Bool, color: Color?) -> Text](./text/strikethrough%28_,color%29.md)
  Applies a strikethrough to the text.
- [func strikethrough(Bool, pattern: Text.LineStyle.Pattern, color: Color?) -> Text](./text/strikethrough%28_,pattern,color%29.md)
  Applies a strikethrough to the text.
- [func underline(Bool, color: Color?) -> Text](./text/underline%28_,color%29.md)
  Applies an underline to the text.
- [func underline(Bool, pattern: Text.LineStyle.Pattern, color: Color?) -> Text](./text/underline%28_,pattern,color%29.md)
  Applies an underline to the text.
- [func monospaced(Bool) -> Text](./text/monospaced%28_%29.md)
  Modifies the font of the text to use the fixed-width variant of the current font, if possible.
- [func monospacedDigit() -> Text](./text/monospaceddigit%28%29.md)
  Modifies the text view’s font to use fixed-width digits, while leaving other characters proportionally spaced.
- [func kerning(CGFloat) -> Text](./text/kerning%28_%29.md)
  Sets the spacing, or kerning, between characters.
- [func tracking(CGFloat) -> Text](./text/tracking%28_%29.md)
  Sets the tracking for the text.
- [func baselineOffset(CGFloat) -> Text](./text/baselineoffset%28_%29.md)
  Sets the vertical offset for the text relative to its baseline.
- [Text.Case](./text/case.md)
  A scheme for transforming the capitalization of characters within text.
- [struct DateStyle](./text/datestyle.md)
  A predefined style used to display a `Date`.
- [struct LineStyle](./text/linestyle.md)
  Description of the style used to draw the line for `StrikethroughStyleAttribute` and `UnderlineStyleAttribute`.
- [func foregroundColor(Color?) -> Text](./text/foregroundcolor%28_%29.md)
  Sets the color of the text displayed by this view.
### Fitting text into available space
- [func textScale(Text.Scale, isEnabled: Bool) -> Text](./text/textscale%28_,isenabled%29.md)
  Applies a text scale to the text.
- [struct Scale](./text/scale.md)
  Defines text scales
- [Text.TruncationMode](./text/truncationmode.md)
  The type of truncation to apply to a line of text when it’s too long to fit in the available space.
### Localizing text
- [func typesettingLanguage(_:isEnabled:)](./text/typesettinglanguage%28_,isenabled%29.md)
  Specifies the language for typesetting.
### Configuring voiceover
- [func speechAdjustedPitch(Double) -> Text](./text/speechadjustedpitch%28_%29.md)
  Raises or lowers the pitch of spoken text.
- [func speechAlwaysIncludesPunctuation(Bool) -> Text](./text/speechalwaysincludespunctuation%28_%29.md)
  Sets whether VoiceOver should always speak all punctuation in the text view.
- [func speechAnnouncementsQueued(Bool) -> Text](./text/speechannouncementsqueued%28_%29.md)
  Controls whether to queue pending announcements behind existing speech rather than interrupting speech in progress.
- [func speechSpellsOutCharacters(Bool) -> Text](./text/speechspellsoutcharacters%28_%29.md)
  Sets whether VoiceOver should speak the contents of the text view character by character.
### Providing accessibility information
- [func accessibilityHeading(AccessibilityHeadingLevel) -> Text](./text/accessibilityheading%28_%29.md)
  Sets the accessibility level of this heading.
- [func accessibilityLabel(_:)](./text/accessibilitylabel%28_%29.md)
  Adds a label to the view that describes its contents.
- [func accessibilityTextContentType(AccessibilityTextContentType) -> Text](./text/accessibilitytextcontenttype%28_%29.md)
  Sets an accessibility text content type.
### Combining text views
- [static func + (Text, Text) -> Text](./text/plus%28_,_%29.md)
  Concatenates the text in two text views in a new text view.
### Structures
- [struct AlignmentStrategy](./text/alignmentstrategy.md)
  The way SwiftUI infers the appropriate text alignment if no value is explicitly provided.
- [struct Layout](./text/layout.md)
  A value describing the layout and custom attributes of a tree of `Text` views.
- [struct LayoutKey](./text/layoutkey.md)
  A preference key that provides the `Text.Layout` values for all text views in the queried subtree.
- [struct WritingDirectionStrategy](./text/writingdirectionstrategy.md)
  The way SwiftUI infers the appropriate writing direction if no value is explicitly provided.
### Instance Methods
- [func customAttribute<T>(T) -> Text](./text/customattribute%28_%29.md)
  Adds a custom attribute to the text view.
- [func textVariant<V>(V) -> some View](./text/textvariant%28_%29.md)
  Controls the way text size variants are chosen.

## Relationships

### Conforms To
- [Copyable](../Swift/copyable.md)
- [Equatable](../Swift/equatable.md)
- [Escapable](../Swift/escapable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [View](./view.md)

## See Also

### Displaying text
- [struct Label](./label.md)
  A standard label for user interface items, consisting of an icon with a title.
- [func labelStyle<S>(S) -> some View](./view/labelstyle%28_%29.md)
  Sets the style for labels within this view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/text)*