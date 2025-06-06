# combineLatest(_:_:_:)

**Framework**: Combine  
**Kind**: method

Subscribes to two additional publishers and invokes a closure upon receiving output from any of the publishers.

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
func combineLatest<P, Q, T>(_ publisher1: P, _ publisher2: Q, _ transform: @escaping (Self.Output, P.Output, Q.Output) -> T) -> Publishers.Map<Publishers.CombineLatest3<Self, P, Q>, T> where P : Publisher, Q : Publisher, Self.Failure == P.Failure, P.Failure == Q.Failure
```

#### Return Value

A publisher that receives and combines elements from this publisher and two other publishers.

#### Discussion

Use `combineLatest<P, Q>(_:,_:)` to combine the current and two additional publishers and transform them using a closure you specify to publish a new value to the downstream.

> 💡 **Tip**: The combined publisher doesn’t produce elements until each of its upstream publishers publishes at least one element.

The combined publisher doesn’t produce elements until each of its upstream publishers publishes at least one element.

The combined publisher passes through any requests to  upstream publishers. However, it still obeys the demand-fulfilling rule of only sending the request amount downstream. If the demand isn’t `.unlimited`, it drops values from upstream publishers. It implements this by using a buffer size of 1 for each upstream, and holds the most-recent value in each buffer. All upstream publishers need to finish for this publisher to finish. If an upstream publisher never publishes a value, this publisher never finishes. If any of the combined publishers terminates with a failure, this publisher also fails.

In the example below, `combineLatest()` receives the most-recent values published by three publishers, multiplies them together, and republishes the result:

```swift
let pub = PassthroughSubject<Int, Never>()
let pub2 = PassthroughSubject<Int, Never>()
let pub3 = PassthroughSubject<Int, Never>()

cancellable = pub
    .combineLatest(pub2, pub3) { firstValue, secondValue, thirdValue in
        return firstValue * secondValue * thirdValue
    }
    .sink { print("Result: \($0).") }

pub.send(1)
pub.send(2)
pub2.send(2)
pub3.send(10)

pub.send(9)
pub3.send(4)
pub2.send(12)

// Prints:
//  Result: 40.     // pub = 2, pub2 = 2, pub3 = 10
//  Result: 180.    // pub = 9, pub2 = 2, pub3 = 10
//  Result: 72.     // pub = 9, pub2 = 2, pub3 = 4
//  Result: 432.    // pub = 9, pub2 = 12, pub3 = 4
```

## Parameters

- `publisher1`: A second publisher to combine with the first publisher.
- `publisher2`: A third publisher to combine with the first publisher.
- `transform`: A closure that receives the most-recent value from each publisher and returns a new value to publish.

## See Also

- [func combineLatest<P, T>(P, (Self.Output, P.Output) -> T) -> Publishers.Map<Publishers.CombineLatest<Self, P>, T>](publishers/merge7/combinelatest(_:_:)-6lu7p.md)
  Subscribes to an additional publisher and invokes a closure upon receiving output from either publisher.
- [func combineLatest<P>(P) -> Publishers.CombineLatest<Self, P>](publishers/merge7/combinelatest(_:).md)
  Subscribes to an additional publisher and publishes a tuple upon receiving output from either publisher.
- [func combineLatest<P, Q>(P, Q) -> Publishers.CombineLatest3<Self, P, Q>](publishers/merge7/combinelatest(_:_:)-9kuzr.md)
  Subscribes to two additional publishers and publishes a tuple upon receiving output from any of the publishers.
- [func combineLatest<P, Q, R, T>(P, Q, R, (Self.Output, P.Output, Q.Output, R.Output) -> T) -> Publishers.Map<Publishers.CombineLatest4<Self, P, Q, R>, T>](publishers/merge7/combinelatest(_:_:_:_:).md)
  Subscribes to three additional publishers and invokes a closure upon receiving output from any of the publishers.
- [func combineLatest<P, Q, R>(P, Q, R) -> Publishers.CombineLatest4<Self, P, Q, R>](publishers/merge7/combinelatest(_:_:_:)-78psy.md)
  Subscribes to three additional publishers and publishes a tuple upon receiving output from any of the publishers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/merge7/combinelatest(_:_:_:)-4yta7)*