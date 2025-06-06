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

- [func merge<P>(with: P) -> Publishers.Merge5<A, B, C, D, P>](publishers/merge4/merge(with:).md)
- [func merge<B, C>(with: B, C) -> Publishers.Merge3<Self, B, C>](publishers/merge4/merge(with:_:)-68iu2.md)
  Combines elements from this publisher with those from two other publishers, delivering an interleaved sequence of elements.
- [func merge<Z, Y>(with: Z, Y) -> Publishers.Merge6<A, B, C, D, Z, Y>](publishers/merge4/merge(with:_:).md)
- [func merge<B, C, D>(with: B, C, D) -> Publishers.Merge4<Self, B, C, D>](publishers/merge4/merge(with:_:_:)-8xlrj.md)
  Combines elements from this publisher with those from three other publishers, delivering an interleaved sequence of elements.
- [func merge<Z, Y, X>(with: Z, Y, X) -> Publishers.Merge7<A, B, C, D, Z, Y, X>](publishers/merge4/merge(with:_:_:).md)
- [func merge<B, C, D, E>(with: B, C, D, E) -> Publishers.Merge5<Self, B, C, D, E>](publishers/merge4/merge(with:_:_:_:)-2nv09.md)
  Combines elements from this publisher with those from four other publishers, delivering an interleaved sequence of elements.
- [func merge<Z, Y, X, W>(with: Z, Y, X, W) -> Publishers.Merge8<A, B, C, D, Z, Y, X, W>](publishers/merge4/merge(with:_:_:_:).md)
- [func merge<B, C, D, E, F>(with: B, C, D, E, F) -> Publishers.Merge6<Self, B, C, D, E, F>](publishers/merge4/merge(with:_:_:_:_:).md)
  Combines elements from this publisher with those from five other publishers, delivering an interleaved sequence of elements.
- [func merge<B, C, D, E, F, G>(with: B, C, D, E, F, G) -> Publishers.Merge7<Self, B, C, D, E, F, G>](publishers/merge4/merge(with:_:_:_:_:_:).md)
  Combines elements from this publisher with those from six other publishers, delivering an interleaved sequence of elements.
- [func merge<B, C, D, E, F, G, H>(with: B, C, D, E, F, G, H) -> Publishers.Merge8<Self, B, C, D, E, F, G, H>](publishers/merge4/merge(with:_:_:_:_:_:_:).md)
  Combines elements from this publisher with those from seven other publishers, delivering an interleaved sequence of elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/merge4/merge(with:)-67g3k)*