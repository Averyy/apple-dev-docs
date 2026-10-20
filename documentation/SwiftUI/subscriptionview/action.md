# action

**Framework**: SwiftUI  
**Kind**: property  
**Role**: Instance Property

The `Action` executed when `publisher` emits an event.

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
var action: (PublisherType.Output) -> Void
```

## See Also

### Managing the subscription
- [var publisher: PublisherType](./publisher.md)
  The `Publisher` that is being subscribed.
- [var content: Content](./content.md)
  The content view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/subscriptionview/action)*