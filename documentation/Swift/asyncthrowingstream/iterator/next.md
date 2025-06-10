# next()

**Framework**: Swift  
**Kind**: method

The next value from the asynchronous stream.

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
mutating func next() async throws -> Element?
```

#### Discussion

When `next()` returns `nil`, this signifies the end of the `AsyncThrowingStream`.

It is a programmer error to invoke `next()` from a concurrent context that contends with another such call, which results in a call to `fatalError()`.

If you cancel the task this iterator is running in while `next()` is awaiting a value, the `AsyncThrowingStream` terminates. In this case, `next()` may return `nil` immediately, or else return `nil` on subsequent calls.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/asyncthrowingstream/iterator/next())*