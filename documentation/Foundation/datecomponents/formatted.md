# formatted(_:)

**Framework**: Foundation  
**Kind**: method

Converts `self` to its textual representation.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 1.0+
- watchOS 26.0+ (Beta)

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