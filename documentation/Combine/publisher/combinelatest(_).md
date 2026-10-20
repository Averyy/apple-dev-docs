# combineLatest(_:)

**Framework**: Combine  
**Kind**: method  
**Role**: Instance Method

Subscribes to an additional publisher and publishes a tuple upon receiving output from either publisher.

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
func combineLatest<P>(_ other: P) -> Publishers.CombineLatest<Self, P> where P : Publisher, Self.Failure == P.Failure
```

#### Return Value

A publisher that receives and combines elements from this and another publisher.

#### Discussion

Use [`combineLatest(_:)`](./combinelatest%28_%29.md) when you want the downstream subscriber to receive a tuple of the most-recent element from multiple publishers when any of them emit a value. To pair elements from multiple publishers, use [`zip(_:)`](./zip%28_%29.md) instead. To receive just the most-recent element from multiple publishers rather than tuples, use [`merge(with:)`](./merge%28with%29-7qt71.md).

> 💡 **Tip**: The combined publisher doesn’t produce elements until each of its upstream publishers publishes at least one element.

The combined publisher passes through any requests to *all* upstream publishers. However, it still obeys the demand-fulfilling rule of only sending the request amount downstream. If the demand isn’t [`unlimited`](../subscribers/demand/unlimited.md), it drops values from upstream publishers. It implements this by using a buffer size of 1 for each upstream, and holds the most-recent value in each buffer.

In this example, [`PassthroughSubject`](../passthroughsubject.md) `pub1` and also `pub2` emit values; as [`combineLatest(_:)`](./combinelatest%28_%29.md) receives input from either upstream publisher, it combines the latest value from each publisher into a tuple and publishes it.

```swift
let pub1 = PassthroughSubject<Int, Never>()
let pub2 = PassthroughSubject<Int, Never>()

cancellable = pub1
    .combineLatest(pub2)
    .sink { print("Result: \($0).") }

pub1.send(1)
pub1.send(2)
pub2.send(2)
pub1.send(3)
pub1.send(45)
pub2.send(22)

// Prints:
//    Result: (2, 2).    // pub1 latest = 2, pub2 latest = 2
//    Result: (3, 2).    // pub1 latest = 3, pub2 latest = 2
//    Result: (45, 2).   // pub1 latest = 45, pub2 latest = 2
//    Result: (45, 22).  // pub1 latest = 45, pub2 latest = 22
```

When all upstream publishers finish, this publisher finishes. If an upstream publisher never publishes a value, this publisher never finishes.

## Parameters

- `other`: Another publisher to combine with this one.

## See Also

### Collecting and republishing the latest elements from multiple publishers
- [func combineLatest<P, T>(P, (Self.Output, P.Output) -> T) -> Publishers.Map<Publishers.CombineLatest<Self, P>, T>](./combinelatest%28_,_%29-1n30g.md)
  Subscribes to an additional publisher and invokes a closure upon receiving output from either publisher.
- [func combineLatest<P, Q, T>(P, Q, (Self.Output, P.Output, Q.Output) -> T) -> Publishers.Map<Publishers.CombineLatest3<Self, P, Q>, T>](./combinelatest%28_,_,_%29-6ekpz.md)
  Subscribes to two additional publishers and invokes a closure upon receiving output from any of the publishers.
- [func combineLatest<P, Q>(P, Q) -> Publishers.CombineLatest3<Self, P, Q>](./combinelatest%28_,_%29-5crqg.md)
  Subscribes to two additional publishers and publishes a tuple upon receiving output from any of the publishers.
- [func combineLatest<P, Q, R, T>(P, Q, R, (Self.Output, P.Output, Q.Output, R.Output) -> T) -> Publishers.Map<Publishers.CombineLatest4<Self, P, Q, R>, T>](./combinelatest%28_,_,_,_%29.md)
  Subscribes to three additional publishers and invokes a closure upon receiving output from any of the publishers.
- [func combineLatest<P, Q, R>(P, Q, R) -> Publishers.CombineLatest4<Self, P, Q, R>](./combinelatest%28_,_,_%29-48buc.md)
  Subscribes to three additional publishers and publishes a tuple upon receiving output from any of the publishers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publisher/combinelatest(_:))*