# init(_:)

**Framework**: Combine  
**Kind**: init

Creates a type-erasing publisher to wrap the provided publisher.

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
init<P>(_ publisher: P) where Output == P.Output, Failure == P.Failure, P : Publisher
```

## Parameters

- `publisher`: A publisher to wrap with a type-eraser.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/anypublisher/init(_:))*