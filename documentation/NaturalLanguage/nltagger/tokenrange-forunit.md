# tokenRange(for:unit:)

**Framework**: Natural Language  
**Kind**: method

Finds the entire range of all tokens of the specified linguistic unit contained completely or partially within the specified range.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
@nonobjc
func tokenRange(for range: Range<String.Index>, unit: NLTokenUnit) -> Range<String.Index>
```

#### Return Value

The smallest possible range that contains all of the tokens of the specified linguistic unit within the range specified in `range`. This result includes a token’s entire range if any part of that token is included within `range`. If the length of `range` is 0, this return value is equivalent to [`tokenRangeAtIndex:unit:`](nltagger/tokenrangeatindex:unit:.md).

## Parameters

- `range`: The range within the string to search for tokens.
- `unit`: The linguistic unit. For possible values, see  .

## See Also

- [func tokenRange(at: String.Index, unit: NLTokenUnit) -> Range<String.Index>](nltagger/tokenrange(at:unit:).md)
  Returns the range of the linguistic unit containing the specified character index.
- [enum NLTokenUnit](nltokenunit.md)
  Constants representing linguistic units.


---

*[View on Apple Developer](https://developer.apple.com/documentation/naturallanguage/nltagger/tokenrange(for:unit:))*