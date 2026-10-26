---
url: "https://swiftpackageindex.com/apple/swift-async-algorithms/main/documentation/asyncalgorithms/multiproducersingleconsumerasyncchannel/channelandstream/takechannel()"
framework: "swift-async-algorithms/AsyncAlgorithms"
---

# takeChannel()

**Framework**: swift-async-algorithms/AsyncAlgorithms  
**Kind**: method  
**Role**: Instance Method

Takes and returns the channel.

**Availability**:
- iOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
mutating func takeChannel() -> sending MultiProducerSingleConsumerAsyncChannel<Element, Failure>
```

#### Discussion

> ❗ **Important**: If this is called more than once it will result in a runtime crash.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-async-algorithms/main/documentation/asyncalgorithms/multiproducersingleconsumerasyncchannel/channelandstream/takechannel())*