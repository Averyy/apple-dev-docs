# init(_:value:format:prompt:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a text field that applies a format style to a bound optional value, with a label generated from a localized title string resource.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
@export(implementation)
nonisolated init<F>(_ titleResource: LocalizedStringResource, value: Binding<F.FormatInput?>, format: F, prompt: Text? = nil) where F : ParseableFormatStyle, F.FormatOutput == String
```

Available when `Label` is `Text`.

**Other overloads**:

```swift
@export(implementation)
nonisolated init<F>(_ titleResource: LocalizedStringResource, value: Binding<F.FormatInput>, format: F, prompt: Text? = nil) where F : ParseableFormatStyle, F.FormatOutput == String
```

```swift
nonisolated
init<F>(_ titleKey: LocalizedStringKey, value: Binding<F.FormatInput>, format: F, prompt: Text? = nil) where F : ParseableFormatStyle, F.FormatOutput == String
```

```swift
nonisolated
init<F>(_ titleKey: LocalizedStringKey, value: Binding<F.FormatInput?>, format: F, prompt: Text? = nil) where F : ParseableFormatStyle, F.FormatOutput == String
```

```swift
nonisolated
init<S, F>(_ title: S, value: Binding<F.FormatInput>, format: F, prompt: Text? = nil) where S : StringProtocol, F : ParseableFormatStyle, F.FormatOutput == String
```

```swift
nonisolated
init<S, F>(_ title: S, value: Binding<F.FormatInput?>, format: F, prompt: Text? = nil) where S : StringProtocol, F : ParseableFormatStyle, F.FormatOutput == String
```

## Discussion

Use this initializer to create a text field that binds to a bound optional value, using a [`ParseableFormatStyle`](../../Foundation/parseableformatstyle.md) to convert to and from this type. Changes to the bound value update the string displayed by the text field. Editing the text field updates the bound value, as long as the format style can parse the text. If the format style can’t parse the input, the text field sets the bound value to `nil`.

Use the [`onSubmit(of:_:)`](../view/onsubmit%28of,_%29.md) modifier to invoke an action whenever the user submits this text field.

The following example uses an optional [`Double`](../../Swift/double.md) as the bound currency value, and a [`FloatingPointFormatStyle.Currency`](../../Foundation/floatingpointformatstyle/currency.md) instance to convert to and from a representation as U.S. dollars. As the user types, a `View.onChange(of:_:)` modifier logs the new value to the console. If the user enters an invalid currency value, like letters or emoji, the console output is `Optional(nil)`.

```swift
@State private var myMoney: Double? = 300.0
var body: some View {
    TextField(
        "Currency (USD)",
        value: $myMoney,
        format: .currency(code: "USD")
    )
    .onChange(of: myMoney) { newValue in
        print ("myMoney: \(newValue)")
    }
}
```

## Parameters

- `titleResource`: The title of the text field, describing its purpose.
- `value`: The underlying value to edit.
- `format`: A format style of type `F` to use when converting between the string the user edits and the underlying value of type `F.FormatInput`. If `format` can’t perform the conversion, the text field sets `binding.value` to `nil`.
- `prompt`: A `Text` which provides users with guidance on what to type into the text field.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/textfield/init(_:value:format:prompt:)-75nzx)*