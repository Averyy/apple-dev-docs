# firstRange(of:in:)

**Framework**: Foundation  
**Kind**: method  
**Required**: Yes

Returns the first found range of the type’s data buffer.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func firstRange<D, R>(of: D, in: R) -> Range<Self.Index>? where D : DataProtocol, R : RangeExpression, Self.Index == R.Bound
```

#### Return Value

The range, if found, of the first match of the provided data sequence.

#### Discussion

An example of searching a constrained range within a data buffer for the first match:

```swift
let data: [UInt8] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
let pattern: [UInt8] = [2, 3, 4]

let possibleMatch = data.firstRange(of: pattern, in: 5...9)
// possibleMatch == nil

let match = data.firstRange(of: pattern, in: 2...9)
// match == 2..<5
```

## Parameters

- `of`: The data sequence to find.
- `in`: A range to limit the scope of the search.

## See Also

- [func firstRange<D>(of: D) -> Range<Self.Index>?](dataprotocol/firstrange(of:).md)
  Returns the first found range of the type’s data buffer.
- [func lastRange<D>(of: D) -> Range<Self.Index>?](dataprotocol/lastrange(of:).md)
  Returns the last found range of the type’s data buffer.
- [func lastRange<D, R>(of: D, in: R) -> Range<Self.Index>?](dataprotocol/lastrange(of:in:).md)
  Returns the last found range of the type’s data buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/dataprotocol/firstrange(of:in:))*