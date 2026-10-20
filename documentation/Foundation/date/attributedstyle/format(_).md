# format(_:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Creates a locale-aware attributed string representation from a date value.

**Availability**:
- iOS 15.0+ - Deprecated in 18.0
- iPadOS 15.0+ - Deprecated in 18.0
- Mac Catalyst 15.0+ - Deprecated in 18.0
- macOS 12.0+ - Deprecated in 15.0
- tvOS 15.0+ - Deprecated in 18.0
- visionOS 1.0+
- watchOS 8.0+ - Deprecated in 11.0

> **Deprecated**: Use Date.FormatStyle.Attributed or Date.VerbatimFormatStyle.Attributed instead

## Declaration

```swift
func format(_ value: Date) -> AttributedString
```

#### Return Value

An attributed string representation of the date.

#### Discussion

The [`Date.ISO8601FormatStyle`](../iso8601formatstyle.md) [`format(_:)`](../formatstyle/format%28_%29.md) instance method generates an attributed string from the provided date. Once you create a style, you can use it to format dates multiple times.

For an example of formatting multiple dates into plain strings, see [`format(_:)`](../formatstyle/format%28_%29.md).

## Parameters

- `value`: The date to format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/date/attributedstyle/format(_:))*