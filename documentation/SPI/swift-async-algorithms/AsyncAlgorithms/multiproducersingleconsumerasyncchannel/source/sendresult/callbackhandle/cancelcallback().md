---
url: "https://swiftpackageindex.com/apple/swift-async-algorithms/main/documentation/asyncalgorithms/multiproducersingleconsumerasyncchannel/source/sendresult/callbackhandle/cancelcallback()"
framework: "swift-async-algorithms/AsyncAlgorithms"
---

# cancelCallback()

**Framework**: swift-async-algorithms/AsyncAlgorithms  
**Kind**: method  
**Role**: Instance Method

Cancel an enqueued callback.

**Availability**:
- iOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
mutating func cancelCallback()
```

#### Discussion

> **Note**: This methods supports being called before [`enqueueCallback(onProduceMore:)`](./enqueuecallback%28onproducemore%29.md) is called.

> ❗ **Important**: Calling enqueue more than once is **not allowed**.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-async-algorithms/main/documentation/asyncalgorithms/multiproducersingleconsumerasyncchannel/source/sendresult/callbackhandle/cancelcallback())*