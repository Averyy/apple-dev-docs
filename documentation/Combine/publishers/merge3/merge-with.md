# merge(with:_:_:_:_:)

**Framework**: Combine  
**Kind**: method

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
func merge<Z, Y, X, W, V>(with z: Z, _ y: Y, _ x: X, _ w: W, _ v: V) -> Publishers.Merge8<A, B, C, Z, Y, X, W, V> where Z : Publisher, Y : Publisher, X : Publisher, W : Publisher, V : Publisher, C.Failure == Z.Failure, C.Output == Z.Output, Z.Failure == Y.Failure, Z.Output == Y.Output, Y.Failure == X.Failure, Y.Output == X.Output, X.Failure == W.Failure, X.Output == W.Output, W.Failure == V.Failure, W.Output == V.Output
```

## See Also

- [func merge<P>(with: P) -> Publishers.Merge4<A, B, C, P>](publishers/merge3/merge(with:).md)
- [func merge<Z, Y>(with: Z, Y) -> Publishers.Merge5<A, B, C, Z, Y>](publishers/merge3/merge(with:_:).md)
- [func merge<Z, Y, X>(with: Z, Y, X) -> Publishers.Merge6<A, B, C, Z, Y, X>](publishers/merge3/merge(with:_:_:).md)
- [func merge<Z, Y, X, W>(with: Z, Y, X, W) -> Publishers.Merge7<A, B, C, Z, Y, X, W>](publishers/merge3/merge(with:_:_:_:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/merge3/merge(with:_:_:_:_:))*