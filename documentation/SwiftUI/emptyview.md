# EmptyView

**Framework**: SwiftUI  
**Kind**: struct

A view that doesn’t contain any content.

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
struct EmptyView
```

#### Overview

You will rarely, if ever, need to create an `EmptyView` directly. Instead, `EmptyView` represents the absence of a view.

SwiftUI uses `EmptyView` in situations where a SwiftUI view type defines one or more child views with generic parameters, and allows the child views to be absent. When absent, the child view’s type in the generic type parameter is `EmptyView`.

The following example creates an indeterminate [`ProgressView`](progressview.md) without a label. The [`ProgressView`](progressview.md) type declares two generic parameters, `Label` and `CurrentValueLabel`, for the types used by its subviews. When both subviews are absent, like they are here, the resulting type is `ProgressView<EmptyView, EmptyView>`, as indicated by the example’s output:

```swift
let progressView = ProgressView()
print("\(type(of:progressView))")
// Prints: ProgressView<EmptyView, EmptyView>
```

## Topics

### Creating an empty view
- [init()](emptyview/init.md)
  Creates an empty view.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Copyable](../Swift/Copyable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [View](view.md)

## See Also

- [struct AnyView](anyview.md)
  A type-erased view.
- [struct EquatableView](equatableview.md)
  A view type that compares itself against its previous value and prevents its child updating if its new value is the same as its old value.
- [struct SubscriptionView](subscriptionview.md)
  A view that subscribes to a publisher with an action.
- [struct TupleView](tupleview.md)
  A View created from a swift tuple of View values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/emptyview)*