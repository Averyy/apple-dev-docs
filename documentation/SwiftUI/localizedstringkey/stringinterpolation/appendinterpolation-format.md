# appendInterpolation(_:format:)

**Framework**: SwiftUI  
**Kind**: method

Appends the formatted representation  of a nonstring type supported by a corresponding format style.

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
mutating func appendInterpolation<F>(_ input: F.FormatInput, format: F) where F : FormatStyle, F.FormatInput : Equatable, F.FormatOutput == AttributedString
```

#### Discussion

Don’t call this method directly; it’s used by the compiler when interpreting string interpolations.

The following example shows how to use a string interpolation to format a [`Date`](https://developer.apple.com/documentation/Foundation/Date) with a [`Date.FormatStyle`](https://developer.apple.com/documentation/Foundation/Date/FormatStyle) and append it to static text. The resulting interpolation implicitly creates a [`LocalizedStringKey`](localizedstringkey.md), which a [`Text`](text.md) uses to provide its content.

```swift
Text("The time is \(myDate, format: Date.FormatStyle(date: .omitted, time:.complete).attributedStyle)")
```

## Parameters

- `input`: The instance to format and append.
- `format`: A format style to use when converting   into an attributed   string representation.

## See Also

- [func appendInterpolation(_:)](localizedstringkey/stringinterpolation/appendinterpolation(_:).md)
  Appends an attributed string to a string interpolation.
- [func appendInterpolation<T>(T, specifier: String)](localizedstringkey/stringinterpolation/appendinterpolation(_:specifier:).md)
  Appends a type, convertible to a string with a format specifier, to a string interpolation.
- [func appendInterpolation(_:formatter:)](localizedstringkey/stringinterpolation/appendinterpolation(_:formatter:).md)
  Appends an optionally-formatted instance of an Objective-C subclass to a string interpolation.
- [func appendInterpolation(Date, style: Text.DateStyle)](localizedstringkey/stringinterpolation/appendinterpolation(_:style:).md)
  Appends a formatted date to a string interpolation.
- [func appendInterpolation(timerInterval: ClosedRange<Date>, pauseTime: Date?, countsDown: Bool, showsHours: Bool)](localizedstringkey/stringinterpolation/appendinterpolation(timerinterval:pausetime:countsdown:showshours:).md)
  Appends a timer interval to a string interpolation.
- [func appendLiteral(String)](localizedstringkey/stringinterpolation/appendliteral(_:).md)
  Appends a literal string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/localizedstringkey/stringinterpolation/appendinterpolation(_:format:))*