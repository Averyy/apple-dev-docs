# +=(_:_:)

**Framework**: Foundation  
**Kind**: op  
**Role**: Operator

Appends an attributed string or substring to another attributed string.

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
static func += (lhs: inout AttributedString, rhs: some AttributedStringProtocol)
```

## Parameters

- `lhs`: An attributed string. After the operation, the value of this string is the original `lhs` string with `rhs` appended to it.
- `rhs`: An attributed string or substring to append to `lhs`.

## See Also

### Combining Attributed Strings
- [func append(some AttributedStringProtocol)](./append%28_%29.md)
  Appends a string to the attributed string.
- [static func + (AttributedString, AttributedString) -> AttributedString](./plus%28_,_%29-8sbsq.md)
  Concatenates two attributed strings.
- [static func + (AttributedString, some AttributedStringProtocol) -> AttributedString](./plus%28_,_%29-drfc.md)
  Concatenates two attributed strings or substrings.
- [static func += (inout AttributedString, AttributedString)](./pluseq%28_,_%29-4dk88.md)
  Appends an attributed string to another attributed string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/attributedstring/+=(_:_:)-6yimu)*