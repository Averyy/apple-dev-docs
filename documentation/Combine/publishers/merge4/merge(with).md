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
func merge<P>(with other: P) -> Publishers.Merge5<A, B, C, D, P> where P : Publisher, D.Failure == P.Failure, D.Output == P.Output
```

## See Also

### Merging elements
- [func merge<Z, Y>(with: Z, Y) -> Publishers.Merge6<A, B, C, D, Z, Y>](./merge%28with,_%29.md)
- [func merge<Z, Y, X>(with: Z, Y, X) -> Publishers.Merge7<A, B, C, D, Z, Y, X>](./merge%28with,_,_%29.md)
- [func merge<Z, Y, X, W>(with: Z, Y, X, W) -> Publishers.Merge8<A, B, C, D, Z, Y, X, W>](./merge%28with,_,_,_%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/merge4/merge(with:))*