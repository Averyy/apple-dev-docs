# advertiserAssistantDidDismissInvitation(_:)

**Framework**: Multipeer Connectivity  
**Kind**: method

Indicates that the advertiser assistant finished showing the invitation to the user.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
optional func advertiserAssistantDidDismissInvitation(_ advertiserAssistant: MCAdvertiserAssistant)
```

#### Discussion

This call tells your app to resume any activity that it stopped doing while the invitation was onscreen. For example, it might resume computationally intensive UI updates for views that are no longer hidden by the invitation.

## Parameters

- `advertiserAssistant`: The advertiser assistant that finished showing an invitation.

## See Also

- [func advertiserAssistantWillPresentInvitation(MCAdvertiserAssistant)](mcadvertiserassistantdelegate/advertiserassistantwillpresentinvitation(_:).md)
  Indicates that the advertiser assistant is about to present an invitation to the user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/multipeerconnectivity/mcadvertiserassistantdelegate/advertiserassistantdiddismissinvitation(_:))*