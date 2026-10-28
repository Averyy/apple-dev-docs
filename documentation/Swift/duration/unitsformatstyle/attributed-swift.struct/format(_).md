# format(_:)

**Framework**: Swift  
**Kind**: method  
**Role**: Instance Method

Creates a locale-aware attributed string representation from a duration value.

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
func format(_ duration: Duration) -> AttributedString
```

## Return Value

A string representation of the duration, according to the style’s pattern and locale.

## Discussion

Use this method when you want to create a format style and repeatedly use it to format different durations. For one-off cases with default formatting, call the [`formatted()`](../../formatted%28%29.md) method of [`Duration`](../../../duration.md) instead.

## Parameters

- `duration`: The duration value to format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/duration/unitsformatstyle/attributed-swift.struct/format(_:))*