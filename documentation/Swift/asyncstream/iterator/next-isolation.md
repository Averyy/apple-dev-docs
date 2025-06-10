# next(isolation:)

**Framework**: Swift  
**Kind**: method

The next value from the asynchronous stream.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
mutating func next(isolation actor: isolated (any Actor)?) async -> Element?
```

#### Discussion

When `next()` returns `nil`, this signifies the end of the `AsyncStream`.

It is a programmer error to invoke `next()` from a concurrent context that contends with another such call, which results in a call to `fatalError()`.

If you cancel the task this iterator is running in while `next()` is awaiting a value, the `AsyncStream` terminates. In this case, `next()` might return `nil` immediately, or return `nil` on subsequent calls.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/asyncstream/iterator/next(isolation:))*