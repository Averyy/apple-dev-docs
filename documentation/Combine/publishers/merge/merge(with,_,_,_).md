# merge(with:_:_:_:)

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
func merge<Z, Y, X, W>(with z: Z, _ y: Y, _ x: X, _ w: W) -> Publishers.Merge6<A, B, Z, Y, X, W> where Z : Publisher, Y : Publisher, X : Publisher, W : Publisher, B.Failure == Z.Failure, B.Output == Z.Output, Z.Failure == Y.Failure, Z.Output == Y.Output, Y.Failure == X.Failure, Y.Output == X.Output, X.Failure == W.Failure, X.Output == W.Output
```

## See Also

### Merging elements
- [func merge<P>(with: P) -> Publishers.Merge3<A, B, P>](./merge%28with%29.md)
- [func merge<Z, Y>(with: Z, Y) -> Publishers.Merge4<A, B, Z, Y>](./merge%28with,_%29.md)
- [func merge<Z, Y, X>(with: Z, Y, X) -> Publishers.Merge5<A, B, Z, Y, X>](./merge%28with,_,_%29.md)
- [func merge<Z, Y, X, W, V>(with: Z, Y, X, W, V) -> Publishers.Merge7<A, B, Z, Y, X, W, V>](./merge%28with,_,_,_,_%29.md)
- [func merge<Z, Y, X, W, V, U>(with: Z, Y, X, W, V, U) -> Publishers.Merge8<A, B, Z, Y, X, W, V, U>](./merge%28with,_,_,_,_,_%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/merge/merge(with:_:_:_:))*