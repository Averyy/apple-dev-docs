# buffer(size:prefetch:whenFull:)

**Framework**: RealityKit  
**Kind**: method

Buffers elements received from an upstream publisher.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst ?+
- macOS 10.15+
- tvOS 13.0+
- visionOS ?+
- watchOS 6.0+

## Declaration

```swift
func buffer(size: Int, prefetch: Publishers.PrefetchStrategy, whenFull: Publishers.BufferingStrategy<Self.Failure>) -> Publishers.Buffer<Self>
```

#### Return Value

A publisher that buffers elements received from an upstream publisher.

#### Discussion

Use `Publisher/buffer(size:prefetch:whenFull:)` to collect a specific number of elements from an upstream publisher before republishing them to the downstream subscriber according to the `Publishers/BufferingStrategy` and `Publishers/PrefetchStrategy` strategy you specify.

If the publisher completes before reaching the `size` threshold, it buffers the elements and publishes them downstream prior to completion.

## Parameters

- `size`: The maximum number of elements to store.
- `prefetch`: The strategy to initially populate the buffer.
- `whenFull`: The action to take when the buffer becomes full.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/loadrequest/buffer(size:prefetch:whenfull:))*