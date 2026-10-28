# appendInterpolation(_:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Appends an attributed substring to a string interpolation.

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
@export(implementation)
mutating func appendInterpolation(_ attributedSubstring: AttributedSubstring)
```

**Other overloads**:

```swift
@export(implementation)
mutating func appendInterpolation(_ substring: Substring)
```

```swift
mutating func appendInterpolation(_ attributedString: AttributedString)
```

```swift
mutating func appendInterpolation(_ dates: ClosedRange<Date>)
```

```swift
mutating func appendInterpolation(_ image: Image)
```

```swift
mutating func appendInterpolation(_ interval: DateInterval)
```

```swift
mutating func appendInterpolation(_ resource: LocalizedStringResource)
```

```swift
mutating func appendInterpolation(_ string: String)
```

```swift
mutating func appendInterpolation(_ text: Text)
```

```swift
mutating func appendInterpolation<T>(_ value: T) where T : _FormatSpecifiable
```

```swift
@export(implementation)
mutating func appendInterpolation<T>(_ object: T)
```

## Discussion

Don’t call this method directly; it’s used by the compiler when interpreting string interpolations.

The following example shows how to use a string interpolation to format an [`AttributedSubstring`](../../../Foundation/attributedsubstring.md) and append it to static text. The resulting interpolation implicitly creates a [`LocalizedStringKey`](../../localizedstringkey.md), which a [`Text`](../../text.md) view uses to provide its content.

```swift
struct ContentView: View {

    var identificationNumberSuffix: AttributedSubstring {
        // …
    }

    var body: some View {
        Text("Identification: •••• •••• \(identificationNumberSuffix)!")
    }
}
```

For this example, assume that the app runs on a device set to a Russian locale, and has the following entry in a Russian-localized `Localizable.strings` file:

```swift
"Identification: •••• •••• %@" = "Идентификация: •••• •••• %@";
```

The attributed string `identificationNumberSuffix` replaces the format specifier `%@`,  maintaining its color attributes, when the [`Text`](../../text.md) view renders its contents:

## Parameters

- `attributedSubstring`: The attributed substring to append.

## See Also

### Appending to an interpolation
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
- [func appendLiteral(String)](./appendliteral%28_%29.md)
  Appends a literal string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/localizedstringkey/stringinterpolation/appendinterpolation(_:))*