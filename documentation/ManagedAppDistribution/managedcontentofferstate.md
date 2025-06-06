# ManagedContentOfferState

**Framework**: ManagedAppDistribution  
**Kind**: struct

**Availability**:
- iOS 17.2+
- iPadOS 17.2+

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
### Operators
- [static func == (ManagedContentOfferState, ManagedContentOfferState) -> Bool](managedcontentofferstate/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Instance Properties
- [var hashValue: Int](managedcontentofferstate/hashvalue.md)
  The hash value.
### Instance Methods
- [func hash(into: inout Hasher)](managedcontentofferstate/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Default Implementations
- [Equatable Implementations](managedcontentofferstate/equatable-implementations.md)

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