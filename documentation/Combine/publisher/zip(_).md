# zip(_:)

**Framework**: Combine  
**Kind**: method  
**Role**: Instance Method

Combines elements from another publisher and deliver pairs of elements as tuples.

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
func zip<P>(_ other: P) -> Publishers.Zip<Self, P> where P : Publisher, Self.Failure == P.Failure
```

## Return Value

A publisher that emits pairs of elements from the upstream publishers as tuples.

## Discussion

Use [`zip(_:)`](./zip%28_%29.md) to combine the latest elements from two publishers and emit a tuple to the downstream. The returned publisher waits until both publishers have emitted an event, then delivers the oldest unconsumed event from each publisher together as a tuple to the subscriber.

Much like a zipper or zip fastener on a piece of clothing pulls together rows of teeth to link the two sides, [`zip(_:)`](./zip%28_%29.md) combines streams from two different publishers by linking pairs of elements from each side.

In this example, `numbers` and `letters` are [`PassthroughSubject`](../passthroughsubject.md)s that emit values; once [`zip(_:)`](./zip%28_%29.md) receives one value from each, it publishes the pair as a tuple to the downstream subscriber. It then waits for the next pair of values.

```swift
 let numbersPub = PassthroughSubject<Int, Never>()
 let lettersPub = PassthroughSubject<String, Never>()

 cancellable = numbersPub
     .zip(lettersPub)
     .sink { print("\($0)") }
 numbersPub.send(1)    // numbersPub: 1      lettersPub:        zip output: <none>
 numbersPub.send(2)    // numbersPub: 1,2    lettersPub:        zip output: <none>
 letters.send("A")     // numbers: 1,2       letters:"A"        zip output: <none>
 numbers.send(3)       // numbers: 1,2,3     letters:           zip output: (1,"A")
 letters.send("B")     // numbers: 1,2,3     letters: "B"       zip output: (2,"B")

 // Prints:
 //  (1, "A")
 //  (2, "B")
```

If either upstream publisher finishes successfully or fails with an error, the zipped publisher does the same.

## Parameters

- `other`: Another publisher.

## See Also

### Collecting and republishing the oldest unconsumed elements from multiple publishers
- [func zip<P, T>(P, (Self.Output, P.Output) -> T) -> Publishers.Map<Publishers.Zip<Self, P>, T>](./zip%28_,_%29-4xn21.md)
  Combines elements from another publisher and delivers a transformed output.
- [func zip<P, Q>(P, Q) -> Publishers.Zip3<Self, P, Q>](./zip%28_,_%29-8d7k7.md)
  Combines elements from two other publishers and delivers groups of elements as tuples.
- [func zip<P, Q, T>(P, Q, (Self.Output, P.Output, Q.Output) -> T) -> Publishers.Map<Publishers.Zip3<Self, P, Q>, T>](./zip%28_,_,_%29-9yqi1.md)
  Combines elements from two other publishers and delivers a transformed output.
- [func zip<P, Q, R>(P, Q, R) -> Publishers.Zip4<Self, P, Q, R>](./zip%28_,_,_%29-16rcy.md)
  Combines elements from three other publishers and delivers groups of elements as tuples.
- [func zip<P, Q, R, T>(P, Q, R, (Self.Output, P.Output, Q.Output, R.Output) -> T) -> Publishers.Map<Publishers.Zip4<Self, P, Q, R>, T>](./zip%28_,_,_,_%29.md)
  Combines elements from three other publishers and delivers a transformed output.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publisher/zip(_:))*