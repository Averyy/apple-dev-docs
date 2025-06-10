# subscribe(_:)

**Framework**: Swift  
**Kind**: method

Attaches the specified subject to this publisher.

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
func subscribe<S>(_ subject: S) -> AnyCancellable where S : Subject, Self.Failure == S.Failure, Self.Output == S.Output
```

## Parameters

- `subject`: The subject to attach to this publisher.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/result/publisher-swift.struct/subscribe(_:)-7c5ul)*