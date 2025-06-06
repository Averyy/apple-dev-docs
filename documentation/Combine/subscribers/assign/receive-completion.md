# receive(completion:)

**Framework**: Combine  
**Kind**: method

Tells the subscriber that the publisher has completed publishing, either normally or with an error.

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
final func receive(completion: Subscribers.Completion<Never>)
```

## Parameters

- `completion`: A   case indicating whether publishing completed normally or with an error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/subscribers/assign/receive(completion:))*