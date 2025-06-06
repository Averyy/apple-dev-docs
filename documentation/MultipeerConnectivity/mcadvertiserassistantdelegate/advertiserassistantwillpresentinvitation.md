# advertiserAssistantWillPresentInvitation(_:)

**Framework**: Multipeer Connectivity  
**Kind**: method

Indicates that the advertiser assistant is about to present an invitation to the user.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
optional func advertiserAssistantWillPresentInvitation(_ advertiserAssistant: MCAdvertiserAssistant)
```

#### Discussion

This call is intended to allow your app to prepare for an invitation that will be presented to the user. For example, your app might stop performing computationally intensive UI updates for views that will be hidden by the invitation.

## Parameters

- `advertiserAssistant`: The advertiser assistant that is about to present an invitation to the user.

## See Also

- [func advertiserAssistantDidDismissInvitation(MCAdvertiserAssistant)](mcadvertiserassistantdelegate/advertiserassistantdiddismissinvitation(_:).md)
  Indicates that the advertiser assistant finished showing the invitation to the user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/multipeerconnectivity/mcadvertiserassistantdelegate/advertiserassistantwillpresentinvitation(_:))*