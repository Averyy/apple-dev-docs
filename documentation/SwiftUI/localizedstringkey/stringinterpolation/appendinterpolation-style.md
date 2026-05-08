# appendInterpolation(_:style:)

**Framework**: SwiftUI  
**Kind**: method

Appends a formatted date to a string interpolation.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
mutating func appendInterpolation(_ date: Date, style: Text.DateStyle)
```

#### Discussion

Don’t call this method directly; it’s used by the compiler when interpreting string interpolations.

## Parameters

- `date`: The date to append.
- `style`: A predefined style to format the date with.

## See Also

- [func appendInterpolation(_:)](localizedstringkey/stringinterpolation/appendinterpolation(_:).md)
  Appends an attributed string to a string interpolation.
- [func appendInterpolation<T>(T, specifier: String)](localizedstringkey/stringinterpolation/appendinterpolation(_:specifier:).md)
  Appends a type, convertible to a string with a format specifier, to a string interpolation.
- [func appendInterpolation(_:format:)](localizedstringkey/stringinterpolation/appendinterpolation(_:format:).md)
  Appends the formatted representation  of a nonstring type supported by a corresponding format style.
- [func appendInterpolation(_:formatter:)](localizedstringkey/stringinterpolation/appendinterpolation(_:formatter:).md)
  Appends an optionally-formatted instance of an Objective-C subclass to a string interpolation.
- [func appendInterpolation(timerInterval: ClosedRange<Date>, pauseTime: Date?, countsDown: Bool, showsHours: Bool)](localizedstringkey/stringinterpolation/appendinterpolation(timerinterval:pausetime:countsdown:showshours:).md)
  Appends a timer interval to a string interpolation.
- [func appendLiteral(String)](localizedstringkey/stringinterpolation/appendliteral(_:).md)
  Appends a literal string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/localizedstringkey/stringinterpolation/appendinterpolation(_:style:))*