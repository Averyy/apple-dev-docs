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
func merge<P>(with other: P) -> Publishers.Merge7<A, B, C, D, E, F, P> where P : Publisher, F.Failure == P.Failure, F.Output == P.Output
```

## See Also

### Merging elements
- [func merge<Z, Y>(with: Z, Y) -> Publishers.Merge8<A, B, C, D, E, F, Z, Y>](./merge%28with,_%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/merge6/merge(with:))*