---
url: "https://swiftpackageindex.com/apple/swift-async-algorithms/main/documentation/asyncalgorithms/multiproducersingleconsumerasyncchannel/source/makeadditionalsource()"
framework: "swift-async-algorithms/AsyncAlgorithms"
---

# makeAdditionalSource()

**Framework**: swift-async-algorithms/AsyncAlgorithms  
**Kind**: method  
**Role**: Instance Method

Creates a new source which can be used to send elements to the channel concurrently.

**Availability**:
- iOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
mutating func makeAdditionalSource() -> sending MultiProducerSingleConsumerAsyncChannel<Element, Failure>.Source
```

#### Return Value

A new source for sending elements to the channel.

#### Discussion

The channel will only automatically be finished if all existing sources have been deinited.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-async-algorithms/main/documentation/asyncalgorithms/multiproducersingleconsumerasyncchannel/source/makeadditionalsource())*