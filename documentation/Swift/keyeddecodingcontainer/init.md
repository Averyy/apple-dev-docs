# init(_:)

**Framework**: Swift  
**Kind**: init

Creates a new instance with the given container.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
init<Container>(_ container: Container) where K == Container.Key, Container : KeyedDecodingContainerProtocol
```

## Parameters

- `container`: The container to hold.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/keyeddecodingcontainer/init(_:))*