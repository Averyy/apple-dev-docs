# merge(with:_:)

**Framework**: Combine  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
func merge<Z, Y>(with z: Z, _ y: Y) -> Publishers.Merge8<A, B, C, D, E, F, Z, Y> where Z : Publisher, Y : Publisher, F.Failure == Z.Failure, F.Output == Z.Output, Z.Failure == Y.Failure, Z.Output == Y.Output
```

## See Also

### Merging elements
- [func merge<P>(with: P) -> Publishers.Merge7<A, B, C, D, E, F, P>](./merge%28with%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/merge6/merge(with:_:))*