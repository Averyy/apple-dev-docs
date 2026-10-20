# indices

**Framework**: Swift  
**Kind**: property  
**Role**: Instance Property

The indices that are valid for subscripting the range, in ascending order.

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
var indices: Range<Bound>.Indices { get }
```

Available when `Bound` conforms to `Strideable` and `Bound.Stride` conforms to `SignedInteger`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/range/indices-swift.property)*