# lastRange(of:)

**Framework**: Foundation  
**Kind**: method

Returns the last found range of the type’s data buffer.

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
func lastRange<D>(of data: D) -> Range<Self.Index>? where D : DataProtocol
```

#### Return Value

The range, if found, of the last match of the provided data sequence.

#### Discussion

An example of searching a data buffer for the last match:

```swift
let data: [UInt8] = [0, 1, 2, 3, 0, 1, 2, 3]
let pattern: [UInt8] = [2, 3]

let match = data.lastRange(of: pattern)
// match == 6..<8

```

## Parameters

- `data`: The data sequence to find.

## See Also

- [func firstRange<D>(of: D) -> Range<Self.Index>?](dataprotocol/firstrange(of:).md)
  Returns the first found range of the type’s data buffer.
- [func firstRange<D, R>(of: D, in: R) -> Range<Self.Index>?](dataprotocol/firstrange(of:in:).md)
  Returns the first found range of the type’s data buffer.
- [func lastRange<D, R>(of: D, in: R) -> Range<Self.Index>?](dataprotocol/lastrange(of:in:).md)
  Returns the last found range of the type’s data buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/dataprotocol/lastrange(of:))*