# AsyncThrowingStream.Continuation.Termination.finished(_:)

**Framework**: Swift  
**Kind**: case

The stream finished as a result of calling the continuation’s `finish` method.

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
case finished(Failure?)
```

#### Discussion

The associated `Failure` value provides the error that terminated the stream. If no error occurred, this value is `nil`.

## See Also

- [AsyncThrowingStream.Continuation.Termination.cancelled](asyncthrowingstream/continuation/termination/cancelled.md)
  The stream finished as a result of cancellation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/asyncthrowingstream/continuation/termination/finished(_:))*