# merge(with:)

**Framework**: Combine  
**Kind**: method

Combines elements from this publisher with those from another publisher of the same type, delivering an interleaved sequence of elements.

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
func merge(with other: Self) -> Publishers.MergeMany<Self>
```

#### Return Value

A publisher that emits an event when either upstream publisher emits an event.

## Parameters

- `other`: Another publisher of this publisher’s type.

## See Also

- [func merge<P>(with: P) -> Publishers.Merge3<A, B, P>](publishers/merge/merge(with:).md)
- [func merge<B, C>(with: B, C) -> Publishers.Merge3<Self, B, C>](publishers/merge/merge(with:_:)-1qs5s.md)
  Combines elements from this publisher with those from two other publishers, delivering an interleaved sequence of elements.
- [func merge<Z, Y>(with: Z, Y) -> Publishers.Merge4<A, B, Z, Y>](publishers/merge/merge(with:_:).md)
- [func merge<B, C, D>(with: B, C, D) -> Publishers.Merge4<Self, B, C, D>](publishers/merge/merge(with:_:_:)-7dt5o.md)
  Combines elements from this publisher with those from three other publishers, delivering an interleaved sequence of elements.
- [func merge<Z, Y, X>(with: Z, Y, X) -> Publishers.Merge5<A, B, Z, Y, X>](publishers/merge/merge(with:_:_:).md)
- [func merge<B, C, D, E>(with: B, C, D, E) -> Publishers.Merge5<Self, B, C, D, E>](publishers/merge/merge(with:_:_:_:)-33rgx.md)
  Combines elements from this publisher with those from four other publishers, delivering an interleaved sequence of elements.
- [func merge<Z, Y, X, W>(with: Z, Y, X, W) -> Publishers.Merge6<A, B, Z, Y, X, W>](publishers/merge/merge(with:_:_:_:).md)
- [func merge<B, C, D, E, F>(with: B, C, D, E, F) -> Publishers.Merge6<Self, B, C, D, E, F>](publishers/merge/merge(with:_:_:_:_:)-44szr.md)
  Combines elements from this publisher with those from five other publishers, delivering an interleaved sequence of elements.
- [func merge<Z, Y, X, W, V>(with: Z, Y, X, W, V) -> Publishers.Merge7<A, B, Z, Y, X, W, V>](publishers/merge/merge(with:_:_:_:_:).md)
- [func merge<B, C, D, E, F, G>(with: B, C, D, E, F, G) -> Publishers.Merge7<Self, B, C, D, E, F, G>](publishers/merge/merge(with:_:_:_:_:_:)-39jtm.md)
  Combines elements from this publisher with those from six other publishers, delivering an interleaved sequence of elements.
- [func merge<Z, Y, X, W, V, U>(with: Z, Y, X, W, V, U) -> Publishers.Merge8<A, B, Z, Y, X, W, V, U>](publishers/merge/merge(with:_:_:_:_:_:).md)
- [func merge<B, C, D, E, F, G, H>(with: B, C, D, E, F, G, H) -> Publishers.Merge8<Self, B, C, D, E, F, G, H>](publishers/merge/merge(with:_:_:_:_:_:_:).md)
  Combines elements from this publisher with those from seven other publishers, delivering an interleaved sequence of elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/merge/merge(with:)-9r2dw)*