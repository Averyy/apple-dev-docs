# init(_:format:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a text view that displays the current system time as defined by the given format style, keeping the text up to date as time progresses.

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
init<V, F>(_ source: TimeDataSource<V>, format: F) where V == F.FormatInput, F : DiscreteFormatStyle, F.FormatOutput == String
```

**Other overloads**:

```swift
init<F>(_ input: F.FormatInput, format: F) where F : FormatStyle, F.FormatInput : Equatable, F.FormatOutput == AttributedString
```

```swift
init<F>(_ input: F.FormatInput, format: F) where F : FormatStyle, F.FormatInput : Equatable, F.FormatOutput == String
```

```swift
init<V, F>(_ source: TimeDataSource<V>, format: F) where V == F.FormatInput, F : DiscreteFormatStyle, F.FormatOutput == AttributedString
```

## Discussion

Use this initializer to create a text view that updates as time progresses, just like [`init(_:style:)`](./init%28_,style%29.md), but with the flexibility of Foundation’s `FormatStyle` protocol.

In the following example, the first [`Text`](../text.md) view presents the current date and time, whereas the second view displays a soccer clock counting from `startDate`. Both views are kept up to date as time progresses.

```swift
Text(.currentDate, format: .dateTime)
Text(.durationOffset(to: startDate), format: .time(pattern: .minuteSecond))
```

## Redaction for Reduced Luminance

When the text is displayed with reduced luminance and frame rate, it automatically modifies the `format` or its output so it never shows outdated information.

If the `format` is known to SwiftUI and allows removing units or fields, SwiftUI removes parts that change more frequently than the frame rate allows. E.g. a string like *13 minutes, 22 seconds* would change to just `13 minutes`.

Otherwise, all digits in the formatted output are redacted using dashes.

> **Note**: In a widget, this `Text` becomes horizontally flexible and expands to fill the available width, because its displayed content keeps updating over time. Widgets can’t perform layout again after the system archives them, so the text can’t measure itself against its eventual content without risking clipping. If you want to constrain the width, apply a [`frame(width:height:alignment:)`](../view/frame%28width,height,alignment%29.md) modifier, and use [`multilineTextAlignment(_:)`](../view/multilinetextalignment%28_%29.md) to align the text within that frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/text/init(_:format:)-8sfgg)*