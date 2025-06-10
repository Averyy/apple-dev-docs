# drop(untilOutputFrom:)

**Framework**: Swift  
**Kind**: method

Ignores elements from the upstream publisher until it receives an element from a second publisher.

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
func drop<P>(untilOutputFrom publisher: P) -> Publishers.DropUntilOutput<Self, P> where P : Publisher, Self.Failure == P.Failure
```

#### Return Value

A publisher that drops elements from the upstream publisher until the `other` publisher produces a value.

#### Discussion

Use [`drop(untilOutputFrom:)`](result/publisher-swift.struct/drop(untiloutputfrom:).md) to ignore elements from the upstream publisher until another, second, publisher delivers its first element. This publisher requests a single value from the second publisher, and it ignores (drops) all elements from the upstream publisher until the second publisher produces a value. After the second publisher produces an element, [`drop(untilOutputFrom:)`](result/publisher-swift.struct/drop(untiloutputfrom:).md) cancels its subscription to the second publisher, and allows events from the upstream publisher to pass through.

After this publisher receives a subscription from the upstream publisher, it passes through backpressure requests from downstream to the upstream publisher. If the upstream publisher acts on those requests before the other publisher produces an item, this publisher drops the elements it receives from the upstream publisher.

In the example below, the `pub1` publisher defers publishing its elements until the `pub2` publisher delivers its first element:

```swift
let upstream = PassthroughSubject<Int,Never>()
let second = PassthroughSubject<String,Never>()
cancellable = upstream
    .drop(untilOutputFrom: second)
    .sink { print("\($0)", terminator: " ") }

upstream.send(1)
upstream.send(2)
second.send("A")
upstream.send(3)
upstream.send(4)
// Prints "3 4"
```

## Parameters

- `publisher`: A publisher to monitor for its first emitted element.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/result/publisher-swift.struct/drop(untiloutputfrom:))*