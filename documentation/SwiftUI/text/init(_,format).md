# init(_:format:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a text view that displays the formatted representation of a nonstring type supported by a corresponding format style.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
init<F>(_ input: F.FormatInput, format: F) where F : FormatStyle, F.FormatInput : Equatable, F.FormatOutput == AttributedString
```

**Other overloads**:

```swift
init<F>(_ input: F.FormatInput, format: F) where F : FormatStyle, F.FormatInput : Equatable, F.FormatOutput == String
```

```swift
init<V, F>(_ source: TimeDataSource<V>, format: F) where V == F.FormatInput, F : DiscreteFormatStyle, F.FormatOutput == AttributedString
```

```swift
init<V, F>(_ source: TimeDataSource<V>, format: F) where V == F.FormatInput, F : DiscreteFormatStyle, F.FormatOutput == String
```

## Discussion

Use this initializer to create a text view backed by a nonstring value, using a [`FormatStyle`](../../Foundation/formatstyle.md) to convert the type to an attributed string representation. Any changes to the value update the string displayed by the text view.

In the following example, three [`Text`](../text.md) views present a date with different combinations of date and time fields, by using different [`Date.FormatStyle`](../../Foundation/date/formatstyle.md) options.

```swift
@State private var myDate = Date()
var body: some View {
    VStack {
        Text(myDate, format: Date.FormatStyle(date: .numeric, time: .omitted).attributedStyle)
        Text(myDate, format: Date.FormatStyle(date: .complete, time: .complete).attributedStyle)
        Text(myDate, format: Date.FormatStyle().hour(.defaultDigitsNoAMPM).minute().attributedStyle)
    }
}
```

![Three vertically stacked text views showing the date with different](https://developer.apple.com/tutorials/images/com.apple.SwiftUI/Text-init-format-1@2x.png)

## Parameters

- `input`: The underlying value to display.
- `format`: A format style of type `F` to convert the underlying value of type `F.FormatInput` to an attributed string representation.

## See Also

### Creating a text view
- [init(LocalizedStringKey, tableName: String?, bundle: Bundle?, comment: StaticString?)](./init%28_,tablename,bundle,comment%29.md)
  Creates a text view that displays localized content identified by a key.
- [init(_:)](./init%28_%29.md)
  Creates a text view that displays styled attributed content.
- [init(verbatim: String)](./init%28verbatim%29.md)
  Creates a text view that displays a string literal without localization.
- [init(Date, style: Text.DateStyle)](./init%28_,style%29.md)
  Creates an instance that displays localized dates and times using a specific style.
- [init(_:formatter:)](./init%28_,formatter%29.md)
  Creates a text view that displays the formatted representation of a Foundation object.
- [init(timerInterval: ClosedRange<Date>, pauseTime: Date?, countsDown: Bool, showsHours: Bool)](./init%28timerinterval,pausetime,countsdown,showshours%29.md)
  Creates an instance that displays a timer counting within the provided interval.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/text/init(_:format:))*