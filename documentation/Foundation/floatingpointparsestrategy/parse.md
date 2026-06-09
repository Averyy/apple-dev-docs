# parse(_:)

**Framework**: Foundation  
**Kind**: method

Parses a floating-point string in accordance with this strategy and returns the parsed value.

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
func parse(_ value: String) throws -> Format.FormatInput
```

#### Return Value

The parsed integer value.

#### Discussion

Use this method to repeatedly parse floating-point strings with the same [`FloatingPointParseStrategy`](floatingpointparsestrategy.md). To parse a single floating-point string, use the initializers inherited from [`BinaryFloatingPoint`](https://developer.apple.com/documentation/Swift/BinaryFloatingPoint) that take a [`String`](https://developer.apple.com/documentation/Swift/String) and a [`FormatStyle`](formatstyle.md) as parameters.

This method throws an error if the parse strategy can’t parse the provided string.

## Parameters

- `value`: The string to parse.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/floatingpointparsestrategy/parse(_:))*