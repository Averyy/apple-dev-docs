# SubscriptionView

**Framework**: SwiftUI  
**Kind**: struct

A view that subscribes to a publisher with an action.

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
@frozen
struct SubscriptionView<PublisherType, Content> where PublisherType : Publisher, Content : View, PublisherType.Failure == Never
```

## Topics

### Creating a subscription view
- [init(content: Content, publisher: PublisherType, action: (PublisherType.Output) -> Void)](subscriptionview/init(content:publisher:action:).md)
### Managing the subscription
- [var publisher: PublisherType](subscriptionview/publisher.md)
  The `Publisher` that is being subscribed.
- [var action: (PublisherType.Output) -> Void](subscriptionview/action.md)
  The `Action` executed when `publisher` emits an event.
- [var content: Content](subscriptionview/content.md)
  The content view.

## Relationships

### Conforms To
- [View](view.md)

## See Also

- [struct AnyView](anyview.md)
  A type-erased view.
- [struct EmptyView](emptyview.md)
  A view that doesn’t contain any content.
- [struct EquatableView](equatableview.md)
  A view type that compares itself against its previous value and prevents its child updating if its new value is the same as its old value.
- [struct TupleView](tupleview.md)
  A View created from a swift tuple of View values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/subscriptionview)*