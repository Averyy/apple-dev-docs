# combineLatest(_:_:)

**Framework**: Combine  
**Kind**: method

Subscribes to an additional publisher and invokes a closure upon receiving output from either publisher.

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
func combineLatest<P, T>(_ other: P, _ transform: @escaping (Self.Output, P.Output) -> T) -> Publishers.Map<Publishers.CombineLatest<Self, P>, T> where P : Publisher, Self.Failure == P.Failure
```

#### Return Value

A publisher that receives and combines elements from this and another publisher.

#### Discussion

Use `combineLatest<P,T>(_:)` to combine the current and one additional publisher and transform them using a closure you specify to publish a new value to the downstream.

> 💡 **Tip**: The combined publisher doesn’t produce elements until each of its upstream publishers publishes at least one element.

The combined publisher passes through any requests to  upstream publishers. However, it still obeys the demand-fulfilling rule of only sending the request amount downstream. If the demand isn’t `.unlimited`, it drops values from upstream publishers. It implements this by using a buffer size of 1 for each upstream, and holds the most-recent value in each buffer.

In the example below, `combineLatest()` receives the most-recent values published by the two publishers, it multiplies them together, and republishes the result:

```swift
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

- [func combineLatest<P>(P) -> Publishers.CombineLatest<Self, P>](publishers/merge6/combinelatest(_:).md)
  Subscribes to an additional publisher and publishes a tuple upon receiving output from either publisher.
- [func combineLatest<P, Q, T>(P, Q, (Self.Output, P.Output, Q.Output) -> T) -> Publishers.Map<Publishers.CombineLatest3<Self, P, Q>, T>](publishers/merge6/combinelatest(_:_:_:)-4ysy7.md)
  Subscribes to two additional publishers and invokes a closure upon receiving output from any of the publishers.
- [func combineLatest<P, Q>(P, Q) -> Publishers.CombineLatest3<Self, P, Q>](publishers/merge6/combinelatest(_:_:)-9kvbr.md)
  Subscribes to two additional publishers and publishes a tuple upon receiving output from any of the publishers.
- [func combineLatest<P, Q, R, T>(P, Q, R, (Self.Output, P.Output, Q.Output, R.Output) -> T) -> Publishers.Map<Publishers.CombineLatest4<Self, P, Q, R>, T>](publishers/merge6/combinelatest(_:_:_:_:).md)
  Subscribes to three additional publishers and invokes a closure upon receiving output from any of the publishers.
- [func combineLatest<P, Q, R>(P, Q, R) -> Publishers.CombineLatest4<Self, P, Q, R>](publishers/merge6/combinelatest(_:_:_:)-78q50.md)
  Subscribes to three additional publishers and publishes a tuple upon receiving output from any of the publishers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/merge6/combinelatest(_:_:)-6luh5)*