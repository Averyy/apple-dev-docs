# Text

**Framework**: SwiftUI  
**Kind**: struct

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

- [Configuring views](configuring-views.md)
- [Laying out a simple view](laying-out-a-simple-view.md)
- [Declaring a custom view](declaring-a-custom-view.md)
- [Building layouts with stack views](building-layouts-with-stack-views.md)
- [Displaying data in lists](displaying-data-in-lists.md)
- [Preparing views for localization](preparing-views-for-localization.md)
- [Performing a search operation](performing-a-search-operation.md)
- [Reducing view modifier maintenance](reducing-view-modifier-maintenance.md)
- [Adding a search interface to your app](adding-a-search-interface-to-your-app.md)
- [Populating SwiftUI menus with adaptive controls](populating-swiftui-menus-with-adaptive-controls.md)
- [Grouping data with lazy stack views](grouping-data-with-lazy-stack-views.md)
- [Suggesting search terms](suggesting-search-terms.md)

#### Overview

A text view draws a string in your app’s user interface using a [`body`](font/body.md) font that’s appropriate for the current platform. You can choose a different standard font, like [`title`](font/title.md) or [`caption`](font/caption.md), using the [`font(_:)`](view/font(_:).md) view modifier.

```swift
Text("Hamlet")
    .font(.title)
```

