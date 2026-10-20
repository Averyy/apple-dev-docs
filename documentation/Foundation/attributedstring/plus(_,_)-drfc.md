# +(_:_:)

**Framework**: Foundation  
**Kind**: op  
**Role**: Operator

Concatenates two attributed strings or substrings.

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
static func + (lhs: AttributedString, rhs: some AttributedStringProtocol) -> AttributedString
```

#### Return Value

The result of concatenating `rhs` to the end of `lhs`.

## Parameters

- `lhs`: An attributed string or substring to concatenate.
- `rhs`: Another attributed string or substring to concatenate.

## See Also

### Combining Attributed Strings
- [func append(some AttributedStringProtocol)](./append%28_%29.md)
  Appends a string to the attributed string.
- [static func + (AttributedString, AttributedString) -> AttributedString](./plus%28_,_%29-8sbsq.md)
  Concatenates two attributed strings.
- [static func += (inout AttributedString, AttributedString)](./pluseq%28_,_%29-4dk88.md)
  Appends an attributed string to another attributed string.
- [static func += (inout AttributedString, some AttributedStringProtocol)](./pluseq%28_,_%29-6yimu.md)
  Appends an attributed string or substring to another attributed string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/attributedstring/+(_:_:)-drfc)*