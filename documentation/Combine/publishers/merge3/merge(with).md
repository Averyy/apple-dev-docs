# merge(with:)

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
func merge<P>(with other: P) -> Publishers.Merge4<A, B, C, P> where P : Publisher, C.Failure == P.Failure, C.Output == P.Output
```

## See Also

### Merging elements
- [func merge<Z, Y>(with: Z, Y) -> Publishers.Merge5<A, B, C, Z, Y>](./merge%28with,_%29.md)
- [func merge<Z, Y, X>(with: Z, Y, X) -> Publishers.Merge6<A, B, C, Z, Y, X>](./merge%28with,_,_%29.md)
- [func merge<Z, Y, X, W>(with: Z, Y, X, W) -> Publishers.Merge7<A, B, C, Z, Y, X, W>](./merge%28with,_,_,_%29.md)
- [func merge<Z, Y, X, W, V>(with: Z, Y, X, W, V) -> Publishers.Merge8<A, B, C, Z, Y, X, W, V>](./merge%28with,_,_,_,_%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/merge3/merge(with:))*