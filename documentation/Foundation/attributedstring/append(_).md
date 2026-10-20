# append(_:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Appends a string to the attributed string.

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
mutating func append(_ s: some AttributedStringProtocol)
```

## Parameters

- `s`: The string to append.

## See Also

### Combining Attributed Strings
- [static func + (AttributedString, AttributedString) -> AttributedString](./plus%28_,_%29-8sbsq.md)
  Concatenates two attributed strings.
- [static func + (AttributedString, some AttributedStringProtocol) -> AttributedString](./plus%28_,_%29-drfc.md)
  Concatenates two attributed strings or substrings.
- [static func += (inout AttributedString, AttributedString)](./pluseq%28_,_%29-4dk88.md)
  Appends an attributed string to another attributed string.
- [static func += (inout AttributedString, some AttributedStringProtocol)](./pluseq%28_,_%29-6yimu.md)
  Appends an attributed string or substring to another attributed string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/attributedstring/append(_:))*