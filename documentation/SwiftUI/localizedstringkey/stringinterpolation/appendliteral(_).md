# appendLiteral(_:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

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

### Appending to an interpolation
- [func appendInterpolation(_:)](./appendinterpolation%28_%29.md)
  Appends an attributed substring to a string interpolation.
- [func appendInterpolation<T>(T, specifier: String)](./appendinterpolation%28_,specifier%29.md)
  Appends a type, convertible to a string with a format specifier, to a string interpolation.
- [func appendInterpolation(_:format:)](./appendinterpolation%28_,format%29.md)
  Appends the formatted representation  of a nonstring type supported by a corresponding format style.
- [func appendInterpolation(_:formatter:)](./appendinterpolation%28_,formatter%29.md)
  Appends an optionally-formatted instance of an Objective-C subclass to a string interpolation.
- [func appendInterpolation(Date, style: Text.DateStyle)](./appendinterpolation%28_,style%29.md)
  Appends a formatted date to a string interpolation.
- [func appendInterpolation(timerInterval: ClosedRange<Date>, pauseTime: Date?, countsDown: Bool, showsHours: Bool)](./appendinterpolation%28timerinterval,pausetime,countsdown,showshours%29.md)
  Appends a timer interval to a string interpolation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/localizedstringkey/stringinterpolation/appendliteral(_:))*