# appendInterpolation(_:)

**Framework**: SwiftUI  
**Kind**: method

Appends an attributed string to a string interpolation.

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
mutating func appendInterpolation(_ attributedString: AttributedString)
```

#### Discussion

Don’t call this method directly; it’s used by the compiler when interpreting string interpolations.

The following example shows how to use a string interpolation to format an [`AttributedString`](https://developer.apple.com/documentation/Foundation/AttributedString) and append it to static text. The resulting interpolation implicitly creates a [`LocalizedStringKey`](localizedstringkey.md), which a [`Text`](text.md) view uses to provide its content.

```swift
struct ContentView: View {

    var nextDate: AttributedString {
        var result = Calendar.current
            .nextWeekend(startingAfter: Date.now)!
            .start
            .formatted(
                .dateTime
                .month(.wide)
                .day()
                .attributed
            )
        result.backgroundColor = .green
        result.foregroundColor = .white
        return result
    }

    var body: some View {
        Text("Our next catch-up is on \(nextDate)!")
    }
}
```

For this example, assume that the app runs on a device set to a Russian locale, and has the following entry in a Russian-localized `Localizable.strings` file:

```swift
"Our next catch-up is on %@!" = "Наша следующая встреча состоится %@!";
```

The attributed string `nextDate` replaces the format specifier `%@`,  maintaining its color and date-formatting attributes, when the [`Text`](text.md) view renders its contents:

![A text view with Russian text, ending with a date that uses white](https://docs-assets.developer.apple.com/published/68c95cae63ea252ddb42d0cfdba106dd/LocalizedStringKey-AttributedString-Russian%402x.png)

## Parameters

- `attributedString`: The attributed string to append.

## See Also

- [func appendInterpolation<T>(T, specifier: String)](localizedstringkey/stringinterpolation/appendinterpolation(_:specifier:).md)
  Appends a type, convertible to a string with a format specifier, to a string interpolation.
- [func appendInterpolation(_:format:)](localizedstringkey/stringinterpolation/appendinterpolation(_:format:).md)
  Appends the formatted representation  of a nonstring type supported by a corresponding format style.
- [func appendInterpolation(_:formatter:)](localizedstringkey/stringinterpolation/appendinterpolation(_:formatter:).md)
  Appends an optionally-formatted instance of an Objective-C subclass to a string interpolation.
- [func appendInterpolation(Date, style: Text.DateStyle)](localizedstringkey/stringinterpolation/appendinterpolation(_:style:).md)
  Appends a formatted date to a string interpolation.
- [func appendInterpolation(timerInterval: ClosedRange<Date>, pauseTime: Date?, countsDown: Bool, showsHours: Bool)](localizedstringkey/stringinterpolation/appendinterpolation(timerinterval:pausetime:countsdown:showshours:).md)
  Appends a timer interval to a string interpolation.
- [func appendLiteral(String)](localizedstringkey/stringinterpolation/appendliteral(_:).md)
  Appends a literal string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/localizedstringkey/stringinterpolation/appendinterpolation(_:))*