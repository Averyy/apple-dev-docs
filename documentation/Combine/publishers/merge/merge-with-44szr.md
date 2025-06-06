# merge(with:_:_:_:_:)

**Framework**: Combine  
**Kind**: method

Combines elements from this publisher with those from five other publishers, delivering an interleaved sequence of elements.

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
func merge<B, C, D, E, F>(with b: B, _ c: C, _ d: D, _ e: E, _ f: F) -> Publishers.Merge6<Self, B, C, D, E, F> where B : Publisher, C : Publisher, D : Publisher, E : Publisher, F : Publisher, Self.Failure == B.Failure, Self.Output == B.Output, B.Failure == C.Failure, B.Output == C.Output, C.Failure == D.Failure, C.Output == D.Output, D.Failure == E.Failure, D.Output == E.Output, E.Failure == F.Failure, E.Output == F.Output
```

#### Return Value

A publisher that emits an event when any upstream publisher emits an event.

#### Discussion

Use [`merge(with:_:_:_:_:_:)`](publisher/merge(with:_:_:_:_:_:).md) when you want to receive a new element whenever any of the upstream publishers emits an element. To receive tuples of the most-recent value from all the upstream publishers whenever any of them emit a value, use [`combineLatest(_:_:_:)`](publisher/combinelatest(_:_:_:)-48buc.md). To combine elements from multiple upstream publishers, use [`zip(_:_:_:)`](publisher/zip(_:_:_:)-16rcy.md).

In this example, as [`merge(with:_:_:_:_:_:)`](publisher/merge(with:_:_:_:_:_:).md) receives input from the upstream publishers, it republishes the interleaved elements to the downstream:

```swift
let pubA = PassthroughSubject<Int, Never>()
let pubB = PassthroughSubject<Int, Never>()
let pubC = PassthroughSubject<Int, Never>()
let pubD = PassthroughSubject<Int, Never>()
let pubE = PassthroughSubject<Int, Never>()
let pubF = PassthroughSubject<Int, Never>()

cancellable = pubA
    .merge(with: pubB, pubC, pubD, pubE, pubF)
    .sink { print("\($0)", terminator: " " ) }

pubA.send(1)
pubB.send(40)
pubC.send(90)
pubD.send(-1)
pubE.send(33)
pubF.send(44)

pubA.send(2)
pubB.send(50)
pubC.send(100)
pubD.send(-2)
pubE.send(33)
pubF.send(33)

//Prints: "1 40 90 -1 33 44 2 50 100 -2 33 33"
```

The merged publisher continues to emit elements until all upstream publishers finish. If an upstream publisher produces an error, the merged publisher fails with that error.

## Parameters

- `b`: A second publisher.
- `c`: A third publisher.
- `d`: A fourth publisher.
- `e`: A fifth publisher.
- `f`: A sixth publisher.

## See Also

- [func merge(with: Self) -> Publishers.MergeMany<Self>](publishers/merge/merge(with:)-9r2dw.md)
  Combines elements from this publisher with those from another publisher of the same type, delivering an interleaved sequence of elements.
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
- [func merge<Z, Y, X, W, V>(with: Z, Y, X, W, V) -> Publishers.Merge7<A, B, Z, Y, X, W, V>](publishers/merge/merge(with:_:_:_:_:).md)
- [func merge<B, C, D, E, F, G>(with: B, C, D, E, F, G) -> Publishers.Merge7<Self, B, C, D, E, F, G>](publishers/merge/merge(with:_:_:_:_:_:)-39jtm.md)
  Combines elements from this publisher with those from six other publishers, delivering an interleaved sequence of elements.
- [func merge<Z, Y, X, W, V, U>(with: Z, Y, X, W, V, U) -> Publishers.Merge8<A, B, Z, Y, X, W, V, U>](publishers/merge/merge(with:_:_:_:_:_:).md)
- [func merge<B, C, D, E, F, G, H>(with: B, C, D, E, F, G, H) -> Publishers.Merge8<Self, B, C, D, E, F, G, H>](publishers/merge/merge(with:_:_:_:_:_:_:).md)
  Combines elements from this publisher with those from seven other publishers, delivering an interleaved sequence of elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/merge/merge(with:_:_:_:_:)-44szr)*