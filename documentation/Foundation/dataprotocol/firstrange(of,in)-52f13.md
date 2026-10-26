# firstRange(of:in:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

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
func firstRange<D, R>(of data: D, in range: R) -> Range<Self.Index>? where D : DataProtocol, R : RangeExpression, Self.Index == R.Bound
```

#### Return Value

The range, if found, of the first match of the provided data sequence.

## Parameters

- `data`: The data sequence to find.
- `range`: A range to limit the scope of the search.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/dataprotocol/firstrange(of:in:)-52f13)*