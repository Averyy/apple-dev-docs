# advertiserAssistantDidDismissInvitation(_:)

**Framework**: Multipeer Connectivity  
**Kind**: method  
**Role**: Instance Method

Indicates that the advertiser assistant finished showing the invitation to the user.

**Availability**:
- iOS 7.0+ - Deprecated in 27.0
- iPadOS 7.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- macOS 10.10+ - Deprecated in 27.0
- tvOS 10.0+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0

> **Deprecated**: Use Network Framework instead

## Declaration

```swift
optional func advertiserAssistantDidDismissInvitation(_ advertiserAssistant: MCAdvertiserAssistant)
```

```objc
- (void) advertiserAssistantDidDismissInvitation:(MCAdvertiserAssistant *) advertiserAssistant;
```

## Discussion

This call tells your app to resume any activity that it stopped doing while the invitation was onscreen. For example, it might resume computationally intensive UI updates for views that are no longer hidden by the invitation.

## Parameters

- `advertiserAssistant`: The advertiser assistant that finished showing an invitation.

## See Also

### Advertiser Assistant Delegate Methods
- [func advertiserAssistantWillPresentInvitation(MCAdvertiserAssistant)](./advertiserassistantwillpresentinvitation%28_%29.md)
  Indicates that the advertiser assistant is about to present an invitation to the user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/multipeerconnectivity/mcadvertiserassistantdelegate/advertiserassistantdiddismissinvitation(_:))*