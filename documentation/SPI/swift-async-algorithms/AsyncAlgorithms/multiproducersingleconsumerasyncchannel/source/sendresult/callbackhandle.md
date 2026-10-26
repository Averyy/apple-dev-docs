---
url: "https://swiftpackageindex.com/apple/swift-async-algorithms/main/documentation/asyncalgorithms/multiproducersingleconsumerasyncchannel/source/sendresult/callbackhandle"
framework: "swift-async-algorithms/AsyncAlgorithms"
---

# MultiProducerSingleConsumerAsyncChannel.Source.SendResult.CallbackHandle

**Framework**: swift-async-algorithms/AsyncAlgorithms  
**Kind**: struct  
**Role**: Structure

A handle that is returned when the channel’s backpressure strategy indicated that production should be suspended. Use this handle to enqueue a callback by  calling the [`enqueueCallback(onProduceMore:)`](./callbackhandle/enqueuecallback%28onproducemore%29.md) method.

**Availability**:
- iOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
struct CallbackHandle
```

#### Overview

> ❗ **Important**: [`enqueueCallback(onProduceMore:)`](./callbackhandle/enqueuecallback%28onproducemore%29.md) and [`cancelCallback()`](./callbackhandle/cancelcallback%28%29.md) must only be called once.

## Topics

### Operators
- [static func == (MultiProducerSingleConsumerAsyncChannel<Element, Failure>.Source.SendResult.CallbackHandle, MultiProducerSingleConsumerAsyncChannel<Element, Failure>.Source.SendResult.CallbackHandle) -> Bool](./callbackhandle/eqeq%28_,_%29.md)
### Instance Methods
- [func cancelCallback()](./callbackhandle/cancelcallback%28%29.md)
  Cancel an enqueued callback.
- [func enqueueCallback(onProduceMore: sending (Result<Void, any Error>) -> Void)](./callbackhandle/enqueuecallback%28onproducemore%29.md)
  Enqueues a callback that will be invoked once more elements should be produced.
- [func hash(into: inout Hasher)](./callbackhandle/hash%28into%29.md)
### Default Implementations
- [Equatable Implementations](./callbackhandle/equatable-implementations.md)

## Relationships

### Conforms To
- Swift.Equatable
- Swift.Hashable
- Swift.Sendable
- Swift.SendableMetatype


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-async-algorithms/main/documentation/asyncalgorithms/multiproducersingleconsumerasyncchannel/source/sendresult/callbackhandle)*