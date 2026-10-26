---
url: "https://swiftpackageindex.com/apple/swift-async-algorithms/main/documentation/asyncalgorithms/multiproducersingleconsumerasyncchannel/source/send(contentsof:)-1h7t9"
framework: "swift-async-algorithms/AsyncAlgorithms"
---

# send(contentsOf:)

**Framework**: swift-async-algorithms/AsyncAlgorithms  
**Kind**: method  
**Role**: Instance Method

Send new elements to the channel.

**Availability**:
- iOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
nonisolated
(nonsending) mutating func send<S>(contentsOf sequence: consuming sending S) async throws where Element == S.Element, S : Sequence
```

#### Discussion

If there is a task consuming the channel and awaiting the next element then the task will get resumed with the first element of the provided sequence. If the channel already terminated then this method will throw an error indicating the failure.

This method returns once more elements should be produced.

## Parameters

- `sequence`: The elements to send to the channel.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-async-algorithms/main/documentation/asyncalgorithms/multiproducersingleconsumerasyncchannel/source/send(contentsof:)-1h7t9)*