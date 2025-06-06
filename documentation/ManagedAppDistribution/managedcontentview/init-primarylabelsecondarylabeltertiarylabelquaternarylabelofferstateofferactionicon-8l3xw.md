# init(primaryLabel:secondaryLabel:tertiaryLabel:quaternaryLabel:offerState:offerAction:icon:)

**Framework**: ManagedAppDistribution  
**Kind**: init

Create a content view with the layout of a managed app view and customized labels using strings.

**Availability**:
- iOS 17.2+
- iPadOS 17.2+

## Declaration

```swift
nonisolated
init(primaryLabel: any StringProtocol, secondaryLabel: any StringProtocol = "", tertiaryLabel: any StringProtocol = "", quaternaryLabel: any StringProtocol = "", offerState: ManagedContentOfferState, offerAction: @escaping (ManagedContentOfferState) -> Void, @ViewBuilder icon: () -> Icon)
```

## Parameters

- `primaryLabel`: The string for primary label.
- `secondaryLabel`: The string for secondary label.
- `tertiaryLabel`: The string for tertiary label.
- `quaternaryLabel`: The string for quaternary label.
- `offerState`: The view’s offer state.
- `offerAction`: The action to execute when a person taps the offer button.
- `icon`: A view that represents the icon for this managed content.

## See Also

- [init(primaryLabel: LocalizedStringKey, secondaryLabel: LocalizedStringKey, tertiaryLabel: LocalizedStringKey, quaternaryLabel: LocalizedStringKey, offerState: ManagedContentOfferState, offerAction: (ManagedContentOfferState) -> Void, icon: () -> Icon)](managedcontentview/init(primarylabel:secondarylabel:tertiarylabel:quaternarylabel:offerstate:offeraction:icon:)-4blv1.md)
  Create a view with the layout of a managed app view and customized labels using localized string keys.


---

*[View on Apple Developer](https://developer.apple.com/documentation/managedappdistribution/managedcontentview/init(primarylabel:secondarylabel:tertiarylabel:quaternarylabel:offerstate:offeraction:icon:)-8l3xw)*