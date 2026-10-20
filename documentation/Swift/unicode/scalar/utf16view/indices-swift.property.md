# indices

**Framework**: Swift  
**Kind**: property  
**Role**: Instance Property

The indices that are valid for subscripting the collection, in ascending order.

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
var indices: Range<Self.Index> { get }
```

Available when `Index` conforms to `Strideable`, `Indices` is `Range<Self.Index>`, and `Index.Stride` is `Int`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/unicode/scalar/utf16view/indices-swift.property)*