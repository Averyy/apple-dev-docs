# init(_:value:formatter:)

**Framework**: SwiftUI  
**Kind**: init

Create an instance which binds over an arbitrary type, `V`.

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
nonisolated
init<S, V>(_ title: S, value: Binding<V>, formatter: Formatter) where S : StringProtocol
```

#### Discussion

Use this initializer to create a text field that binds to a bound optional value, using a [`Formatter`](https://developer.apple.com/documentation/Foundation/Formatter) to convert to and from this type. Changes to the bound value update the string displayed by the text field. Editing the text field updates the bound value, as long as the formatter can parse the text. If the format style can’t parse the input, the bound value remains unchanged.

Use the [`onSubmit(of:_:)`](view/onsubmit(of:_:).md) modifier to invoke an action whenever the user submits this text field.

The following example uses a [`Double`](https://developer.apple.com/documentation/Swift/Double) as the bound value, and a [`NumberFormatter`](https://developer.apple.com/documentation/Foundation/NumberFormatter) instance to convert to and from a string representation. The formatter uses the [`NumberFormatter.Style.decimal`](https://developer.apple.com/documentation/Foundation/NumberFormatter/Style/decimal) style, to allow entering a fractional part. As the user types, the bound value updates, which in turn updates three [`Text`](text.md) views that use different format styles. If the user enters text that doesn’t represent a valid `Double`, the bound value doesn’t update.

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
            value: $myDouble,
            formatter: numberFormatter
        ) {
            Text("Double")
        }
        Text(myDouble, format: .number)
        Text(myDouble, format: .number.precision(.significantDigits(5)))
        Text(myDouble, format: .number.notation(.scientific))
    }
}
```

## Parameters

- `title`: The title of the text view, describing its purpose.
- `value`: The underlying value to edit.
- `formatter`: A formatter to use when converting between the   string the user edits and the underlying value of type  .   If   can’t perform the conversion, the text field doesn’t   modify  .

## See Also

- [init(_:value:format:prompt:)](textfield/init(_:value:format:prompt:).md)
  Creates a text field that applies a format style to a bound value, with a label generated from a localized title string.
- [init(value:format:prompt:label:)](textfield/init(value:format:prompt:label:).md)
  Creates a text field that applies a format style to a bound value, with a label generated from a view builder.
- [init(_:value:formatter:prompt:)](textfield/init(_:value:formatter:prompt:).md)
  Creates a text field that applies a formatter to a bound value, with a label generated from a title string.
- [init<V>(value: Binding<V>, formatter: Formatter, prompt: Text?, label: () -> Label)](textfield/init(value:formatter:prompt:label:).md)
  Creates a text field that applies a formatter to a bound optional value, with a label generated from a view builder.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/textfield/init(_:value:formatter:))*