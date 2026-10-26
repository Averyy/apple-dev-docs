---
url: "https://swiftpackageindex.com/apple/swift-async-algorithms/main/documentation/asyncalgorithms/multiproducersingleconsumerasyncchannel/source/sendresult/callbackhandle/enqueuecallback(onproducemore:)"
framework: "swift-async-algorithms/AsyncAlgorithms"
---

# enqueueCallback(onProduceMore:)

**Framework**: swift-async-algorithms/AsyncAlgorithms  
**Kind**: method  
**Role**: Instance Method

Enqueues a callback that will be invoked once more elements should be produced.

**Availability**:
- iOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
mutating func enqueueCallback(onProduceMore: sending @escaping (Result<Void, any Error>) -> Void)
```

#### Discussion

> ❗ **Important**: Calling enqueue more than once is **not allowed**.

## Parameters

- `onProduceMore`: The callback which gets invoked once more elements should be produced.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-async-algorithms/main/documentation/asyncalgorithms/multiproducersingleconsumerasyncchannel/source/sendresult/callbackhandle/enqueuecallback(onproducemore:))*