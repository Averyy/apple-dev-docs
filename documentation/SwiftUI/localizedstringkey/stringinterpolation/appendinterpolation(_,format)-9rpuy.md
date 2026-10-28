# appendInterpolation(_:format:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Appends the formatted representation  of a nonstring type supported by a corresponding format style.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
mutating func appendInterpolation<F>(_ input: F.FormatInput, format: F) where F : FormatStyle, F.FormatInput : Equatable, F.FormatOutput == String
```

**Other overloads**:

```swift
mutating func appendInterpolation<F>(_ input: F.FormatInput, format: F) where F : FormatStyle, F.FormatInput : Equatable, F.FormatOutput == AttributedString
```

```swift
mutating func appendInterpolation<V, F>(_ source: TimeDataSource<V>, format: F) where V == F.FormatInput, F : DiscreteFormatStyle, F.FormatOutput == AttributedString
```

```swift
mutating func appendInterpolation<V, F>(_ source: TimeDataSource<V>, format: F) where V == F.FormatInput, F : DiscreteFormatStyle, F.FormatOutput == String
```

## Discussion

Don’t call this method directly; it’s used by the compiler when interpreting string interpolations.

The following example shows how to use a string interpolation to format a [`Date`](../../../Foundation/date.md) with a [`Date.FormatStyle`](../../../Foundation/date/formatstyle.md) and append it to static text. The resulting interpolation implicitly creates a [`LocalizedStringKey`](../../localizedstringkey.md), which a [`Text`](../../text.md) uses to provide its content.

```swift
Text("The time is \(myDate, format: Date.FormatStyle(date: .omitted, time:.complete))")
```

## Parameters

- `input`: The instance to format and append.
- `format`: A format style to use when converting `input` into a string representation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/localizedstringkey/stringinterpolation/appendinterpolation(_:format:)-9rpuy)*