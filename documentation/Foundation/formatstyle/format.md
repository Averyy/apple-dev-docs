# format(_:)

**Framework**: Foundation  
**Kind**: method  
**Required**: Yes

Formats a value, using this style.

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
func format(_ value: Self.FormatInput) -> Self.FormatOutput
```

#### Return Value

A representation of `value`, in the [`FormatOutput`](formatstyle/formatoutput.md) type, formatted according to the style’s configuration.

#### Discussion

Use this method when you want to create a single style instance, and then use it to format multiple values.

## Parameters

- `value`: The value to format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/formatstyle/format(_:))*