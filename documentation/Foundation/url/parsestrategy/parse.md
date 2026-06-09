# parse(_:)

**Framework**: Foundation  
**Kind**: method

Parses a URL string in accordance with this strategy and returns the parsed value.

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
func parse(_ value: String) throws -> URL
```

#### Return Value

The parsed integer value.

#### Discussion

Use this method to repeatedly parse integer strings with the same [`URL.ParseStrategy`](url/parsestrategy.md). To parse a single integer string, use the URL initializer [`init(_:strategy:)`](url/init(_:strategy:).md).

This method throws an error if the parse strategy can’t parse the provided string.

## Parameters

- `value`: The string to parse.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/url/parsestrategy/parse(_:))*