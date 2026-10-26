---
url: "https://swiftpackageindex.com/apple/swift-async-algorithms/main/documentation/asyncalgorithms/multiproducersingleconsumerasyncchannel/source/send(_:)-5rwh7"
framework: "swift-async-algorithms/AsyncAlgorithms"
---

# send(_:)

**Framework**: swift-async-algorithms/AsyncAlgorithms  
**Kind**: method  
**Role**: Instance Method

Send new element to the channel.

**Availability**:
- iOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
nonisolated
(nonsending) mutating func send(_ element: consuming sending Element) async throws
```

#### Discussion

If there is a task consuming the channel and awaiting the next element then the task will get resumed with the provided element. If the channel already terminated then this method will throw an error indicating the failure.

This method returns once more elements should be produced.

## Parameters

- `element`: The element to send to the channel.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-async-algorithms/main/documentation/asyncalgorithms/multiproducersingleconsumerasyncchannel/source/send(_:)-5rwh7)*