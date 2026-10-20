# merge(with:_:_:)

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
func merge<Z, Y, X>(with z: Z, _ y: Y, _ x: X) -> Publishers.Merge8<A, B, C, D, E, Z, Y, X> where Z : Publisher, Y : Publisher, X : Publisher, E.Failure == Z.Failure, E.Output == Z.Output, Z.Failure == Y.Failure, Z.Output == Y.Output, Y.Failure == X.Failure, Y.Output == X.Output
```

## See Also

- [func merge<P>(with: P) -> Publishers.Merge6<A, B, C, D, E, P>](publishers/merge5/merge(with:).md)
- [func merge<Z, Y>(with: Z, Y) -> Publishers.Merge7<A, B, C, D, E, Z, Y>](publishers/merge5/merge(with:_:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/merge5/merge(with:_:_:))*