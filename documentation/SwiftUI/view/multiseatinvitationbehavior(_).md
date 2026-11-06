# multiSeatInvitationBehavior(_:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Sets the behavior of the Apple-owned invitation sheet that appears after a customer purchases a multi-seat subscription from a StoreKit view.

**Availability**:
- iOS 27.3+ (Beta)
- iPadOS 27.3+ (Beta)
- Mac Catalyst 27.3+ (Beta)
- macOS 27.3+ (Beta)

## Declaration

```swift
nonisolated
func multiSeatInvitationBehavior(_ behavior: MultiSeatInvitationBehavior) -> some View
```

## Discussion

The behavior you set applies to StoreKit views within this view, and only to the sheet the system presents in-line once a purchase completes. It has no effect on [`multiSeatInvitationSheet(isPresented:subscriptionGroupID:onCompletion:)`](./multiseatinvitationsheet%28ispresented,subscriptiongroupid,oncompletion%29.md), which your app presents on demand.

Behaviors you set in this modifier overwrite any behavior you specified in ancestor views.

## Parameters

- `behavior`: The behavior to apply to the Apple-owned multi-seat invitation sheet.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/multiseatinvitationbehavior(_:))*