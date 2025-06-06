# MCAdvertiserAssistantDelegate

**Framework**: Multipeer Connectivity  
**Kind**: protocol

The `MCAdvertiserAssistantDelegate` protocol describes the methods that the delegate object for an `MCAdvertiserAssistant` instance can implement to handle advertising-related events.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.0+
- macOS 10.10+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
protocol MCAdvertiserAssistantDelegate : NSObjectProtocol
```

#### Overview

No assumption should be made about which queue the delegate methods are called on. It is the delegate’s responsibility to ensure that any UIKit-related updates are called on the main thread.

## Topics

### Advertiser Assistant Delegate Methods
- [func advertiserAssistantWillPresentInvitation(MCAdvertiserAssistant)](mcadvertiserassistantdelegate/advertiserassistantwillpresentinvitation(_:).md)
  Indicates that the advertiser assistant is about to present an invitation to the user.
- [func advertiserAssistantDidDismissInvitation(MCAdvertiserAssistant)](mcadvertiserassistantdelegate/advertiserassistantdiddismissinvitation(_:).md)
  Indicates that the advertiser assistant finished showing the invitation to the user.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [protocol MCBrowserViewControllerDelegate](mcbrowserviewcontrollerdelegate.md)
  The `MCBrowserViewControllerDelegate` protocol defines the methods that your delegate object can implement to handle events related to the `MCBrowserViewController` class.
- [protocol MCNearbyServiceAdvertiserDelegate](mcnearbyserviceadvertiserdelegate.md)
  The `MCNearbyServiceAdvertiserDelegate` protocol describes the methods that the delegate object for an `MCNearbyServiceAdvertiser` instance can implement for handling events from the `MCNearbyServiceAdvertiser` class.
- [protocol MCNearbyServiceBrowserDelegate](mcnearbyservicebrowserdelegate.md)
  The `MCNearbyServiceBrowserDelegate` protocol defines methods that a `MCNearbyServiceBrowser` object’s delegate can implement to handle browser-related events.
- [protocol MCSessionDelegate](mcsessiondelegate.md)
  The `MCSessionDelegate` protocol defines methods that a delegate of the `MCSession` class can implement to handle session-related events. For more information, see [`MCSession`](mcsession.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/multipeerconnectivity/mcadvertiserassistantdelegate)*