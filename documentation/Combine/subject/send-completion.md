# send(completion:)

**Framework**: Combine  
**Kind**: method  
**Required**: Yes

Sends a completion signal to the subscriber.

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
func send(completion: Subscribers.Completion<Self.Failure>)
```

## Mentions

- [Using Combine for Your App’s Asynchronous Code](using-combine-for-your-app-s-asynchronous-code.md)

## Parameters

- `completion`: A   instance which indicates whether publishing has finished normally or failed with an error.

## See Also

- [func send(subscription: any Subscription)](subject/send(subscription:).md)
  Sends a subscription to the subscriber.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/subject/send(completion:))*