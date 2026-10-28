# init(value:format:prompt:label:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a text field that applies a format style to a bound optional value, with a label generated from a content builder.

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
nonisolated
init<F>(value: Binding<F.FormatInput?>, format: F, prompt: Text? = nil, @ContentBuilder label: () -> Label) where F : ParseableFormatStyle, F.FormatOutput == String
```

Available when `Label` conforms to `View`.

**Other overloads**:

```swift
nonisolated
init<F>(value: Binding<F.FormatInput>, format: F, prompt: Text? = nil, @ContentBuilder label: () -> Label) where F : ParseableFormatStyle, F.FormatOutput == String
```

## Discussion

Use this initializer to create a text field that binds to a bound optional value, using a [`ParseableFormatStyle`](../../Foundation/parseableformatstyle.md) to convert to and from this type. Changes to the bound value update the string displayed by the text field. Editing the text field updates the bound value, as long as the format style can parse the text. If the format style can’t parse the input, the text field sets the bound value to `nil`.

Use the [`onSubmit(of:_:)`](../view/onsubmit%28of,_%29.md) modifier to invoke an action whenever the user submits this text field.

The following example uses an optional [`Double`](../../Swift/double.md) as the bound currency value, and a [`FloatingPointFormatStyle.Currency`](../../Foundation/floatingpointformatstyle/currency.md) instance to convert to and from a representation as U.S. dollars. As the user types, a `View.onChange(of:_:)` modifier logs the new value to the console. If the user enters an invalid currency value, like letters or emoji, the console output is `Optional(nil)`.

```swift
@State private var myMoney: Double? = 300.0
var body: some View {
    TextField(
        value: $myMoney,
        format: .currency(code: "USD")
    ) {
        Text("Currency (USD)")
    }
    .onChange(of: myMoney) { newValue in
        print ("myMoney: \(newValue)")
    }
}
```

## Parameters

- `value`: The underlying value to edit.
- `format`: A format style of type `F` to use when converting between the string the user edits and the underlying value of type `F.FormatInput`. If `format` can’t perform the conversion, the text field sets `binding.value` to `nil`.
- `prompt`: A `Text` which provides users with guidance on what to type into the text field.
- `label`: A content builder that produces a label for the text field, describing its purpose.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/textfield/init(value:format:prompt:label:)-5325h)*