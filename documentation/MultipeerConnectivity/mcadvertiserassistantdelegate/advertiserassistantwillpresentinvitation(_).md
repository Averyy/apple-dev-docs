# advertiserAssistantWillPresentInvitation(_:)

**Framework**: Multipeer Connectivity  
**Kind**: method  
**Role**: Instance Method

Indicates that the advertiser assistant is about to present an invitation to the user.

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
optional func advertiserAssistantWillPresentInvitation(_ advertiserAssistant: MCAdvertiserAssistant)
```

```objc
- (void) advertiserAssistantWillPresentInvitation:(MCAdvertiserAssistant *) advertiserAssistant;
```

## Discussion

This call is intended to allow your app to prepare for an invitation that will be presented to the user. For example, your app might stop performing computationally intensive UI updates for views that will be hidden by the invitation.

## Parameters

- `advertiserAssistant`: The advertiser assistant that is about to present an invitation to the user.

## See Also

### Advertiser Assistant Delegate Methods
- [func advertiserAssistantDidDismissInvitation(MCAdvertiserAssistant)](./advertiserassistantdiddismissinvitation%28_%29.md)
  Indicates that the advertiser assistant finished showing the invitation to the user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/multipeerconnectivity/mcadvertiserassistantdelegate/advertiserassistantwillpresentinvitation(_:))*