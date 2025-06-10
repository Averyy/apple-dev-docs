# receive(subscriber:)

**Framework**: Combine  
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
func receive<S>(subscriber: S) where S : Subscriber, C.Failure == S.Failure, S.Input == (A.Output, B.Output, C.Output)
```

#### Discussion

Implementations of [`Publisher`](publisher.md) must implement this method.

The provided implementation of [`subscribe(_:)`](publisher/subscribe(_:)-4u8kn.md)calls this method.

## Parameters

- `subscriber`: The subscriber to attach to this  , after which it can receive values.

## See Also

- [func subscribe<S>(S)](publishers/zip3/subscribe(_:)-2a594.md)
  Attaches the specified subscriber to this publisher.
- [func subscribe<S>(S) -> AnyCancellable](publishers/zip3/subscribe(_:)-4ipjy.md)
  Attaches the specified subject to this publisher.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/zip3/receive(subscriber:))*