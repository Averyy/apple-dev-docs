# merge(with:_:_:_:)

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
func merge<Z, Y, X, W>(with z: Z, _ y: Y, _ x: X, _ w: W) -> Publishers.Merge8<A, B, C, D, Z, Y, X, W> where Z : Publisher, Y : Publisher, X : Publisher, W : Publisher, D.Failure == Z.Failure, D.Output == Z.Output, Z.Failure == Y.Failure, Z.Output == Y.Output, Y.Failure == X.Failure, Y.Output == X.Output, X.Failure == W.Failure, X.Output == W.Output
```

## See Also

- [func merge<P>(with: P) -> Publishers.Merge5<A, B, C, D, P>](publishers/merge4/merge(with:).md)
- [func merge<Z, Y>(with: Z, Y) -> Publishers.Merge6<A, B, C, D, Z, Y>](publishers/merge4/merge(with:_:).md)
- [func merge<Z, Y, X>(with: Z, Y, X) -> Publishers.Merge7<A, B, C, D, Z, Y, X>](publishers/merge4/merge(with:_:_:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/merge4/merge(with:_:_:_:))*