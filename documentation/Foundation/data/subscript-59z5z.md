# subscript(_:)

**Framework**: Foundation  
**Kind**: subscript

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
subscript<R>(rangeExpression: R) -> Data where R : RangeExpression, R.Bound : FixedWidthInteger { get set }
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/data/subscript(_:)-59z5z)*