# subscript(_:)

**Framework**: Swift  
**Kind**: subscript

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
subscript<R>(r: R) -> Self.SubSequence where R : RangeExpression, Self.Index == R.Bound { get set }
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/slice/subscript(_:)-4f8ky)*