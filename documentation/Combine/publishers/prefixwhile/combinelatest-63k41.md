# combineLatest(_:_:)

**Framework**: Combine  
**Kind**: method

Subscribes to two additional publishers and publishes a tuple upon receiving output from any of the publishers.

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
func combineLatest<P, Q>(_ publisher1: P, _ publisher2: Q) -> Publishers.CombineLatest3<Self, P, Q> where P : Publisher, Q : Publisher, Self.Failure == P.Failure, P.Failure == Q.Failure
```

#### Return Value

A publisher that receives and combines elements from this publisher and two other publishers.

#### Discussion

Use [`combineLatest(_:_:)`](publisher/combinelatest(_:_:)-5crqg.md) when you want the downstream subscriber to receive a tuple of the most-recent element from multiple publishers when any of them emit a value. To combine elements from multiple publishers, use [`zip(_:_:)`](publisher/zip(_:_:)-8d7k7.md) instead. To receive just the most-recent element from multiple publishers rather than tuples, use [`merge(with:_:)`](publisher/merge(with:_:).md).

> 💡 **Tip**: The combined publisher doesn’t produce elements until each of its upstream publishers publishes at least one element.

The combined publisher doesn’t produce elements until each of its upstream publishers publishes at least one element.

The combined publisher passes through any requests to  upstream publishers. However, it still obeys the demand-fulfilling rule of only sending the request amount downstream. If the demand isn’t [`unlimited`](subscribers/demand/unlimited.md), it drops values from upstream publishers. It implements this by using a buffer size of 1 for each upstream, and holds the most-recent value in each buffer.

All upstream publishers need to finish for this publisher to finish. If an upstream publisher never publishes a value, this publisher never finishes.

In this example, three instances of [`PassthroughSubject`](passthroughsubject.md) emit values; as [`combineLatest(_:_:)`](publisher/combinelatest(_:_:)-5crqg.md) receives input from any of the upstream publishers, it combines the latest value from each publisher into a tuple and publishes it:

```swift
let pub = PassthroughSubject<Int, Never>()
let pub2 = PassthroughSubject<Int, Never>()
let pub3 = PassthroughSubject<Int, Never>()

cancellable = pub
    .combineLatest(pub2, pub3)
    .sink { print("Result: \($0).") }

pub.send(1)
pub.send(2)
pub2.send(2)
pub3.send(9)

pub.send(3)
pub2.send(12)
pub.send(13)
pub3.send(19)

// Prints:
//  Result: (2, 2, 9).
//  Result: (3, 2, 9).
//  Result: (3, 12, 9).
//  Result: (13, 12, 9).
//  Result: (13, 12, 19).
```

If any of the combined publishers terminates with a failure, this publisher also fails.

## Parameters

- `publisher1`: A second publisher to combine with the first publisher.
- `publisher2`: A third publisher to combine with the first publisher.

## See Also

- [func combineLatest<P, T>(P, (Self.Output, P.Output) -> T) -> Publishers.Map<Publishers.CombineLatest<Self, P>, T>](publishers/prefixwhile/combinelatest(_:_:)-8xjvh.md)
  Subscribes to an additional publisher and invokes a closure upon receiving output from either publisher.
- [func combineLatest<P>(P) -> Publishers.CombineLatest<Self, P>](publishers/prefixwhile/combinelatest(_:).md)
  Subscribes to an additional publisher and publishes a tuple upon receiving output from either publisher.
- [func combineLatest<P, Q, T>(P, Q, (Self.Output, P.Output, Q.Output) -> T) -> Publishers.Map<Publishers.CombineLatest3<Self, P, Q>, T>](publishers/prefixwhile/combinelatest(_:_:_:)-249ai.md)
  Subscribes to two additional publishers and invokes a closure upon receiving output from any of the publishers.
- [func combineLatest<P, Q, R, T>(P, Q, R, (Self.Output, P.Output, Q.Output, R.Output) -> T) -> Publishers.Map<Publishers.CombineLatest4<Self, P, Q, R>, T>](publishers/prefixwhile/combinelatest(_:_:_:_:).md)
  Subscribes to three additional publishers and invokes a closure upon receiving output from any of the publishers.
- [func combineLatest<P, Q, R>(P, Q, R) -> Publishers.CombineLatest4<Self, P, Q, R>](publishers/prefixwhile/combinelatest(_:_:_:)-1phg4.md)
  Subscribes to three additional publishers and publishes a tuple upon receiving output from any of the publishers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/prefixwhile/combinelatest(_:_:)-63k41)*