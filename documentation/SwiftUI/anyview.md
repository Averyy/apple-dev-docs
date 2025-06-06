# AnyView

**Framework**: SwiftUI  
**Kind**: struct

A type-erased view.

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
struct AnyView
```

#### Overview

An `AnyView` allows changing the type of view used in a given view hierarchy. Whenever the type of view used with an `AnyView` changes, the old hierarchy is destroyed and a new hierarchy is created for the new type.

## Topics

### Creating a view
- [init<V>(V)](anyview/init(_:).md)
  Create an instance that type-erases `view`.
- [init<V>(erasing: V)](anyview/init(erasing:).md)

## Relationships

### Conforms To
- [View](view.md)

## See Also

- [struct EmptyView](emptyview.md)
  A view that doesn’t contain any content.
- [struct EquatableView](equatableview.md)
  A view type that compares itself against its previous value and prevents its child updating if its new value is the same as its old value.
- [struct SubscriptionView](subscriptionview.md)
  A view that subscribes to a publisher with an action.
- [struct TupleView](tupleview.md)
  A View created from a swift tuple of View values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/anyview)*