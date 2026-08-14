# appendInterpolation(_:specifier:)

**Framework**: SwiftUI  
**Kind**: method

Appends a type, convertible to a string with a format specifier, to a string interpolation.

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
mutating func appendInterpolation<T>(_ value: T, specifier: String) where T : _FormatSpecifiable
```

#### Discussion

Don’t call this method directly; it’s used by the compiler when interpreting string interpolations.

## Parameters

- `value`: The value to append.
- `specifier`: A format specifier to convert `subject` to a string representation, like `%f` for a [`Double`](https://developer.apple.com/documentation/swift/double), or `%x` to create a hexidecimal representation of a [`UInt32`](https://developer.apple.com/documentation/swift/uint32). For a list of available specifier strings, see [`String Format Specifers`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFStrings/formatSpecifiers.html#//apple_ref/doc/uid/TP40004265).

## See Also

- [func appendInterpolation(_:)](localizedstringkey/stringinterpolation/appendinterpolation(_:).md)
  Appends an attributed substring to a string interpolation.
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

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/localizedstringkey/stringinterpolation/appendinterpolation(_:specifier:))*