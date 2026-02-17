# installing(progress:)

**Framework**: ManagedAppDistribution  
**Kind**: method

A state indicating install progress.

**Availability**:
- iOS 17.2+
- iPadOS 17.2+
- Mac Catalyst 26.4+ (Beta)
- macOS 26.4+ (Beta)
- visionOS 26.4+ (Beta)

## Declaration

```swift
static func installing(progress: Double?) -> ManagedContentOfferState
```

## Parameters

- `progress`: The progress of the install from   to  .   represents indeterminate progress.

## See Also

- [static func custom(title: String) -> ManagedContentOfferState](managedcontentofferstate/custom(title:).md)
  A state with a custom title.


---

*[View on Apple Developer](https://developer.apple.com/documentation/managedappdistribution/managedcontentofferstate/installing(progress:))*