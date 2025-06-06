# init(_:)

**Framework**: Combine  
**Kind**: init

Creates a publisher that exposes elements received from an upstream publisher as a throwing asynchronous sequence.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
init(_ publisher: P)
```

## Parameters

- `publisher`: An upstream publisher. The asynchronous publisher converts elements received from this publisher into an asynchronous sequence.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/asyncthrowingpublisher/init(_:))*