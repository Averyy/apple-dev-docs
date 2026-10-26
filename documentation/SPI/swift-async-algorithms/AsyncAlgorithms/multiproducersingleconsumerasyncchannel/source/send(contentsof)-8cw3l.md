---
url: "https://swiftpackageindex.com/apple/swift-async-algorithms/main/documentation/asyncalgorithms/multiproducersingleconsumerasyncchannel/source/send(contentsof:)-8cw3l"
framework: "swift-async-algorithms/AsyncAlgorithms"
---

# send(contentsOf:)

**Framework**: swift-async-algorithms/AsyncAlgorithms  
**Kind**: method  
**Role**: Instance Method

Send the elements of the asynchronous sequence to the channel.

**Availability**:
- iOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
nonisolated
(nonsending) mutating func send<S>(contentsOf sequence: consuming sending S) async throws where Element : Sendable, Element == S.Element, S : Sendable, S : AsyncSequence
```

#### Discussion

This method returns once the provided asynchronous sequence or the channel finished.

> ❗ **Important**: This method does not finish the source if consuming the upstream sequence terminated.

## Parameters

- `sequence`: The elements to send to the channel.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-async-algorithms/main/documentation/asyncalgorithms/multiproducersingleconsumerasyncchannel/source/send(contentsof:)-8cw3l)*