# subscript(_:)

**Framework**: Foundation  
**Kind**: subscript

**Availability**:
- Mac Catalyst 13.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
subscript<R>(r: R) -> Self.SubSequence where R : RangeExpression, Self.Index == R.Bound { get set }
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/data/subscript(_:)-6fjxg)*