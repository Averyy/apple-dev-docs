# zip(_:_:)

**Framework**: Combine  
**Kind**: method

Combines elements from another publisher and delivers a transformed output.

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
func zip<P, T>(_ other: P, _ transform: @escaping (Self.Output, P.Output) -> T) -> Publishers.Map<Publishers.Zip<Self, P>, T> where P : Publisher, Self.Failure == P.Failure
```

#### Return Value

A publisher that uses the `transform` closure to emit new elements, produced by combining the most recent value from two upstream publishers.

#### Discussion

Use [`zip(_:_:)`](publisher/zip(_:_:)-4xn21.md) to return a new publisher that combines the elements from two publishers using a transformation you specify to publish a new value to the downstream.  The returned publisher waits until both publishers have emitted an event, then delivers the oldest unconsumed event from each publisher together that the operator uses in the transformation.

In this example, [`PassthroughSubject`](passthroughsubject.md) instances `numbersPub` and `lettersPub` emit values; [`zip(_:_:)`](publisher/zip(_:_:)-4xn21.md) receives the oldest value from each publisher, uses the `Int` from `numbersPub` and publishes a string that repeats the [`String`](https://developer.apple.com/documentation/Swift/String) from `lettersPub` that many times.

```swift
let numbersPub = PassthroughSubject<Int, Never>()
let lettersPub = PassthroughSubject<String, Never>()
cancellable = numbersPub
    .zip(lettersPub) { anInt, aLetter in
        String(repeating: aLetter, count: anInt)
    }
    .sink { print("\($0)") }
numbersPub.send(1)     // numbersPub: 1      lettersPub:       zip output: <none>
numbersPub.send(2)     // numbersPub: 1,2    lettersPub:       zip output: <none>
numbersPub.send(3)     // numbersPub: 1,2,3  lettersPub:       zip output: <none>
lettersPub.send("A")   // numbersPub: 1,2,3  lettersPub: "A"   zip output: "A"
lettersPub.send("B")   // numbersPub: 2,3    lettersPub: "B"   zip output: "BB"
// Prints:
//  A
//  BB
```

If either upstream publisher finishes successfully or fails with an error, the zipped publisher does the same.

## Parameters

- `other`: Another publisher.
- `transform`: A closure that receives the most-recent value from each publisher and returns a new value to publish.

## See Also

- [func zip<P>(P) -> Publishers.Zip<Self, P>](publishers/ignoreoutput/zip(_:).md)
  Combines elements from another publisher and deliver pairs of elements as tuples.
- [func zip<P, Q>(P, Q) -> Publishers.Zip3<Self, P, Q>](publishers/ignoreoutput/zip(_:_:)-30wr9.md)
  Combines elements from two other publishers and delivers groups of elements as tuples.
- [func zip<P, Q, T>(P, Q, (Self.Output, P.Output, Q.Output) -> T) -> Publishers.Map<Publishers.Zip3<Self, P, Q>, T>](publishers/ignoreoutput/zip(_:_:_:)-1are0.md)
  Combines elements from two other publishers and delivers a transformed output.
- [func zip<P, Q, R>(P, Q, R) -> Publishers.Zip4<Self, P, Q, R>](publishers/ignoreoutput/zip(_:_:_:)-7bogz.md)
  Combines elements from three other publishers and delivers groups of elements as tuples.
- [func zip<P, Q, R, T>(P, Q, R, (Self.Output, P.Output, Q.Output, R.Output) -> T) -> Publishers.Map<Publishers.Zip4<Self, P, Q, R>, T>](publishers/ignoreoutput/zip(_:_:_:_:).md)
  Combines elements from three other publishers and delivers a transformed output.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/ignoreoutput/zip(_:_:)-8byjb)*