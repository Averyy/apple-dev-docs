# ManagedAppView

**Framework**: ManagedAppDistribution  
**Kind**: struct

A view that displays a managed app.

**Availability**:
- iOS 17.2+
- iPadOS 17.2+

## Declaration

```swift
@MainActor
@preconcurrency struct ManagedAppView
```

## Topics

### Creating a view
- [init(app: ManagedApp)](managedappview/init(app:).md)
  Create a managed app view from a managed app.
### Getting the properties
- [var body: some View](managedappview/body-swift.property.md)
  The content and behavior of the view.
### Type Aliases
- [ManagedAppView.Body](managedappview/body-swift.typealias.md)
  The type of view representing the body of this view.
### Default Implementations
- [View Implementations](managedappview/view-implementations.md)

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [View](../SwiftUI/View.md)

## See Also

- [struct ManagedContentView](managedcontentview.md)
- [struct ManagedContentOfferState](managedcontentofferstate.md)
- [struct ManagedContentStyle](managedcontentstyle.md)
  A type that applies a custom appearance to the managed content view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/managedappdistribution/managedappview)*