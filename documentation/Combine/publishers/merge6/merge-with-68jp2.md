# merge(with:_:)

**Framework**: Combine  
**Kind**: method

Combines elements from this publisher with those from two other publishers, delivering an interleaved sequence of elements.

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
func merge<B, C>(with b: B, _ c: C) -> Publishers.Merge3<Self, B, C> where B : Publisher, C : Publisher, Self.Failure == B.Failure, Self.Output == B.Output, B.Failure == C.Failure, B.Output == C.Output
```

#### Return Value

A publisher that emits an event when any upstream publisher emits an event.

#### Discussion

Use [`merge(with:_:)`](publisher/merge(with:_:).md) when you want to receive a new element whenever any of the upstream publishers emits an element. To receive tuples of the most-recent value from all the upstream publishers whenever any of them emit a value, use [`combineLatest(_:_:)`](publisher/combinelatest(_:_:)-5crqg.md). To combine elements from multiple upstream publishers, use [`zip(_:_:)`](publisher/zip(_:_:)-8d7k7.md).

In this example, as [`merge(with:_:)`](publisher/merge(with:_:).md) receives input from the upstream publishers, it republishes the interleaved elements to the downstream:

```swift
let pubA = PassthroughSubject<Int, Never>()
let pubB = PassthroughSubject<Int, Never>()
let pubC = PassthroughSubject<Int, Never>()

cancellable = pubA
    .merge(with: pubB, pubC)
    .sink { print("\($0)", terminator: " " )}

pubA.send(1)
pubB.send(40)
pubC.send(90)
pubA.send(2)
pubB.send(50)
pubC.send(100)

// Prints: "1 40 90 2 50 100"
```

The merged publisher continues to emit elements until all upstream publishers finish. If an upstream publisher produces an error, the merged publisher fails with that error.

## Parameters

- `b`: A second publisher.
- `c`: A third publisher.

## See Also

- [func merge(with: Self) -> Publishers.MergeMany<Self>](publishers/merge6/merge(with:)-67fi0.md)
  Combines elements from this publisher with those from another publisher of the same type, delivering an interleaved sequence of elements.
- [func merge<P>(with: P) -> Publishers.Merge7<A, B, C, D, E, F, P>](publishers/merge6/merge(with:).md)
- [func merge<Z, Y>(with: Z, Y) -> Publishers.Merge8<A, B, C, D, E, F, Z, Y>](publishers/merge6/merge(with:_:).md)
- [func merge<B, C, D>(with: B, C, D) -> Publishers.Merge4<Self, B, C, D>](publishers/merge6/merge(with:_:_:).md)
  Combines elements from this publisher with those from three other publishers, delivering an interleaved sequence of elements.
- [func merge<B, C, D, E>(with: B, C, D, E) -> Publishers.Merge5<Self, B, C, D, E>](publishers/merge6/merge(with:_:_:_:).md)
  Combines elements from this publisher with those from four other publishers, delivering an interleaved sequence of elements.
- [func merge<B, C, D, E, F>(with: B, C, D, E, F) -> Publishers.Merge6<Self, B, C, D, E, F>](publishers/merge6/merge(with:_:_:_:_:).md)
  Combines elements from this publisher with those from five other publishers, delivering an interleaved sequence of elements.
- [func merge<B, C, D, E, F, G>(with: B, C, D, E, F, G) -> Publishers.Merge7<Self, B, C, D, E, F, G>](publishers/merge6/merge(with:_:_:_:_:_:).md)
  Combines elements from this publisher with those from six other publishers, delivering an interleaved sequence of elements.
- [func merge<B, C, D, E, F, G, H>(with: B, C, D, E, F, G, H) -> Publishers.Merge8<Self, B, C, D, E, F, G, H>](publishers/merge6/merge(with:_:_:_:_:_:_:).md)
  Combines elements from this publisher with those from seven other publishers, delivering an interleaved sequence of elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/merge6/merge(with:_:)-68jp2)*