# merge(with:_:_:_:_:_:_:)

**Framework**: RealityKit  
**Kind**: method

Combines elements from this publisher with those from seven other publishers, delivering an interleaved sequence of elements.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst ?+
- macOS 10.15+
- tvOS 13.0+
- visionOS ?+
- watchOS 6.0+

## Declaration

```swift
func merge<B, C, D, E, F, G, H>(with b: B, _ c: C, _ d: D, _ e: E, _ f: F, _ g: G, _ h: H) -> Publishers.Merge8<Self, B, C, D, E, F, G, H> where B : Publisher, C : Publisher, D : Publisher, E : Publisher, F : Publisher, G : Publisher, H : Publisher, Self.Failure == B.Failure, Self.Output == B.Output, B.Failure == C.Failure, B.Output == C.Output, C.Failure == D.Failure, C.Output == D.Output, D.Failure == E.Failure, D.Output == E.Output, E.Failure == F.Failure, E.Output == F.Output, F.Failure == G.Failure, F.Output == G.Output, G.Failure == H.Failure, G.Output == H.Output
```

#### Return Value

A publisher that emits an event when any upstream publisher emits an event.

#### Discussion

Use [`merge(with:_:_:_:_:_:_:)`](scene/publisher/merge(with:_:_:_:_:_:_:).md) when you want to receive a new element whenever any of the upstream publishers emits an element. To receive tuples of the most-recent value from all the upstream publishers whenever any of them emit a value, use `Publisher/combineLatest(_:_:_:)-48buc`. To combine elements from multiple upstream publishers, use `Publisher/zip(_:_:_:)-16rcy`.

In this example, as [`merge(with:_:_:_:_:_:_:)`](scene/publisher/merge(with:_:_:_:_:_:_:).md) receives input from the upstream publishers, it republishes the interleaved elements to the downstream:

```None
let pubA = PassthroughSubject<Int, Never>()
let pubB = PassthroughSubject<Int, Never>()
let pubC = PassthroughSubject<Int, Never>()
let pubD = PassthroughSubject<Int, Never>()
let pubE = PassthroughSubject<Int, Never>()
let pubF = PassthroughSubject<Int, Never>()
let pubG = PassthroughSubject<Int, Never>()
let pubH = PassthroughSubject<Int, Never>()

cancellable = pubA
    .merge(with: pubB, pubC, pubD, pubE, pubF, pubG, pubH)
    .sink { print("\($0)", terminator: " " ) }

pubA.send(1)
pubB.send(40)
pubC.send(90)
pubD.send(-1)
pubE.send(33)
pubF.send(44)
pubG.send(54)
pubH.send(1000)

pubA.send(2)
pubB.send(50)
pubC.send(100)
pubD.send(-2)
pubE.send(33)
pubF.send(33)
pubG.send(54)
pubH.send(1001)

//Prints: "1 40 90 -1 33 44 54 1000 2 50 100 -2 33 33 54 1001"
```

The merged publisher continues to emit elements until all upstream publishers finish. If an upstream publisher produces an error, the merged publisher fails with that error.

## Parameters

- `b`: A second publisher.
- `c`: A third publisher.
- `d`: A fourth publisher.
- `e`: A fifth publisher.
- `f`: A sixth publisher.
- `g`: A seventh publisher.
- `h`: An eighth publisher.

## See Also

- [func combineLatest<P, T>(P, (Self.Output, P.Output) -> T) -> Publishers.Map<Publishers.CombineLatest<Self, P>, T>](scene/publisher/combinelatest(_:_:)-67l1j.md)
  Subscribes to an additional publisher and invokes a closure upon receiving output from either publisher.
- [func combineLatest<P>(P) -> Publishers.CombineLatest<Self, P>](scene/publisher/combinelatest(_:).md)
  Subscribes to an additional publisher and publishes a tuple upon receiving output from either publisher.
- [func combineLatest<P, Q, T>(P, Q, (Self.Output, P.Output, Q.Output) -> T) -> Publishers.Map<Publishers.CombineLatest3<Self, P, Q>, T>](scene/publisher/combinelatest(_:_:_:)-2r8x1.md)
  Subscribes to two additional publishers and invokes a closure upon receiving output from any of the publishers.
- [func combineLatest<P, Q>(P, Q) -> Publishers.CombineLatest3<Self, P, Q>](scene/publisher/combinelatest(_:_:)-dmq9.md)
  Subscribes to two additional publishers and publishes a tuple upon receiving output from any of the publishers.
- [func combineLatest<P, Q, R, T>(P, Q, R, (Self.Output, P.Output, Q.Output, R.Output) -> T) -> Publishers.Map<Publishers.CombineLatest4<Self, P, Q, R>, T>](scene/publisher/combinelatest(_:_:_:_:).md)
  Subscribes to three additional publishers and invokes a closure upon receiving output from any of the publishers.
- [func combineLatest<P, Q, R>(P, Q, R) -> Publishers.CombineLatest4<Self, P, Q, R>](scene/publisher/combinelatest(_:_:_:)-8tlvp.md)
  Subscribes to three additional publishers and publishes a tuple upon receiving output from any of the publishers.
- [func merge(with: Self) -> Publishers.MergeMany<Self>](scene/publisher/merge(with:).md)
  Combines elements from this publisher with those from another publisher of the same type, delivering an interleaved sequence of elements.
- [func merge<B, C>(with: B, C) -> Publishers.Merge3<Self, B, C>](scene/publisher/merge(with:_:).md)
  Combines elements from this publisher with those from two other publishers, delivering an interleaved sequence of elements.
- [func merge<B, C, D>(with: B, C, D) -> Publishers.Merge4<Self, B, C, D>](scene/publisher/merge(with:_:_:).md)
  Combines elements from this publisher with those from three other publishers, delivering an interleaved sequence of elements.
- [func merge<B, C, D, E>(with: B, C, D, E) -> Publishers.Merge5<Self, B, C, D, E>](scene/publisher/merge(with:_:_:_:).md)
  Combines elements from this publisher with those from four other publishers, delivering an interleaved sequence of elements.
- [func merge<B, C, D, E, F>(with: B, C, D, E, F) -> Publishers.Merge6<Self, B, C, D, E, F>](scene/publisher/merge(with:_:_:_:_:).md)
  Combines elements from this publisher with those from five other publishers, delivering an interleaved sequence of elements.
- [func merge<B, C, D, E, F, G>(with: B, C, D, E, F, G) -> Publishers.Merge7<Self, B, C, D, E, F, G>](scene/publisher/merge(with:_:_:_:_:_:).md)
  Combines elements from this publisher with those from six other publishers, delivering an interleaved sequence of elements.
- [func zip<P>(P) -> Publishers.Zip<Self, P>](scene/publisher/zip(_:).md)
  Combines elements from another publisher and deliver pairs of elements as tuples.
- [func zip<P, T>(P, (Self.Output, P.Output) -> T) -> Publishers.Map<Publishers.Zip<Self, P>, T>](scene/publisher/zip(_:_:)-7rktp.md)
  Combines elements from another publisher and delivers a transformed output.
- [func zip<P, Q>(P, Q) -> Publishers.Zip3<Self, P, Q>](scene/publisher/zip(_:_:)-7vndw.md)
  Combines elements from two other publishers and delivers groups of elements as tuples.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/scene/publisher/merge(with:_:_:_:_:_:_:))*