# installing(progress:)

**Framework**: ManagedAppDistribution  
**Kind**: method

A state indicating install progress.

**Availability**:
- iOS 17.2+
- iPadOS 17.2+
- macOS 26.4+
- visionOS 26.4+

## Declaration

```swift
static func installing(progress: Double?) -> ManagedContentOfferState
```

## Parameters

- `progress`: The progress of the install from `0.0` to `1.0`. `nil` represents indeterminate progress.

## See Also

- [static func custom(title: String) -> ManagedContentOfferState](managedcontentofferstate/custom(title:).md)
  A state with a custom title.


---

*[View on Apple Developer](https://developer.apple.com/documentation/managedappdistribution/managedcontentofferstate/installing(progress:))*