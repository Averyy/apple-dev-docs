# SCNetworkConnectionPPPStatus

**Framework**: System Configuration  
**Kind**: enum

The PPP-specific status of the network connection.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
enum SCNetworkConnectionPPPStatus
```

#### Overview

This status is returned as part of the extended information for a PPP service. Note that additional status might be returned in the future. Therefore, your application should be prepared to receive an unknown value.

## Topics

### Constants
- [SCNetworkConnectionPPPStatus.disconnected](scnetworkconnectionpppstatus/disconnected.md)
  PPP is disconnected.
- [SCNetworkConnectionPPPStatus.initializing](scnetworkconnectionpppstatus/initializing.md)
  PPP is initializing.
- [SCNetworkConnectionPPPStatus.connectingLink](scnetworkconnectionpppstatus/connectinglink.md)
  PPP is connecting the lower connection layer (for example, the modem is dialing out).
- [SCNetworkConnectionPPPStatus.dialOnTraffic](scnetworkconnectionpppstatus/dialontraffic.md)
  PPP is waiting for networking traffic to automatically establish the connection.
- [SCNetworkConnectionPPPStatus.negotiatingLink](scnetworkconnectionpppstatus/negotiatinglink.md)
  The PPP lower layer is connected and PPP is negotiating the link layer (LCP protocol).
- [SCNetworkConnectionPPPStatus.authenticating](scnetworkconnectionpppstatus/authenticating.md)
  PPP is authenticating to the server (PAP, CHAP, MS-CHAP, or EAP protocols).
- [SCNetworkConnectionPPPStatus.waitingForCallBack](scnetworkconnectionpppstatus/waitingforcallback.md)
  PPP is waiting for the server to call back.
- [SCNetworkConnectionPPPStatus.negotiatingNetwork](scnetworkconnectionpppstatus/negotiatingnetwork.md)
  PPP is now authenticated and negotiating the networking layer (IPCP or IPv6CP protocols).
- [SCNetworkConnectionPPPStatus.connected](scnetworkconnectionpppstatus/connected.md)
  PPP is now fully connected for at least one networking layer. Additional networking protocol might still be negotiating.
- [SCNetworkConnectionPPPStatus.terminating](scnetworkconnectionpppstatus/terminating.md)
  PPP networking and link protocols are terminating.
- [SCNetworkConnectionPPPStatus.disconnectingLink](scnetworkconnectionpppstatus/disconnectinglink.md)
  PPP is disconnecting the lower level (for example, the modem is hanging up).
- [SCNetworkConnectionPPPStatus.holdingLinkOff](scnetworkconnectionpppstatus/holdinglinkoff.md)
  PPP is disconnected and maintaining the link temporarily off.
- [SCNetworkConnectionPPPStatus.suspended](scnetworkconnectionpppstatus/suspended.md)
  PPP is suspended as a result of the suspend command (for example, when a V.92 Modem is On Hold).
- [SCNetworkConnectionPPPStatus.waitingForRedial](scnetworkconnectionpppstatus/waitingforredial.md)
  PPP has found a busy server and is waiting for redial.
### Initializers
- [init?(rawValue: Int32)](scnetworkconnectionpppstatus/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [enum SCNetworkConnectionStatus](scnetworkconnectionstatus.md)
  The current status of the network connection.
- [Statistics Dictionary Keys](statistics-dictionary-keys.md)
  Keys associated with values in the statistics dictionary.
- [Selection Options Dictionary Keys](selection-options-dictionary-keys.md)
  Keys used with the [`SCNetworkConnectionCopyUserPreferences(_:_:_:)`](scnetworkconnectioncopyuserpreferences(_:_:_:).md) selection options dictionary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/systemconfiguration/scnetworkconnectionpppstatus)*