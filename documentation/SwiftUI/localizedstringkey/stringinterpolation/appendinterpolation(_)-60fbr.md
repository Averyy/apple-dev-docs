# appendInterpolation(_:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Appends an attributed string to a string interpolation.

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
mutating func appendInterpolation(_ attributedString: AttributedString)
```

**Other overloads**:

```swift
@export(implementation)
mutating func appendInterpolation(_ attributedSubstring: AttributedSubstring)
```

```swift
@export(implementation)
mutating func appendInterpolation(_ substring: Substring)
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

The following example shows how to use a string interpolation to format an [`AttributedString`](../../../Foundation/attributedstring.md) and append it to static text. The resulting interpolation implicitly creates a [`LocalizedStringKey`](../../localizedstringkey.md), which a [`Text`](../../text.md) view uses to provide its content.

```swift
struct ContentView: View {

    var nextDate: AttributedString {
        var result = Calendar.current
            .nextWeekend(startingAfter: Date.now)!
            .start
            .formatted(
                .dateTime
                .month(.wide)
                .day()
                .attributed
            )
        result.backgroundColor = .green
        result.foregroundColor = .white
        return result
    }

    var body: some View {
        Text("Our next catch-up is on \(nextDate)!")
    }
}
```

For this example, assume that the app runs on a device set to a Russian locale, and has the following entry in a Russian-localized `Localizable.strings` file:

```swift
"Our next catch-up is on %@!" = "Наша следующая встреча состоится %@!";
```

The attributed string `nextDate` replaces the format specifier `%@`,  maintaining its color and date-formatting attributes, when the [`Text`](../../text.md) view renders its contents:

![A text view with Russian text, ending with a date that uses white](https://developer.apple.com/tutorials/images/com.apple.SwiftUI/LocalizedStringKey-AttributedString-Russian@2x.png)

## Parameters

- `attributedString`: The attributed string to append.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/localizedstringkey/stringinterpolation/appendinterpolation(_:)-60fbr)*