# manual

**Framework**: StoreKit  
**Kind**: property  
**Role**: Type Property

A behavior in which the system doesn’t present the invitation sheet after a purchase.

**Availability**:
- iOS 27.3+ (Beta)
- iPadOS 27.3+ (Beta)
- Mac Catalyst 27.3+ (Beta)
- macOS 27.3+ (Beta)

## Declaration

```swift
static let manual: MultiSeatInvitationBehavior
```

## Discussion

To present the invitation sheet at a time you choose, use the [`multiSeatInvitationSheet(isPresented:subscriptionGroupID:onCompletion:)`](../../SwiftUI/view/multiseatinvitationsheet%28ispresented,subscriptiongroupid,oncompletion%29.md) view modifier.

## See Also

### Getting the behaviors
- [static let automatic: MultiSeatInvitationBehavior](./automatic.md)
  A behavior in which the system presents the invitation sheet inline, right after the customer buys a multiseat subscription.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/multiseatinvitationbehavior/manual)*