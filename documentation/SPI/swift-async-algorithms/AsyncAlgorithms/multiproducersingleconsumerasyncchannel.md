---
url: "https://swiftpackageindex.com/apple/swift-async-algorithms/main/documentation/asyncalgorithms/multiproducersingleconsumerasyncchannel"
framework: "swift-async-algorithms/AsyncAlgorithms"
---

# MultiProducerSingleConsumerAsyncChannel

**Framework**: swift-async-algorithms/AsyncAlgorithms  
**Kind**: struct  
**Role**: Structure

A multi-producer single-consumer channel.

**Availability**:
- iOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
struct MultiProducerSingleConsumerAsyncChannel<Element, Failure> where Failure : Error
```

## Overview

The [`MultiProducerSingleConsumerAsyncChannel`](./multiproducersingleconsumerasyncchannel.md) provides a [`MultiProducerSingleConsumerAsyncChannel.Source`](./multiproducersingleconsumerasyncchannel/source.md) to send values to the channel. The channel supports different back pressure strategies to control the buffering and demand. The channel will buffer values until its backpressure strategy decides that the producer have to wait.

This channel is also suitable for the single-producer single-consumer use-case

## Using a MultiProducerSingleConsumerAsyncChannel

To use a [`MultiProducerSingleConsumerAsyncChannel`](./multiproducersingleconsumerasyncchannel.md) you have to create a new channel with its source first by calling the [`makeChannel(of:throwing:backpressureStrategy:)`](./multiproducersingleconsumerasyncchannel/makechannel%28of,throwing,backpressurestrategy%29.md) method. Afterwards, you can pass the source to the producer and the channel to the consumer.

```
var channelAndSource = MultiProducerSingleConsumerAsyncChannel.makeChannel(
    of: Int.self,
    backpressureStrategy: .watermark(low: 2, high: 4)
)

// The channel and source can be extracted from the returned type
let channel = channelAndSource.takeChannel()
let source = consume channelAndSource.source
```

### Asynchronous producing

Values can be send to the source from asynchronous contexts using [`send(contentsOf:)`](./multiproducersingleconsumerasyncchannel/source/send%28contentsof%29-1h7t9.md) and [`send(_:)`](./multiproducersingleconsumerasyncchannel/source/send%28_%29-5rwh7.md). Backpressure results in calls to the `send` methods to be suspended. Once more elements should be produced the `send` methods will be resumed.

```
try await withThrowingTaskGroup(of: Void.self) { group in
    group.addTask {
        try await source.send(1)
        try await source.send(2)
        try await source.send(3)
    }

    for await element in channel {
        print(element)
    }
}
```

### Synchronous produceing

Values can also be send to the source from synchronous context. Backpressure is also exposed on the synchronous contexts; however, it is up to the caller to decide how to properly translate the backpressure to underlying producer e.g. by blocking the thread.

```swift
do {
    let sendResult = try source.send(contentsOf: sequence)

    switch sendResult {
    case .produceMore:
       // Trigger more production in the underlying system

    case .enqueueCallback(let callbackHandle):
        // There are enough values in the channel already. We need to enqueue
        // a callback to get notified when we should produce more.
        callbackHandle.enqueueCallback(onProduceMore: { result in
            switch result {
            case .success:
                // Trigger more production in the underlying system
            case .failure(let error):
                // Terminate the underlying producer
            }
        })
    }
} catch {
    // `send(contentsOf:)` throws if the channel already terminated
}
```

### Multiple producers

To support multiple producers the source offers a [`makeAdditionalSource()`](./multiproducersingleconsumerasyncchannel/source/makeadditionalsource%28%29.md) method to produce a new source.

### Terminating the production of values

The consumer can be terminated through multiple ways:

- Calling [`finish(throwing:)`](./multiproducersingleconsumerasyncchannel/source/finish%28throwing%29.md).
- Deiniting all sources.

In both cases, if there are still elements buffered by the channel, then the consumer will receive all buffered elements. Afterwards it will be terminated.

### Observing termination of the consumer

When the consumer stops consumption by either deiniting the channel or the task calling [`next(isolation:)`](./multiproducersingleconsumerasyncchannel/next%28isolation%29.md) getting cancelled, the source will get notified about the termination if a termination callback has been set before by calling [`setOnTerminationCallback(_:)`](./multiproducersingleconsumerasyncchannel/source/setonterminationcallback%28_%29.md).

## Topics

### Structures
- [MultiProducerSingleConsumerAsyncChannel.ChannelAndStream](./multiproducersingleconsumerasyncchannel/channelandstream.md)
  A struct containing the initialized channel and source.
- [MultiProducerSingleConsumerAsyncChannel.Source](./multiproducersingleconsumerasyncchannel/source.md)
  A struct to send values to the channel.
### Instance Methods
- [func elements() -> some Sendable & AsyncSequence<Element, Failure>
](./multiproducersingleconsumerasyncchannel/elements%28%29.md)
  Converts the channel to an asynchronous sequence for consumption.
- [func next(isolation: isolated (any Actor)?) async throws(Failure) -> Element?](./multiproducersingleconsumerasyncchannel/next%28isolation%29.md)
  Returns the next element.
### Type Methods
- [static func makeChannel(of: Element.Type, throwing: Failure.Type, backpressureStrategy: MultiProducerSingleConsumerAsyncChannel<Element, Failure>.Source.BackpressureStrategy) -> sending MultiProducerSingleConsumerAsyncChannel<Element, Failure>.ChannelAndStream](./multiproducersingleconsumerasyncchannel/makechannel%28of,throwing,backpressurestrategy%29.md)
  Initializes a new [`MultiProducerSingleConsumerAsyncChannel`](./multiproducersingleconsumerasyncchannel.md) and an [`MultiProducerSingleConsumerAsyncChannel.Source`](./multiproducersingleconsumerasyncchannel/source.md).


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-async-algorithms/main/documentation/asyncalgorithms/multiproducersingleconsumerasyncchannel)*