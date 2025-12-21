# ManagedContentOfferState

**Framework**: ManagedAppDistribution  
**Kind**: struct

**Availability**:
- iOS 17.2+
- iPadOS 17.2+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.4+

## Declaration

```swift
struct ManagedContentOfferState
```

## Topics

### Creating states
- [static func custom(title: String) -> ManagedContentOfferState](managedcontentofferstate/custom(title:).md)
  A state with a custom title.
- [static func installing(progress: Double?) -> ManagedContentOfferState](managedcontentofferstate/installing(progress:).md)
  A state indicating install progress.
### Determining installation status
- [static var installed: ManagedContentOfferState](managedcontentofferstate/installed.md)
  A state representing content that’s installed.
- [static var notInstalled: ManagedContentOfferState](managedcontentofferstate/notinstalled.md)
  A state for representing content that isn’t currently installed.
- [static var neverInstalled: ManagedContentOfferState](managedcontentofferstate/neverinstalled.md)
  A state representing content that has never been installed.
- [static var noninteractive: ManagedContentOfferState](managedcontentofferstate/noninteractive.md)
  A state representing content that has no actionable button.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)

## See Also

- [struct ManagedAppView](managedappview.md)
  A view that displays a managed app.
- [struct ManagedContentView](managedcontentview.md)
- [struct ManagedContentStyle](managedcontentstyle.md)
  A type that applies a custom appearance to the managed content view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/managedappdistribution/managedcontentofferstate)*