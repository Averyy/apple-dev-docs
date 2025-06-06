# LocalizedStringKey.StringInterpolation

**Framework**: SwiftUI  
**Kind**: struct

Represents the contents of a string literal with interpolations while it’s being built, for use in creating a localized string key.

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
struct StringInterpolation
```

## Topics

### Appending to an interpolation
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
- [func appendLiteral(String)](localizedstringkey/stringinterpolation/appendliteral(_:).md)
  Appends a literal string.
### Instance Methods
- [func appendInterpolation(accessibilityName: Color)](localizedstringkey/stringinterpolation/appendinterpolation(accessibilityname:).md)
  Appends a localized description of a color for accessibility to a string interpolation.

## Relationships

### Conforms To
- [StringInterpolationProtocol](../Swift/StringInterpolationProtocol.md)

## See Also

- [init(stringInterpolation: LocalizedStringKey.StringInterpolation)](localizedstringkey/init(stringinterpolation:).md)
  Creates a localized string key from the given string interpolation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/localizedstringkey/stringinterpolation)*