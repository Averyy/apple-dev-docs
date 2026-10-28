# appendInterpolation(_:format:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Appends a text view that displays the current system time as defined by the given format style, keeping the text up to date as time progresses.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
mutating func appendInterpolation<V, F>(_ source: TimeDataSource<V>, format: F) where V == F.FormatInput, F : DiscreteFormatStyle, F.FormatOutput == AttributedString
```

**Other overloads**:

```swift
mutating func appendInterpolation<F>(_ input: F.FormatInput, format: F) where F : FormatStyle, F.FormatInput : Equatable, F.FormatOutput == AttributedString
```

```swift
mutating func appendInterpolation<F>(_ input: F.FormatInput, format: F) where F : FormatStyle, F.FormatInput : Equatable, F.FormatOutput == String
```

```swift
mutating func appendInterpolation<V, F>(_ source: TimeDataSource<V>, format: F) where V == F.FormatInput, F : DiscreteFormatStyle, F.FormatOutput == String
```

## Discussion

Use this initializer to create a text view that updates as time progresses, just like `init(_:style:)`, but with the flexibility of Foundation’s `FormatStyle` protocol.

In the following example, the first [`Text`](../../text.md) view presents the offset to `startDate`, whereas the second view displays a stopwatch counting from `startDate`. Both views are kept up to date as time progresses.

```swift
Text(.currentDate, format: .offset(to: startDate))
Text(.currentDate, format: .stopwatch(startingAt: startDate))
```

> **Note**: Don’t call this method directly; it’s used by the compiler when interpreting string interpolations.

## Redaction for Reduced Luminance

When the text is displayed with reduced luminance and frame rate, it automatically modifies the `format` or its output so it never shows outdated information.

If the `format` is known to SwiftUI and allows removing units or fields, SwiftUI removes parts that change more frequently than the frame rate allows. E.g. a string like *13 minutes, 22 seconds* would change to just `13 minutes`.

Otherwise, SwiftUI inspects the `durationField`, `dateField`, and `measurement` attributes on the formatted output to determine which ranges need to be redacted. If these attributes are not present, all digits are redacted using dashes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/localizedstringkey/stringinterpolation/appendinterpolation(_:format:)-8a4n4)*