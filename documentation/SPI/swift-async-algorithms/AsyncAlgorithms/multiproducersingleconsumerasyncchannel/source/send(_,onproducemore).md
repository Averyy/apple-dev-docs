---
url: "https://swiftpackageindex.com/apple/swift-async-algorithms/main/documentation/asyncalgorithms/multiproducersingleconsumerasyncchannel/source/send(_:onproducemore:)"
framework: "swift-async-algorithms/AsyncAlgorithms"
---

# send(_:onProduceMore:)

**Framework**: swift-async-algorithms/AsyncAlgorithms  
**Kind**: method  
**Role**: Instance Method

Sends the element to the channel.

**Availability**:
- iOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
mutating func send(_ element: consuming sending Element, onProduceMore: @escaping @Sendable (Result<Void, any Error>) -> Void)
```

#### Discussion

If there is a task consuming the channel and awaiting the next element then the task will get resumed with the provided element. If the channel already terminated then `onProduceMore` will be invoked with a `Result.failure`.

## Parameters

- `element`: The element to send to the channel.
- `onProduceMore`: The callback which gets invoked once more elements should be produced. This callback might be invoked during the call to [`send(_:onProduceMore:)`](./send%28_,onproducemore%29.md).


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-async-algorithms/main/documentation/asyncalgorithms/multiproducersingleconsumerasyncchannel/source/send(_:onproducemore:))*