# appendInterpolation(timerInterval:pauseTime:countsDown:showsHours:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Appends a timer interval to a string interpolation.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
mutating func appendInterpolation(timerInterval: ClosedRange<Date>, pauseTime: Date? = nil, countsDown: Bool = true, showsHours: Bool = true)
```

#### Discussion

Don’t call this method directly; it’s used by the compiler when interpreting string interpolations.

## Parameters

- `timerInterval`: The interval between where to run the timer.
- `pauseTime`: If present, the date at which to pause the timer. The default is `nil` which indicates to never pause.
- `countsDown`: Whether to count up or down. The default is `true`.
- `showsHours`: Whether to include an hours component if there are more than 60 minutes left on the timer. The default is `true`.

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
- [func appendLiteral(String)](./appendliteral%28_%29.md)
  Appends a literal string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/localizedstringkey/stringinterpolation/appendinterpolation(timerinterval:pausetime:countsdown:showshours:))*