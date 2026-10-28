# appendInterpolation(_:formatter:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Appends an optionally-formatted instance of an Objective-C subclass to a string interpolation.

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
mutating func appendInterpolation<Subject>(_ subject: Subject, formatter: Formatter? = nil) where Subject : NSObject
```

**Other overloads**:

```swift
mutating func appendInterpolation<Subject>(_ subject: Subject, formatter: Formatter? = nil) where Subject : ReferenceConvertible
```

## Discussion

Don’t call this method directly; it’s used by the compiler when interpreting string interpolations.

The following example shows how to use a [`Measurement`](../../../Foundation/measurement.md) value and a [`MeasurementFormatter`](../../../Foundation/measurementformatter.md) to create a [`LocalizedStringKey`](../../localizedstringkey.md) that uses the formatter style [`Formatter.UnitStyle.long`](../../../Foundation/formatter/unitstyle/long.md) when generating the measurement’s string representation. Rather than calling `appendInterpolation(_:formatter)` directly, the code gets the formatting behavior implicitly by using the `\()` string interpolation syntax.

```swift
let siResistance = Measurement(value: 640, unit: UnitElectricResistance.ohms)
let formatter = MeasurementFormatter()
formatter.unitStyle = .long
let key = LocalizedStringKey ("Resistance: \(siResistance, formatter: formatter)")
let text1 = Text(key) // Text contains "Resistance: 640 ohms"
```

## Parameters

- `subject`: An [`NSObject`](../../../ObjectiveC/nsobject-swift.class.md) to append.
- `formatter`: A formatter to convert `subject` to a string representation.

## See Also

### Appending to an interpolation
- [func appendInterpolation(_:)](./appendinterpolation%28_%29.md)
  Appends an attributed substring to a string interpolation.
- [func appendInterpolation<T>(T, specifier: String)](./appendinterpolation%28_,specifier%29.md)
  Appends a type, convertible to a string with a format specifier, to a string interpolation.
- [func appendInterpolation(_:format:)](./appendinterpolation%28_,format%29.md)
  Appends the formatted representation  of a nonstring type supported by a corresponding format style.
- [func appendInterpolation(Date, style: Text.DateStyle)](./appendinterpolation%28_,style%29.md)
  Appends a formatted date to a string interpolation.
- [func appendInterpolation(timerInterval: ClosedRange<Date>, pauseTime: Date?, countsDown: Bool, showsHours: Bool)](./appendinterpolation%28timerinterval,pausetime,countsdown,showshours%29.md)
  Appends a timer interval to a string interpolation.
- [func appendLiteral(String)](./appendliteral%28_%29.md)
  Appends a literal string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/localizedstringkey/stringinterpolation/appendinterpolation(_:formatter:))*