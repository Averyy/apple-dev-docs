# combineLatest(_:_:)

**Framework**: RealityKit  
**Kind**: method

Subscribes to an additional publisher and invokes a closure upon receiving output from either publisher.

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
func combineLatest<P, T>(_ other: P, _ transform: @escaping (Self.Output, P.Output) -> T) -> Publishers.Map<Publishers.CombineLatest<Self, P>, T> where P : Publisher, Self.Failure == P.Failure
```

#### Return Value

A publisher that receives and combines elements from this and another publisher.

#### Discussion

Use `combineLatest<P,T>(_:)` to combine the current and one additional publisher and transform them using a closure you specify to publish a new value to the downstream.

> 💡 **Tip**: The combined publisher doesn’t produce elements until each of its upstream publishers publishes at least one element.

The combined publisher doesn’t produce elements until each of its upstream publishers publishes at least one element.

The combined publisher passes through any requests to  upstream publishers. However, it still obeys the demand-fulfilling rule of only sending the request amount downstream. If the demand isn’t `.unlimited`, it drops values from upstream publishers. It implements this by using a buffer size of 1 for each upstream, and holds the most-recent value in each buffer.

In the example below, `combineLatest()` receives the most-recent values published by the two publishers, it multiplies them together, and republishes the result:

```None
let pub1 = PassthroughSubject<Int, Never>()
let pub2 = PassthroughSubject<Int, Never>()

cancellable = pub1
    .combineLatest(pub2) { (first, second) in
        return first * second
    }
    .sink { print("Result: \($0).") }

pub1.send(1)
pub1.send(2)
pub2.send(2)
pub1.send(9)
pub1.send(3)
pub2.send(12)
pub1.send(13)
//
// Prints:
//Result: 4.    (pub1 latest = 2, pub2 latest = 2)
//Result: 18.   (pub1 latest = 9, pub2 latest = 2)
//Result: 6.    (pub1 latest = 3, pub2 latest = 2)
//Result: 36.   (pub1 latest = 3, pub2 latest = 12)
//Result: 156.  (pub1 latest = 13, pub2 latest = 12)
```

All upstream publishers need to finish for this publisher to finish. If an upstream publisher never publishes a value, this publisher never finishes. If any of the combined publishers terminates with a failure, this publisher also fails.

## Parameters

- `other`: Another publisher to combine with this one.
- `transform`: A closure that receives the most-recent value from each publisher and returns a new value to publish.

## See Also

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
- [func zip<P, Q, T>(P, Q, (Self.Output, P.Output, Q.Output) -> T) -> Publishers.Map<Publishers.Zip3<Self, P, Q>, T>](loadrequest/zip(_:_:_:)-23ai8.md)
  Combines elements from two other publishers and delivers a transformed output.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/loadrequest/combinelatest(_:_:)-7ey7f)*