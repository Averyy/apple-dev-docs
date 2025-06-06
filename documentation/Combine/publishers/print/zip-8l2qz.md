# zip(_:_:)

**Framework**: Combine  
**Kind**: method

Combines elements from two other publishers and delivers groups of elements as tuples.

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
func zip<P, Q>(_ publisher1: P, _ publisher2: Q) -> Publishers.Zip3<Self, P, Q> where P : Publisher, Q : Publisher, Self.Failure == P.Failure, P.Failure == Q.Failure
```

#### Return Value

A publisher that emits groups of elements from the upstream publishers as tuples.

#### Discussion

Use [`zip(_:_:)`](publisher/zip(_:_:)-8d7k7.md) to return a new publisher that combines the elements from two additional publishers to publish a tuple to the downstream. The returned publisher waits until all three publishers have emitted an event, then delivers the oldest unconsumed event from each publisher as a tuple to the subscriber.

In this example, `numbersPub`, `lettersPub` and `emojiPub` are each a [`PassthroughSubject`](passthroughsubject.md); [`zip(_:_:)`](publisher/zip(_:_:)-8d7k7.md) receives the oldest unconsumed value from each publisher and combines them into a tuple that it republishes to the downstream:

```swift
let numbersPub = PassthroughSubject<Int, Never>()
let lettersPub = PassthroughSubject<String, Never>()
let emojiPub = PassthroughSubject<String, Never>()

cancellable = numbersPub
    .zip(lettersPub, emojiPub)
    .sink { print("\($0)") }
numbersPub.send(1)     // numbersPub: 1      lettersPub:          emojiPub:        zip output: <none>
numbersPub.send(2)     // numbersPub: 1,2    lettersPub:          emojiPub:        zip output: <none>
numbersPub.send(3)     // numbersPub: 1,2,3  lettersPub:          emojiPub:        zip output: <none>
lettersPub.send("A")   // numbersPub: 1,2,3  lettersPub: "A"      emojiPub:        zip output: <none>
emojiPub.send("😀")    // numbersPub: 2,3    lettersPub: "A"      emojiPub: "😀"   zip output: (1, "A", "😀")
lettersPub.send("B")   // numbersPub: 2,3    lettersPub: "B"      emojiPub:        zip output: <none>
emojiPub.send("🥰")    // numbersPub: 3      lettersPub:          emojiPub:        zip output: (2, "B", "🥰")

// Prints:
//  (1, "A", "😀")
//  (2, "B", "🥰")
```

If any upstream publisher finishes successfully or fails with an error, so too does the zipped publisher.

## Parameters

- `publisher1`: A second publisher.
- `publisher2`: A third publisher.

## See Also

- [func zip<P>(P) -> Publishers.Zip<Self, P>](publishers/print/zip(_:).md)
  Combines elements from another publisher and deliver pairs of elements as tuples.
- [func zip<P, T>(P, (Self.Output, P.Output) -> T) -> Publishers.Map<Publishers.Zip<Self, P>, T>](publishers/print/zip(_:_:)-8ahgs.md)
  Combines elements from another publisher and delivers a transformed output.
- [func zip<P, Q, T>(P, Q, (Self.Output, P.Output, Q.Output) -> T) -> Publishers.Map<Publishers.Zip3<Self, P, Q>, T>](publishers/print/zip(_:_:_:)-8nsk2.md)
  Combines elements from two other publishers and delivers a transformed output.
- [func zip<P, Q, R>(P, Q, R) -> Publishers.Zip4<Self, P, Q, R>](publishers/print/zip(_:_:_:)-5ot1g.md)
  Combines elements from three other publishers and delivers groups of elements as tuples.
- [func zip<P, Q, R, T>(P, Q, R, (Self.Output, P.Output, Q.Output, R.Output) -> T) -> Publishers.Map<Publishers.Zip4<Self, P, Q, R>, T>](publishers/print/zip(_:_:_:_:).md)
  Combines elements from three other publishers and delivers a transformed output.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/print/zip(_:_:)-8l2qz)*