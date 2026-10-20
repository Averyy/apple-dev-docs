# LocalizedStringKey.StringInterpolation

**Framework**: SwiftUI  
**Kind**: struct  
**Role**: Structure

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
- [func appendInterpolation(_:)](./stringinterpolation/appendinterpolation%28_%29.md)
  Appends an attributed substring to a string interpolation.
- [func appendInterpolation<T>(T, specifier: String)](./stringinterpolation/appendinterpolation%28_,specifier%29.md)
  Appends a type, convertible to a string with a format specifier, to a string interpolation.
- [func appendInterpolation(_:format:)](./stringinterpolation/appendinterpolation%28_,format%29.md)
  Appends the formatted representation  of a nonstring type supported by a corresponding format style.
- [func appendInterpolation(_:formatter:)](./stringinterpolation/appendinterpolation%28_,formatter%29.md)
  Appends an optionally-formatted instance of an Objective-C subclass to a string interpolation.
- [func appendInterpolation(Date, style: Text.DateStyle)](./stringinterpolation/appendinterpolation%28_,style%29.md)
  Appends a formatted date to a string interpolation.
- [func appendInterpolation(timerInterval: ClosedRange<Date>, pauseTime: Date?, countsDown: Bool, showsHours: Bool)](./stringinterpolation/appendinterpolation%28timerinterval,pausetime,countsdown,showshours%29.md)
  Appends a timer interval to a string interpolation.
- [func appendLiteral(String)](./stringinterpolation/appendliteral%28_%29.md)
  Appends a literal string.
### Instance Methods
- [func appendInterpolation(accessibilityName: Color)](./stringinterpolation/appendinterpolation%28accessibilityname%29.md)
  Appends a localized description of a color for accessibility to a string interpolation.

## Relationships

### Conforms To
- [StringInterpolationProtocol](../../Swift/stringinterpolationprotocol.md)

## See Also

### Creating a key from an interpolation
- [init(stringInterpolation: LocalizedStringKey.StringInterpolation)](./init%28stringinterpolation%29.md)
  Creates a localized string key from the given string interpolation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/localizedstringkey/stringinterpolation)*