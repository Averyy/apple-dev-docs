# tokenRange(at:unit:)

**Framework**: Natural Language  
**Kind**: method

Returns the range of the linguistic unit containing the specified character index.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 12.0+
- macOS 10.14+
- tvOS 12.0+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
@nonobjc
func tokenRange(at index: String.Index, unit: NLTokenUnit) -> Range<String.Index>
```

#### Return Value

The range of the substring for the linguistic unit.

## Parameters

- `unit`: The linguistic unit. For possible values, see  .

## See Also

- [func tokenRange(for: Range<String.Index>, unit: NLTokenUnit) -> Range<String.Index>](nltagger/tokenrange(for:unit:).md)
  Finds the entire range of all tokens of the specified linguistic unit contained completely or partially within the specified range.
- [enum NLTokenUnit](nltokenunit.md)
  Constants representing linguistic units.


---

*[View on Apple Developer](https://developer.apple.com/documentation/naturallanguage/nltagger/tokenrange(at:unit:))*