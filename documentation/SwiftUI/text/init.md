# init(_:)

**Framework**: SwiftUI  
**Kind**: init

Creates a text view that displays styled attributed content.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
init(_ attributedContent: AttributedString)
```

#### Discussion

Use this initializer to style text according to attributes found in the specified [`AttributedString`](https://developer.apple.com/documentation/Foundation/AttributedString). Attributes in the attributed string take precedence over styles added by view modifiers. For example, the attributed text in the following example appears in blue, despite the use of the [`foregroundColor(_:)`](view/foregroundcolor(_:).md) modifier to use red throughout the enclosing [`VStack`](vstack.md):

```swift
var content: AttributedString {
    var attributedString = AttributedString("Blue text")
    attributedString.foregroundColor = .blue
    return attributedString
}

var body: some View {
    VStack {
        Text(content)
        Text("Red text")
    }
    .foregroundColor(.red)
}
```

![A vertical stack of two text views, the top labeled Blue Text with a](https://docs-assets.developer.apple.com/published/0e75f9a9c2cd81bdb1086e94efdc2417/SwiftUI-Text-init-attributed%402x.png)

SwiftUI combines text attributes with SwiftUI modifiers whenever possible. For example, the following listing creates text that is both bold and red:

```swift
var content: AttributedString {
    var content = AttributedString("Some text")
    content.inlinePresentationIntent = .stronglyEmphasized
    return content
}

var body: some View {
    Text(content).foregroundColor(Color.red)
}
```

A SwiftUI [`Text`](text.md) view renders most of the styles defined by the Foundation attribute [`inlinePresentationIntent`](https://developer.apple.com/documentation/foundation/attributescopes/foundationattributes/3796123-inlinepresentationintent), like the [`stronglyEmphasized`](https://developer.apple.com/documentation/foundation/inlinepresentationintent/3746899-stronglyemphasized) value, which SwiftUI presents as bold text.

> ❗ **Important**: [`Text`](text.md) uses only a subset of the attributes defined in [`AttributeScopes.FoundationAttributes`](https://developer.apple.com/documentation/Foundation/AttributeScopes/FoundationAttributes). `Text` renders all [`InlinePresentationIntent`](https://developer.apple.com/documentation/Foundation/InlinePresentationIntent) attributes except for [`lineBreak`](https://developer.apple.com/documentation/foundation/inlinepresentationintent/3787563-linebreak) and [`softBreak`](https://developer.apple.com/documentation/foundation/inlinepresentationintent/3787564-softbreak). It also renders the [`link`](https://developer.apple.com/documentation/foundation/attributescopes/foundationattributes/3764633-link) attribute as a clickable link. `Text` ignores any other Foundation-defined attributes in an attributed string.

[`Text`](text.md) uses only a subset of the attributes defined in [`AttributeScopes.FoundationAttributes`](https://developer.apple.com/documentation/Foundation/AttributeScopes/FoundationAttributes). `Text` renders all [`InlinePresentationIntent`](https://developer.apple.com/documentation/Foundation/InlinePresentationIntent) attributes except for [`lineBreak`](https://developer.apple.com/documentation/foundation/inlinepresentationintent/3787563-linebreak) and [`softBreak`](https://developer.apple.com/documentation/foundation/inlinepresentationintent/3787564-softbreak). It also renders the [`link`](https://developer.apple.com/documentation/foundation/attributescopes/foundationattributes/3764633-link) attribute as a clickable link. `Text` ignores any other Foundation-defined attributes in an attributed string.

SwiftUI also defines additional attributes in the attribute scope [`AttributeScopes.SwiftUIAttributes`](https://developer.apple.com/documentation/Foundation/AttributeScopes/SwiftUIAttributes) which you can access from an attributed string’s [`swiftUI`](https://developer.apple.com/documentation/foundation/attributescopes/3788543-swiftui) property. SwiftUI attributes take precedence over equivalent attributes from other frameworks, such as [`AttributeScopes.UIKitAttributes`](https://developer.apple.com/documentation/Foundation/AttributeScopes/UIKitAttributes) and [`AttributeScopes.AppKitAttributes`](https://developer.apple.com/documentation/Foundation/AttributeScopes/AppKitAttributes).

You can create an `AttributedString` with Markdown syntax, which allows you to style distinct runs within a `Text` view:

```swift
let content = try! AttributedString(
    markdown: "**Thank You!** Please visit our [website](http://example.com).")

var body: some View {
    Text(content)
}
```

The `**` syntax around “Thank You!” applies an [`inlinePresentationIntent`](https://developer.apple.com/documentation/foundation/attributescopes/foundationattributes/3796123-inlinepresentationintent) attribute with the value [`stronglyEmphasized`](https://developer.apple.com/documentation/foundation/inlinepresentationintent/3746899-stronglyemphasized). SwiftUI renders this as bold text, as described earlier. The link syntax around “website” creates a [`link`](https://developer.apple.com/documentation/foundation/attributescopes/foundationattributes/3764633-link) attribute, which `Text` styles to indicate it’s a link; by default, clicking or tapping the link opens the linked URL in the user’s default browser. Alternatively, you can perform custom link handling by putting an [`OpenURLAction`](openurlaction.md) in the text view’s environment.

![A text view that says Thank you. Please visit our website. The text](https://docs-assets.developer.apple.com/published/e5680bbca5ad5a5f2779dea53103d8ca/SwiftUI-Text-init-markdown%402x.png)

You can also use Markdown syntax in localized string keys, which means you can write the above example without needing to explicitly create an `AttributedString`:

```swift
var body: some View {
    Text("**Thank You!** Please visit our [website](https://example.com).")
}
```

In your app’s strings files, use Markdown syntax to apply styling to the app’s localized strings. You also use this approach when you want to perform automatic grammar agreement on localized strings, with the `^[text](inflect:true)` syntax.

For details about Markdown syntax support in SwiftUI, see [`init(_:tableName:bundle:comment:)`](text/init(_:tablename:bundle:comment:).md).

## Parameters

- `attributedContent`: An attributed string to style and display,   in accordance with its attributes.

## See Also

- [init(LocalizedStringKey, tableName: String?, bundle: Bundle?, comment: StaticString?)](text/init(_:tablename:bundle:comment:).md)
  Creates a text view that displays localized content identified by a key.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/text/init(_:))*