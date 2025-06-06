# init(unfolding:onCancel:)

**Framework**: Swift  
**Kind**: init

Constructs an asynchronous stream from a given element-producing closure, with an optional closure to handle cancellation.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
@preconcurrency
init(unfolding produce: @escaping () async -> Element?, onCancel: (() -> Void)? = nil)
```

#### Discussion

Use this convenience initializer when you have an asynchronous function that can produce elements for the stream, and don’t want to invoke a continuation manually. This initializer “unfolds” your closure into an asynchronous stream. The created stream handles conformance to the `AsyncSequence` protocol automatically, including termination (either by cancellation or by returning `nil` from the closure to finish iteration).

The following example shows an `AsyncStream` created with this initializer that produces random numbers on a one-second interval. This example uses the Swift multiple trailing closure syntax, which omits the `unfolding` parameter label.

```swift
let stream = AsyncStream<Int> {
    await Task.sleep(1 * 1_000_000_000)
    return Int.random(in: 1...10)
} onCancel: { @Sendable () in print("Canceled.") }

// Call point:
for await random in stream {
    print(random)
}
```

## Parameters

- `produce`: A closure that asynchronously produces elements for the   stream.
- `onCancel`: A closure to execute when canceling the stream’s task.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/asyncstream/init(unfolding:oncancel:))*