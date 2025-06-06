# EquatableView

**Framework**: SwiftUI  
**Kind**: struct

A view type that compares itself against its previous value and prevents its child updating if its new value is the same as its old value.

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
struct EquatableView<Content> where Content : Equatable, Content : View
```

## Topics

### Creating an equatable view
- [init(content: Content)](equatableview/init(content:).md)
- [var content: Content](equatableview/content.md)

## Relationships

### Conforms To
- [View](view.md)

## See Also

- [struct AnyView](anyview.md)
  A type-erased view.
- [struct EmptyView](emptyview.md)
  A view that doesn’t contain any content.
- [struct SubscriptionView](subscriptionview.md)
  A view that subscribes to a publisher with an action.
- [struct TupleView](tupleview.md)
  A View created from a swift tuple of View values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/equatableview)*