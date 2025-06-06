# zip(_:_:_:)

**Framework**: RealityKit  
**Kind**: method

Combines elements from two other publishers and delivers a transformed output.

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
func zip<P, Q, T>(_ publisher1: P, _ publisher2: Q, _ transform: @escaping (Self.Output, P.Output, Q.Output) -> T) -> Publishers.Map<Publishers.Zip3<Self, P, Q>, T> where P : Publisher, Q : Publisher, Self.Failure == P.Failure, P.Failure == Q.Failure
```

#### Return Value

A publisher that uses the `transform` closure to emit new elements, produced by combining the most recent value from three upstream publishers.

#### Discussion

Use `Publisher/zip(_:_:_:)-9yqi1` to return a new publisher that combines the elements from two other publishers using a transformation you specify to publish a new value to the downstream subscriber. The returned publisher waits until all three publishers have emitted an event, then delivers the oldest unconsumed event from each publisher together that the operator uses in the transformation.

In this example, `numbersPub`, `lettersPub` and `emojiPub` are each a `PassthroughSubject` that emit values; `Publisher/zip(_:_:_:)-9yqi1` receives the oldest value from each publisher and uses the `Int` from `numbersPub` and publishes a string that repeats the [`String`](https://developer.apple.com/documentation/Swift/String) from `lettersPub` and `emojiPub` that many times.

```None
let numbersPub = PassthroughSubject<Int, Never>()
let lettersPub = PassthroughSubject<String, Never>()
let emojiPub = PassthroughSubject<String, Never>()

cancellable = numbersPub
    .zip(letters, emoji) { anInt, aLetter, anEmoji in
        ("\(String(repeating: anEmoji, count: anInt)) \(String(repeating: aLetter, count: anInt))")
    }
    .sink { print("\($0)") }

numbersPub.send(1)     // numbersPub: 1      lettersPub:        emojiPub:            zip output: <none>
numbersPub.send(2)     // numbersPub: 1,2    lettersPub:        emojiPub:            zip output: <none>
numbersPub.send(3)     // numbersPub: 1,2,3  lettersPub:        emojiPub:            zip output: <none>
lettersPub.send("A")   // numbersPub: 1,2,3  lettersPub: "A"    emojiPub:            zip output: <none>
emojiPub.send("😀")    // numbersPub: 2,3    lettersPub: "A"    emojiPub:"😀"        zip output: "😀 A"
lettersPub.send("B")   // numbersPub: 2,3    lettersPub: "B"    emojiPub:            zip output: <none>
emojiPub.send("🥰")    // numbersPub: 3      lettersPub:        emojiPub:"😀", "🥰"  zip output: "🥰🥰 BB"

// Prints:
// 😀 A
// 🥰🥰 BB
```

If any upstream publisher finishes successfully or fails with an error, so too does the zipped publisher.

## Parameters

- `publisher1`: A second publisher.
- `publisher2`: A third publisher.
- `transform`: A closure that receives the most-recent value from each publisher and returns a new value to publish.

## See Also

- [func combineLatest<P, T>(P, (Self.Output, P.Output) -> T) -> Publishers.Map<Publishers.CombineLatest<Self, P>, T>](loadrequest/combinelatest(_:_:)-7ey7f.md)
  Subscribes to an additional publisher and invokes a closure upon receiving output from either publisher.
- [func combineLatest<P>(P) -> Publishers.CombineLatest<Self, P>](loadrequest/combinelatest(_:).md)
  Subscribes to an additional publisher and publishes a tuple upon receiving output from either publisher.
- [func combineLatest<P, Q, T>(P, Q, (Self.Output, P.Output, Q.Output) -> T) -> Publishers.Map<Publishers.CombineLatest3<Self, P, Q>, T>](loadrequest/combinelatest(_:_:_:)-1sayg.md)
  Subscribes to two additional publishers and invokes a closure upon receiving output from any of the publishers.
- [func combineLatest<P, Q>(P, Q) -> Publishers.CombineLatest3<Self, P, Q>](loadrequest/combinelatest(_:_:)-25hkp.md)
  Subscribes to two additional publishers and publishes a tuple upon receiving output from any of the publishers.
- [func combineLatest<P, Q, R, T>(P, Q, R, (Self.Output, P.Output, Q.Output, R.Output) -> T) -> Publishers.Map<Publishers.CombineLatest4<Self, P, Q, R>, T>](loadrequest/combinelatest(_:_:_:_:).md)
  Subscribes to three additional publishers and invokes a closure upon receiving output from any of the publishers.
- [func combineLatest<P, Q, R>(P, Q, R) -> Publishers.CombineLatest4<Self, P, Q, R>](loadrequest/combinelatest(_:_:_:)-431ip.md)
  Subscribes to three additional publishers and publishes a tuple upon receiving output from any of the publishers.
- [func merge<B, C>(with: B, C) -> Publishers.Merge3<Self, B, C>](loadrequest/merge(with:_:).md)
  Combines elements from this publisher with those from two other publishers, delivering an interleaved sequence of elements.
- [func merge<B, C, D>(with: B, C, D) -> Publishers.Merge4<Self, B, C, D>](loadrequest/merge(with:_:_:).md)
  Combines elements from this publisher with those from three other publishers, delivering an interleaved sequence of elements.
- [func merge<B, C, D, E>(with: B, C, D, E) -> Publishers.Merge5<Self, B, C, D, E>](loadrequest/merge(with:_:_:_:).md)
  Combines elements from this publisher with those from four other publishers, delivering an interleaved sequence of elements.
- [func merge<B, C, D, E, F>(with: B, C, D, E, F) -> Publishers.Merge6<Self, B, C, D, E, F>](loadrequest/merge(with:_:_:_:_:).md)
  Combines elements from this publisher with those from five other publishers, delivering an interleaved sequence of elements.
- [func merge<B, C, D, E, F, G>(with: B, C, D, E, F, G) -> Publishers.Merge7<Self, B, C, D, E, F, G>](loadrequest/merge(with:_:_:_:_:_:).md)
  Combines elements from this publisher with those from six other publishers, delivering an interleaved sequence of elements.
- [func merge<B, C, D, E, F, G, H>(with: B, C, D, E, F, G, H) -> Publishers.Merge8<Self, B, C, D, E, F, G, H>](loadrequest/merge(with:_:_:_:_:_:_:).md)
  Combines elements from this publisher with those from seven other publishers, delivering an interleaved sequence of elements.
- [func zip<P>(P) -> Publishers.Zip<Self, P>](loadrequest/zip(_:).md)
  Combines elements from another publisher and deliver pairs of elements as tuples.
- [func zip<P, T>(P, (Self.Output, P.Output) -> T) -> Publishers.Map<Publishers.Zip<Self, P>, T>](loadrequest/zip(_:_:)-62pcj.md)
  Combines elements from another publisher and delivers a transformed output.
- [func zip<P, Q>(P, Q) -> Publishers.Zip3<Self, P, Q>](loadrequest/zip(_:_:)-8sc5g.md)
  Combines elements from two other publishers and delivers groups of elements as tuples.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/loadrequest/zip(_:_:_:)-23ai8)*