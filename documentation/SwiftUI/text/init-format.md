# init(_:format:)

**Framework**: SwiftUI  
**Kind**: init

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

#### Discussion

Use this initializer to create a text view backed by a nonstring value, using a [`FormatStyle`](https://developer.apple.com/documentation/Foundation/FormatStyle) to convert the type to an attributed string representation. Any changes to the value update the string displayed by the text view.

In the following example, three [`Text`](text.md) views present a date with different combinations of date and time fields, by using different [`Date.FormatStyle`](https://developer.apple.com/documentation/Foundation/Date/FormatStyle) options.

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

![Three vertically stacked text views showing the date with different](https://docs-assets.developer.apple.com/published/3cbfd7e712f6d26122350b67f0db9862/Text-init-format-1%402x.png)

## Parameters

- `input`: The underlying value to display.
- `format`: A format style of type   to convert the underlying value   of type   to an attributed string representation.

## See Also

- [init(LocalizedStringKey, tableName: String?, bundle: Bundle?, comment: StaticString?)](text/init(_:tablename:bundle:comment:).md)
  Creates a text view that displays localized content identified by a key.
- [init(_:)](text/init(_:).md)
  Creates a text view that displays styled attributed content.
- [init(verbatim: String)](text/init(verbatim:).md)
  Creates a text view that displays a string literal without localization.
- [init(Date, style: Text.DateStyle)](text/init(_:style:).md)
  Creates an instance that displays localized dates and times using a specific style.
- [init(_:formatter:)](text/init(_:formatter:).md)
  Creates a text view that displays the formatted representation of a Foundation object.
- [init(timerInterval: ClosedRange<Date>, pauseTime: Date?, countsDown: Bool, showsHours: Bool)](text/init(timerinterval:pausetime:countsdown:showshours:).md)
  Creates an instance that displays a timer counting within the provided interval.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/text/init(_:format:))*