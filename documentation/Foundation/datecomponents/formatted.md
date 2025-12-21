# formatted(_:)

**Framework**: Foundation  
**Kind**: method

Converts `self` to its textual representation.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
func formatted<F>(_ format: F) -> F.FormatOutput where F : FormatStyle, F.FormatInput == DateComponents
```

#### Return Value

A representation of `self` using the given `format`. The type of the representation is specified by `FormatStyle.FormatOutput`.

## Parameters

- `format`: The format for formatting  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/datecomponents/formatted(_:))*