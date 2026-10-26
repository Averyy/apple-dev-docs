---
url: "https://swiftpackageindex.com/apple/swift-async-algorithms/main/documentation/asyncalgorithms/multiproducersingleconsumerasyncchannel/source/send(contentsof:)-3baoz"
framework: "swift-async-algorithms/AsyncAlgorithms"
---

# send(contentsOf:)

**Framework**: swift-async-algorithms/AsyncAlgorithms  
**Kind**: method  
**Role**: Instance Method

Sends new elements to the channel.

**Availability**:
- iOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
mutating func send<S>(contentsOf sequence: consuming sending S) throws -> MultiProducerSingleConsumerAsyncChannel<Element, Failure>.Source.SendResult where Element == S.Element, S : Sequence
```

#### Return Value

The result that indicates if more elements should be produced at this time.

#### Discussion

If there is a task consuming the channel and awaiting the next element then the task will get resumed with the first element of the provided sequence. If the channel already terminated then this method will throw an error indicating the failure.

## Parameters

- `sequence`: The elements to send to the channel.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-async-algorithms/main/documentation/asyncalgorithms/multiproducersingleconsumerasyncchannel/source/send(contentsof:)-3baoz)*