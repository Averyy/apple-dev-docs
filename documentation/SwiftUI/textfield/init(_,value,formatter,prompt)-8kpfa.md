# init(_:value:formatter:prompt:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a text field that applies a formatter to a bound value, with a label generated from a localized title string.

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
init<V>(_ titleKey: LocalizedStringKey, value: Binding<V>, formatter: Formatter, prompt: Text?)
```

Available when `Label` is `Text`.

**Other overloads**:

```swift
@export(implementation)
nonisolated init<V>(_ titleResource: LocalizedStringResource, value: Binding<V>, formatter: Formatter, prompt: Text?)
```

```swift
nonisolated
init<S, V>(_ title: S, value: Binding<V>, formatter: Formatter, prompt: Text?) where S : StringProtocol
```

## Discussion

Use this initializer to create a text field that binds to a bound value, using a [`Formatter`](../../Foundation/formatter.md) to convert to and from this type. Changes to the bound value update the string displayed by the text field. Editing the text field updates the bound value, as long as the formatter can parse the text. If the format style can’t parse the input, the bound value remains unchanged.

Use the [`onSubmit(of:_:)`](../view/onsubmit%28of,_%29.md) modifier to invoke an action whenever the user submits this text field.

The following example uses a [`Double`](../../Swift/double.md) as the bound value, and a [`NumberFormatter`](../../Foundation/numberformatter.md) instance to convert to and from a string representation. The formatter uses the [`NumberFormatter.Style.decimal`](../../Foundation/numberformatter/style/decimal.md) style, to allow entering a fractional part. As the user types, the bound value updates, which in turn updates three [`Text`](../text.md) views that use different format styles. If the user enters text that doesn’t represent a valid `Double`, the bound value doesn’t update.

```swift
@State private var myDouble: Double = 0.673
@State private var numberFormatter: NumberFormatter = {
    var nf = NumberFormatter()
    nf.numberStyle = .decimal
    return nf
}()

var body: some View {
    VStack {
        TextField(
            "Double",
            value: $myDouble,
            formatter: numberFormatter
        )
        Text(myDouble, format: .number)
        Text(myDouble, format: .number.precision(.significantDigits(5)))
        Text(myDouble, format: .number.notation(.scientific))
    }
}
```

## Parameters

- `titleKey`: The key for the localized title of the text field, describing its purpose.
- `value`: The underlying value to edit.
- `formatter`: A formatter to use when converting between the string the user edits and the underlying value of type `V`. If `formatter` can’t perform the conversion, the text field doesn’t modify `binding.value`.
- `prompt`: A `Text` which provides users with guidance on what to enter into the text field.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/textfield/init(_:value:formatter:prompt:)-8kpfa)*