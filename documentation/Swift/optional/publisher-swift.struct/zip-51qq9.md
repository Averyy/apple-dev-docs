# zip(_:_:)

**Framework**: Swift  
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

Use `Publisher/zip(_:_:)-4xn21` to return a new publisher that combines the elements from two publishers using a transformation you specify to publish a new value to the downstream.  The returned publisher waits until both publishers have emitted an event, then delivers the oldest unconsumed event from each publisher together that the operator uses in the transformation.

In this example, `PassthroughSubject` instances `numbersPub` and `lettersPub` emit values; `Publisher/zip(_:_:)-4xn21` receives the oldest value from each publisher, uses the `Int` from `numbersPub` and publishes a string that repeats the [`String`](String.md) from `lettersPub` that many times.

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/optional/publisher-swift.struct/zip(_:_:)-51qq9)*