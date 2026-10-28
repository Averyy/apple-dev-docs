# init(_:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

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

**Other overloads**:

```swift
init(_ dates: ClosedRange<Date>)
```

```swift
init(_ image: Image)
```

```swift
init(_ interval: DateInterval)
```

```swift
init(_ resource: LocalizedStringResource)
```

```swift
init<S>(_ content: S) where S : StringProtocol
```

### Format text by combining attributes and view modifiers

Use this initializer to style text according to attributes found in the specified [`AttributedString`](../../Foundation/attributedstring.md). Attributes in the attributed string take precedence over styles added by view modifiers. For example, the attributed text in the following example appears in blue, despite the use of the [`foregroundColor(_:)`](../view/foregroundcolor%28_%29.md) modifier to use red throughout the enclosing [`VStack`](../vstack.md):

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

![A vertical stack of two text views, the top labeled Blue Text with a](https://developer.apple.com/tutorials/images/com.apple.SwiftUI/SwiftUI-Text-init-attributed@2x.png)

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

### Supported Foundation attributes

A SwiftUI [`Text`](../text.md) view renders most of the styles defined by the Foundation attribute [`inlinePresentationIntent`](../../Foundation/attributescopes/foundationattributes/inlinepresentationintent.md), like the [`stronglyEmphasized`](../../Foundation/inlinepresentationintent/stronglyemphasized.md) value, which SwiftUI presents as bold text.

> ❗ **Important**: [`Text`](../text.md) uses only a subset of the attributes defined in [`AttributeScopes.FoundationAttributes`](../../Foundation/attributescopes/foundationattributes.md). `Text` renders all [`InlinePresentationIntent`](../../Foundation/inlinepresentationintent.md) attributes except for [`lineBreak`](../../Foundation/inlinepresentationintent/linebreak.md) and [`softBreak`](../../Foundation/inlinepresentationintent/softbreak.md). It also respects [`writingDirection`](../../Foundation/attributescopes/foundationattributes/writingdirection.md) and renders the [`link`](../../Foundation/attributescopes/foundationattributes/link.md) attribute as a clickable link. `Text` ignores any other Foundation-defined attributes in an attributed string.

### SwiftUI attributes

SwiftUI also defines additional attributes in the attribute scope [`AttributeScopes.SwiftUIAttributes`](../../Foundation/attributescopes/swiftuiattributes.md) which you can access from an attributed string’s [`swiftUI`](../../Foundation/attributescopes/swiftui.md) property. SwiftUI attributes take precedence over equivalent attributes from other frameworks, such as [`AttributeScopes.UIKitAttributes`](../../Foundation/attributescopes/uikitattributes.md) and [`AttributeScopes.AppKitAttributes`](../../Foundation/attributescopes/appkitattributes.md).

### Markdown support

You can create an `AttributedString` with Markdown syntax, which allows you to style distinct runs within a `Text` view:

```swift
let content = try! AttributedString(
    markdown: "**Thank You!** Please visit our [website](http://example.com).")

var body: some View {
    Text(content)
}
```

The `**` syntax around “Thank You!” applies an [`inlinePresentationIntent`](../../Foundation/attributescopes/foundationattributes/inlinepresentationintent.md) attribute with the value [`stronglyEmphasized`](../../Foundation/inlinepresentationintent/stronglyemphasized.md). SwiftUI renders this as bold text, as described earlier. The link syntax around “website” creates a [`link`](../../Foundation/attributescopes/foundationattributes/link.md) attribute, which `Text` styles to indicate it’s a link; by default, clicking or tapping the link opens the linked URL in the user’s default browser. Alternatively, you can perform custom link handling by putting an [`OpenURLAction`](../openurlaction.md) in the text view’s environment.

![A text view that says Thank you. Please visit our website. The text](https://developer.apple.com/tutorials/images/com.apple.SwiftUI/SwiftUI-Text-init-markdown@2x.png)

You can also use Markdown syntax in localized string keys, which means you can write the above example without needing to explicitly create an `AttributedString`:

```swift
var body: some View {
    Text("**Thank You!** Please visit our [website](https://example.com).")
}
```

In your app’s strings files, use Markdown syntax to apply styling to the app’s localized strings. You also use this approach when you want to perform automatic grammar agreement on localized strings, with the `^[text](inflect:true)` syntax.

For details about Markdown syntax support in SwiftUI, see [`init(_:tableName:bundle:comment:)`](./init%28_,tablename,bundle,comment%29.md).

### Applying a custom text formatting definition

Use the [`attributedTextFormattingDefinition(_:)`](../view/attributedtextformattingdefinition%28_%29-81jn6.md) modifier to apply a custom [`AttributedTextFormattingDefinition`](../attributedtextformattingdefinition.md) to text created using this initializer. This will result in the text only applying attributes in the definition’s attribute scope and constraining attributes according to the definition’s value constraints prior to display.

Custom attributes listed in the definition’s [`Scope`](../attributedtextformattingdefinition/scope.md), where the [`Value`](../../Foundation/attributedstringkey/value.md) conforms to the [`TextAttribute`](../textattribute.md) protocol, can be read when observing the text’s layout using `Text/Layout/Run/subscript(key:)->T?`, just as text attributes applied using the [`customAttribute(_:)`](./customattribute%28_%29.md) modifier.

## Parameters

- `attributedContent`: An attributed string to style and display, in accordance with its attributes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/text/init(_:)-1a4oh)*