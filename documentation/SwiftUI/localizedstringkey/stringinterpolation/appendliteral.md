# appendLiteral(_:)

**Framework**: SwiftUI  
**Kind**: method

Appends a literal string.

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
mutating func appendLiteral(_ literal: String)
```

#### Discussion

Don’t call this method directly; it’s used by the compiler when interpreting string interpolations.

## Parameters

- `literal`: The literal string to append.

## See Also

- [func appendInterpolation(_:)](localizedstringkey/stringinterpolation/appendinterpolation(_:).md)
  Appends an attributed string to a string interpolation.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/localizedstringkey/stringinterpolation/appendliteral(_:))*