![A text view showing the name “Hamlet” in a title](https://docs-assets.developer.apple.com/published/43b5a30d2c1d2176fe1cc88aa2c567ac/SwiftUI-Text-title%402x.png)

If you need finer control over the styling of the text, you can use the same modifier to configure a system font or choose a custom font. You can also apply view modifiers like [`bold()`](text/bold().md) or [`italic()`](text/italic().md) to further adjust the formatting.

```swift
Text("by William Shakespeare")
    .font(.system(size: 12, weight: .light, design: .serif))
    .italic()
```

![A text view showing by William Shakespeare in a 12 point, light, italic,](https://docs-assets.developer.apple.com/published/c6398423bafcaae5f2c2daccf3057e5e/SwiftUI-Text-font%402x.png)

To apply styling within specific portions of the text, you can create the text view from an [`AttributedString`](https://developer.apple.com/documentation/Foundation/AttributedString), which in turn allows you to use Markdown to style runs of text. You can mix string attributes and SwiftUI modifiers, with the string attributes taking priority.

```swift
let attributedString = try! AttributedString(
    markdown: "_Hamlet_ by William Shakespeare")

var body: some View {
    Text(attributedString)
        .font(.system(size: 12, weight: .light, design: .serif))
}
```

![A text view showing Hamlet by William Shakespeare in a 12 point, light,](https://docs-assets.developer.apple.com/published/ddb3ef16d3bec75a55f66268a153531b/SwiftUI-Text-attributed%402x.png)

A text view always uses exactly the amount of space it needs to display its rendered contents, but you can affect the view’s layout. For example, you can use the [`frame(width:height:alignment:)`](view/frame(width:height:alignment:).md) modifier to propose specific dimensions to the view. If the view accepts the proposal but the text doesn’t fit into the available space, the view uses a combination of wrapping, tightening, scaling, and truncation to make it fit. With a width of `100` points but no constraint on the height, a text view might wrap a long string:

```swift
Text("To be, or not to be, that is the question:")
    .frame(width: 100)
```

![A text view showing a quote from Hamlet split over three](https://docs-assets.developer.apple.com/published/122fc95483e6058c08280430279ba688/SwiftUI-Text-split%402x.png)

Use modifiers like [`lineLimit(_:)`](view/linelimit(_:).md), [`allowsTightening(_:)`](view/allowstightening(_:).md), [`minimumScaleFactor(_:)`](view/minimumscalefactor(_:).md), and [`truncationMode(_:)`](view/truncationmode(_:).md) to configure how the view handles space constraints. For example, combining a fixed width and a line limit of `1` results in truncation for text that doesn’t fit in that space:

```swift
Text("Brevity is the soul of wit.")
    .frame(width: 100)
    .lineLimit(1)
```

![A text view showing a truncated quote from Hamlet starting Brevity is t](https://docs-assets.developer.apple.com/published/d0f08188d0c13dc6fba6acb532579cf8/SwiftUI-Text-truncated%402x.png)

##### Localizing Strings

If you initialize a text view with a string literal, the view uses the [`init(_:tableName:bundle:comment:)`](text/init(_:tablename:bundle:comment:).md) initializer, which interprets the string as a localization key and searches for the key in the table you specify, or in the default table if you don’t specify one.

```swift
Text("pencil") // Searches the default table in the main bundle.
```

For an app localized in both English and Spanish, the above view displays “pencil” and “lápiz” for English and Spanish users, respectively. If the view can’t perform localization, it displays the key instead. For example, if the same app lacks Danish localization, the view displays “pencil” for users in that locale. Similarly, an app that lacks any localization information displays “pencil” in any locale.

To explicitly bypass localization for a string literal, use the [`init(verbatim:)`](text/init(verbatim:).md) initializer.

```swift
Text(verbatim: "pencil") // Displays the string "pencil" in any locale.
```

If you initialize a text view with a variable value, the view uses the [`init(_:)`](text/init(_:)-9d1g4.md) initializer, which doesn’t localize the string. However, you can request localization by creating a [`LocalizedStringKey`](localizedstringkey.md) instance first, which triggers the [`init(_:tableName:bundle:comment:)`](text/init(_:tablename:bundle:comment:).md) initializer instead:

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

If you desire to style only parts of interpolated text while ensuring that the content can still be localized correctly, interpolate `Text` or [`AttributedString`](https://developer.apple.com/documentation/Foundation/AttributedString):

```swift
let name = Text(person.name).bold()
Text("Hello, \(name)")
```

The example above uses [`appendInterpolation(_:)`](localizedstringkey/stringinterpolation/appendinterpolation(_:)-4qyfo.md) and will look up the `"Hello, %@"` in the localized string file and interpolate a bold text rendering the value of  `name`.

Using [`appendInterpolation(_:)`](localizedstringkey/stringinterpolation/appendinterpolation(_:)-5m52e.md) you can interpolate [`Image`](image.md) in text.

## Topics

### Creating a text view
- [init(LocalizedStringKey, tableName: String?, bundle: Bundle?, comment: StaticString?)](text/init(_:tablename:bundle:comment:).md)
  Creates a text view that displays localized content identified by a key.
- [init(_:)](text/init(_:).md)
  Creates a text view that displays styled attributed content.
- [init(verbatim: String)](text/init(verbatim:).md)
  Creates a text view that displays a string literal without localization.
- [init(Date, style: Text.DateStyle)](text/init(_:style:).md)
  Creates an instance that displays localized dates and times using a specific style.
- [init(_:format:)](text/init(_:format:).md)
  Creates a text view that displays the formatted representation of a nonstring type supported by a corresponding format style.
- [init(_:formatter:)](text/init(_:formatter:).md)
  Creates a text view that displays the formatted representation of a Foundation object.
- [init(timerInterval: ClosedRange<Date>, pauseTime: Date?, countsDown: Bool, showsHours: Bool)](text/init(timerinterval:pausetime:countsdown:showshours:).md)
  Creates an instance that displays a timer counting within the provided interval.
### Choosing a font
- [func font(Font?) -> Text](text/font(_:).md)
  Sets the default font for text in the view.
- [func fontWeight(Font.Weight?) -> Text](text/fontweight(_:).md)
  Sets the font weight of the text.
- [func fontDesign(Font.Design?) -> Text](text/fontdesign(_:).md)
  Sets the font design of the text.
- [func fontWidth(Font.Width?) -> Text](text/fontwidth(_:).md)
  Sets the font width of the text.
### Styling the view’s text
- [func foregroundStyle<S>(S) -> Text](text/foregroundstyle(_:).md)
  Sets the style of the text displayed by this view.
- [func bold() -> Text](text/bold.md)
  Applies a bold or emphasized treatment to the fonts of the text.
- [func bold(Bool) -> Text](text/bold(_:).md)
  Applies a bold font weight to the text.
- [func italic() -> Text](text/italic.md)
  Applies italics to the text.
- [func italic(Bool) -> Text](text/italic(_:).md)
  Applies italics to the text.
- [func strikethrough(Bool, color: Color?) -> Text](text/strikethrough(_:color:).md)
  Applies a strikethrough to the text.
- [func strikethrough(Bool, pattern: Text.LineStyle.Pattern, color: Color?) -> Text](text/strikethrough(_:pattern:color:).md)
  Applies a strikethrough to the text.
- [func underline(Bool, color: Color?) -> Text](text/underline(_:color:).md)
  Applies an underline to the text.
- [func underline(Bool, pattern: Text.LineStyle.Pattern, color: Color?) -> Text](text/underline(_:pattern:color:).md)
  Applies an underline to the text.
- [func monospaced(Bool) -> Text](text/monospaced(_:).md)
  Modifies the font of the text to use the fixed-width variant of the current font, if possible.
- [func monospacedDigit() -> Text](text/monospaceddigit.md)
  Modifies the text view’s font to use fixed-width digits, while leaving other characters proportionally spaced.
- [func kerning(CGFloat) -> Text](text/kerning(_:).md)
  Sets the spacing, or kerning, between characters.
- [func tracking(CGFloat) -> Text](text/tracking(_:).md)
  Sets the tracking for the text.
- [func baselineOffset(CGFloat) -> Text](text/baselineoffset(_:).md)
  Sets the vertical offset for the text relative to its baseline.
- [Text.Case](text/case.md)
  A scheme for transforming the capitalization of characters within text.
- [struct DateStyle](text/datestyle.md)
  A predefined style used to display a `Date`.
- [struct LineStyle](text/linestyle.md)
  Description of the style used to draw the line for `StrikethroughStyleAttribute` and `UnderlineStyleAttribute`.
### Fitting text into available space
- [func textScale(Text.Scale, isEnabled: Bool) -> Text](text/textscale(_:isenabled:).md)
  Applies a text scale to the text.
- [struct Scale](text/scale.md)
  Defines text scales
- [Text.TruncationMode](text/truncationmode.md)
  The type of truncation to apply to a line of text when it’s too long to fit in the available space.
### Localizing text
- [func typesettingLanguage(_:isEnabled:)](text/typesettinglanguage(_:isenabled:).md)
  Specifies the language for typesetting.
### Configuring voiceover
- [func speechAdjustedPitch(Double) -> Text](text/speechadjustedpitch(_:).md)
  Raises or lowers the pitch of spoken text.
- [func speechAlwaysIncludesPunctuation(Bool) -> Text](text/speechalwaysincludespunctuation(_:).md)
  Sets whether VoiceOver should always speak all punctuation in the text view.
- [func speechAnnouncementsQueued(Bool) -> Text](text/speechannouncementsqueued(_:).md)
  Controls whether to queue pending announcements behind existing speech rather than interrupting speech in progress.
- [func speechSpellsOutCharacters(Bool) -> Text](text/speechspellsoutcharacters(_:).md)
  Sets whether VoiceOver should speak the contents of the text view character by character.
### Providing accessibility information
- [func accessibilityHeading(AccessibilityHeadingLevel) -> Text](text/accessibilityheading(_:).md)
  Sets the accessibility level of this heading.
- [func accessibilityLabel(_:)](text/accessibilitylabel(_:).md)
  Adds a label to the view that describes its contents.
- [func accessibilityTextContentType(AccessibilityTextContentType) -> Text](text/accessibilitytextcontenttype(_:).md)
  Sets an accessibility text content type.
### Combining text views
- [static func + (Text, Text) -> Text](text/+(_:_:).md)
  Concatenates the text in two text views in a new text view.
### Deprecated symbols
- [func foregroundColor(Color?) -> Text](text/foregroundcolor(_:).md)
  Sets the color of the text displayed by this view.
### Structures
- [struct AlignmentStrategy](text/alignmentstrategy.md)
  The way SwiftUI infers the appropriate text alignment if no value is explicitly provided.
- [struct Layout](text/layout.md)
  A value describing the layout and custom attributes of a tree of `Text` views.
- [struct LayoutKey](text/layoutkey.md)
  A preference key that provides the `Text.Layout` values for all text views in the queried subtree.
- [struct WritingDirectionStrategy](text/writingdirectionstrategy.md)
  The way SwiftUI infers the appropriate writing direction if no value is explicitly provided.
### Instance Methods
- [func customAttribute<T>(T) -> Text](text/customattribute(_:).md)
  Adds a custom attribute to the text view.
- [func textVariant<V>(V) -> some View](text/textvariant(_:).md)
  Controls the way text size variants are chosen.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [View](view.md)

## See Also

- [struct Label](label.md)
  A standard label for user interface items, consisting of an icon with a title.
- [func labelStyle<S>(S) -> some View](view/labelstyle(_:).md)
  Sets the style for labels within this view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/text)*