# firstRange(of:in:)

**Framework**: Foundation  
**Kind**: method

Returns the first found range of the given data buffer.

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

#### Discussion

A default implementation is given in terms of `self.regions`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/data/firstrange(of:in:))*