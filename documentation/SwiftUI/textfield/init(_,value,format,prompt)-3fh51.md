# init(_:value:format:prompt:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a text field that applies a format style to a bound value, with a label generated from a localized title string.

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
init<F>(_ titleKey: LocalizedStringKey, value: Binding<F.FormatInput>, format: F, prompt: Text? = nil) where F : ParseableFormatStyle, F.FormatOutput == String
```

Available when `Label` is `Text`.

**Other overloads**:

```swift
@export(implementation)
nonisolated init<F>(_ titleResource: LocalizedStringResource, value: Binding<F.FormatInput>, format: F, prompt: Text? = nil) where F : ParseableFormatStyle, F.FormatOutput == String
```

```swift
@export(implementation)
nonisolated init<F>(_ titleResource: LocalizedStringResource, value: Binding<F.FormatInput?>, format: F, prompt: Text? = nil) where F : ParseableFormatStyle, F.FormatOutput == String
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

Use this initializer to create a text field that binds to a bound value, using a [`ParseableFormatStyle`](../../Foundation/parseableformatstyle.md) to convert to and from this type. Changes to the bound value update the string displayed by the text field. Editing the text field updates the bound value, as long as the format style can parse the text. If the format style can’t parse the input, the bound value remains unchanged.

Use the [`onSubmit(of:_:)`](../view/onsubmit%28of,_%29.md) modifier to invoke an action whenever the user submits this text field.

The following example uses a [`Double`](../../Swift/double.md) as the bound value, and a [`FloatingPointFormatStyle`](../../Foundation/floatingpointformatstyle.md) instance to convert to and from a string representation. As the user types, the bound value updates, which in turn updates three [`Text`](../text.md) views that use different format styles. If the user enters text that doesn’t represent a valid `Double`, the bound value doesn’t update.

```swift
@State private var myDouble: Double = 0.673
var body: some View {
    VStack {
        TextField(
            "Double",
            value: $myDouble,
            format: .number
        )
        Text(myDouble, format: .number)
        Text(myDouble, format: .number.precision(.significantDigits(5)))
        Text(myDouble, format: .number.notation(.scientific))
    }
}
```

![A text field with the string 0.673. Below this, three text views](https://developer.apple.com/tutorials/images/com.apple.SwiftUI/TextField-init-format-1@2x.png)

## Parameters

- `titleKey`: The title of the text field, describing its purpose.
- `value`: The underlying value to edit.
- `format`: A format style of type `F` to use when converting between the string the user edits and the underlying value of type `F.FormatInput`. If `format` can’t perform the conversion, the text field leaves `binding.value` unchanged. If the user stops editing the text in an invalid state, the text field updates the field’s text to the last known valid value.
- `prompt`: A `Text` which provides users with guidance on what to type into the text field.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/textfield/init(_:value:format:prompt:)-3fh51)*