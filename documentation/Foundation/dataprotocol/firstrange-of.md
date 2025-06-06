# firstRange(of:)

**Framework**: Foundation  
**Kind**: method

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
func firstRange<D>(of data: D) -> Range<Self.Index>? where D : DataProtocol
```

#### Return Value

The range, if found, of the first match of the provided data sequence.

#### Discussion

An example of searching a data buffer converted from a string:

```swift
let data = "0123456789".data(using: .utf8)!
let pattern = "456".data(using: .utf8)!
let foundRange = data.firstRange(of: pattern)

// foundRange == Range(4..<7)
```

## Parameters

- `data`: The data sequence to find.

## See Also

- [func firstRange<D, R>(of: D, in: R) -> Range<Self.Index>?](dataprotocol/firstrange(of:in:).md)
  Returns the first found range of the type’s data buffer.
- [func lastRange<D>(of: D) -> Range<Self.Index>?](dataprotocol/lastrange(of:).md)
  Returns the last found range of the type’s data buffer.
- [func lastRange<D, R>(of: D, in: R) -> Range<Self.Index>?](dataprotocol/lastrange(of:in:).md)
  Returns the last found range of the type’s data buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/dataprotocol/firstrange(of:))*