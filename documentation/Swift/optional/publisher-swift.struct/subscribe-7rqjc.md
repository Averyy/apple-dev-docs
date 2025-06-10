# subscribe(_:)

**Framework**: Swift  
**Kind**: method

Attaches the specified subscriber to this publisher.

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
func subscribe<S>(_ subscriber: S) where S : Subscriber, Self.Failure == S.Failure, Self.Output == S.Input
```

#### Discussion

Always call this function instead of [`receive(subscriber:)`](optional/publisher-swift.struct/receive(subscriber:).md). Adopters of [`Optional.Publisher`](optional/publisher-swift.struct.md) must implement [`receive(subscriber:)`](optional/publisher-swift.struct/receive(subscriber:).md). The implementation of `Publisher/subscribe(_:)-4u8kn` provided by [`Optional.Publisher`](optional/publisher-swift.struct.md) calls through to [`receive(subscriber:)`](optional/publisher-swift.struct/receive(subscriber:).md).

## Parameters

- `subscriber`: The subscriber to attach to this publisher. After attaching, the subscriber can start to receive values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/optional/publisher-swift.struct/subscribe(_:)-7rqjc)*