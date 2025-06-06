# parse(_:)

**Framework**: Foundation  
**Kind**: method  
**Required**: Yes

Parses a value, using this strategy.

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
func parse(_ value: Self.ParseInput) throws -> Self.ParseOutput
```

#### Return Value

A parsed value of the type declared by [`ParseOutput`](parsestrategy/parseoutput.md).

#### Discussion

This method throws an error if the parse strategy can’t parse `value`.

## Parameters

- `value`: A value whose type matches the strategy’s   type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/parsestrategy/parse(_:))*