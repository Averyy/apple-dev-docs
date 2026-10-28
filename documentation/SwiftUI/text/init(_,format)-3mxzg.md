# init(_:format:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a text view that displays the formatted representation of a nonstring type supported by a corresponding format style.

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
init<F>(_ input: F.FormatInput, format: F) where F : FormatStyle, F.FormatInput : Equatable, F.FormatOutput == String
```

**Other overloads**:

```swift
init<F>(_ input: F.FormatInput, format: F) where F : FormatStyle, F.FormatInput : Equatable, F.FormatOutput == AttributedString
```

```swift
init<V, F>(_ source: TimeDataSource<V>, format: F) where V == F.FormatInput, F : DiscreteFormatStyle, F.FormatOutput == AttributedString
```

```swift
init<V, F>(_ source: TimeDataSource<V>, format: F) where V == F.FormatInput, F : DiscreteFormatStyle, F.FormatOutput == String
```

## Discussion

Use this initializer to create a text view backed by a nonstring value, using a [`FormatStyle`](../../Foundation/formatstyle.md) to convert the type to a string representation. Any changes to the value update the string displayed by the text view.

In the following example, three [`Text`](../text.md) views present a date with different combinations of date and time fields, by using different [`Date.FormatStyle`](../../Foundation/date/formatstyle.md) options.

```swift
@State private var myDate = Date()
var body: some View {
    VStack {
        Text(myDate, format: Date.FormatStyle(date: .numeric, time: .omitted))
        Text(myDate, format: Date.FormatStyle(date: .complete, time: .complete))
        Text(myDate, format: Date.FormatStyle().hour(.defaultDigitsNoAMPM).minute())
    }
}
```

![Three vertically stacked text views showing the date with different](https://developer.apple.com/tutorials/images/com.apple.SwiftUI/Text-init-format-1@2x.png)

## Parameters

- `input`: The underlying value to display.
- `format`: A format style of type `F` to convert the underlying value of type `F.FormatInput` to a string representation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/text/init(_:format:)-3mxzg)*