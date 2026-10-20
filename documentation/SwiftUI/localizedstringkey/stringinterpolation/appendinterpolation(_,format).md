# appendInterpolation(_:format:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

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

**Other overloads**:

```swift
mutating func appendInterpolation<F>(_ input: F.FormatInput, format: F) where F : FormatStyle, F.FormatInput : Equatable, F.FormatOutput == String
```

```swift
mutating func appendInterpolation<V, F>(_ source: TimeDataSource<V>, format: F) where V == F.FormatInput, F : DiscreteFormatStyle, F.FormatOutput == AttributedString
```

```swift
mutating func appendInterpolation<V, F>(_ source: TimeDataSource<V>, format: F) where V == F.FormatInput, F : DiscreteFormatStyle, F.FormatOutput == String
```

#### Discussion

Don’t call this method directly; it’s used by the compiler when interpreting string interpolations.

The following example shows how to use a string interpolation to format a [`Date`](../../../Foundation/date.md) with a [`Date.FormatStyle`](../../../Foundation/date/formatstyle.md) and append it to static text. The resulting interpolation implicitly creates a [`LocalizedStringKey`](../../localizedstringkey.md), which a [`Text`](../../text.md) uses to provide its content.

```swift
Text("The time is \(myDate, format: Date.FormatStyle(date: .omitted, time:.complete).attributedStyle)")
```

## Parameters

- `input`: The instance to format and append.
- `format`: A format style to use when converting `input` into an attributed string representation.

## See Also

### Appending to an interpolation
- [func appendInterpolation(_:)](./appendinterpolation%28_%29.md)
  Appends an attributed substring to a string interpolation.
- [func appendInterpolation<T>(T, specifier: String)](./appendinterpolation%28_,specifier%29.md)
  Appends a type, convertible to a string with a format specifier, to a string interpolation.
- [func appendInterpolation(_:formatter:)](./appendinterpolation%28_,formatter%29.md)
  Appends an optionally-formatted instance of an Objective-C subclass to a string interpolation.
- [func appendInterpolation(Date, style: Text.DateStyle)](./appendinterpolation%28_,style%29.md)
  Appends a formatted date to a string interpolation.
- [func appendInterpolation(timerInterval: ClosedRange<Date>, pauseTime: Date?, countsDown: Bool, showsHours: Bool)](./appendinterpolation%28timerinterval,pausetime,countsdown,showshours%29.md)
  Appends a timer interval to a string interpolation.
- [func appendLiteral(String)](./appendliteral%28_%29.md)
  Appends a literal string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/localizedstringkey/stringinterpolation/appendinterpolation(_:format:))*