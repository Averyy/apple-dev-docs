# TupleView

**Framework**: SwiftUI  
**Kind**: struct

A View created from a swift tuple of View values.

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
struct TupleView<T>
```

## Topics

### Creating a tuple view
- [init(_:)](tupleview/init(_:).md)
- [var value: T](tupleview/value.md)

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
- [struct SubscriptionView](subscriptionview.md)
  A view that subscribes to a publisher with an action.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/tupleview)*