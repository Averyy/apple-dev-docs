# init(_:)

**Framework**: Combine  
**Kind**: init

Creates a type-erasing subscriber to wrap an existing subscriber.

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
init<S>(_ s: S) where Input == S.Output, Failure == S.Failure, S : Subject
```

## Parameters

- `s`: The subscriber to type-erase.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/anysubscriber/init(_:)-3t3eh)*