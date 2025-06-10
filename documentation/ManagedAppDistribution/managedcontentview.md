# ManagedContentView

**Framework**: ManagedAppDistribution  
**Kind**: struct

**Availability**:
- iOS 17.2+
- iPadOS 17.2+
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
@MainActor
struct ManagedContentView<Icon> where Icon : View
```

## Topics

### Creating views
- [init(primaryLabel: LocalizedStringKey, secondaryLabel: LocalizedStringKey, tertiaryLabel: LocalizedStringKey, quaternaryLabel: LocalizedStringKey, offerState: ManagedContentOfferState, offerAction: (ManagedContentOfferState) -> Void, icon: () -> Icon)](managedcontentview/init(primarylabel:secondarylabel:tertiarylabel:quaternarylabel:offerstate:offeraction:icon:)-4blv1.md)
  Create a view with the layout of a managed app view and customized labels using localized string keys.
- [init(primaryLabel: any StringProtocol, secondaryLabel: any StringProtocol, tertiaryLabel: any StringProtocol, quaternaryLabel: any StringProtocol, offerState: ManagedContentOfferState, offerAction: (ManagedContentOfferState) -> Void, icon: () -> Icon)](managedcontentview/init(primarylabel:secondarylabel:tertiarylabel:quaternarylabel:offerstate:offeraction:icon:)-8l3xw.md)
  Create a content view with the layout of a managed app view and customized labels using strings.
### Inspecting the view
- [var body: some View](managedcontentview/body-swift.property.md)
  The content and behavior of the view.
### Type Aliases
- [ManagedContentView.Body](managedcontentview/body-swift.typealias.md)
  The type of view representing the body of this view.
### Default Implementations
- [View Implementations](managedcontentview/view-implementations.md)

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [View](../SwiftUI/View.md)

## See Also

- [struct ManagedAppView](managedappview.md)
  A view that displays a managed app.
- [struct ManagedContentOfferState](managedcontentofferstate.md)
- [struct ManagedContentStyle](managedcontentstyle.md)
  A type that applies a custom appearance to the managed content view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/managedappdistribution/managedcontentview)*