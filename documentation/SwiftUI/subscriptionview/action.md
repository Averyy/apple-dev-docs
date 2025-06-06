# action

**Framework**: SwiftUI  
**Kind**: property

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

- [var publisher: PublisherType](subscriptionview/publisher.md)
  The `Publisher` that is being subscribed.
- [var content: Content](subscriptionview/content.md)
  The content view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/subscriptionview/action)*