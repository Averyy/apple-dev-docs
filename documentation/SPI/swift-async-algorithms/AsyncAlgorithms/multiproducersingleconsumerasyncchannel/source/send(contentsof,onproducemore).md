---
url: "https://swiftpackageindex.com/apple/swift-async-algorithms/main/documentation/asyncalgorithms/multiproducersingleconsumerasyncchannel/source/send(contentsof:onproducemore:)"
framework: "swift-async-algorithms/AsyncAlgorithms"
---

# send(contentsOf:onProduceMore:)

**Framework**: swift-async-algorithms/AsyncAlgorithms  
**Kind**: method  
**Role**: Instance Method

Send new elements to the channel and provide a callback which will be invoked once more elements should be produced.

**Availability**:
- iOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
mutating func send<S>(contentsOf sequence: consuming sending S, onProduceMore: @escaping @Sendable (Result<Void, any Error>) -> Void) where Element == S.Element, S : Sequence
```

#### Discussion

If there is a task consuming the channel and awaiting the next element then the task will get resumed with the first element of the provided sequence. If the channel already terminated then `onProduceMore` will be invoked with a `Result.failure`.

## Parameters

- `sequence`: The elements to send to the channel.
- `onProduceMore`: The callback which gets invoked once more elements should be produced. This callback might be invoked during the call to [`send(contentsOf:onProduceMore:)`](./send%28contentsof,onproducemore%29.md).


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-async-algorithms/main/documentation/asyncalgorithms/multiproducersingleconsumerasyncchannel/source/send(contentsof:onproducemore:))*