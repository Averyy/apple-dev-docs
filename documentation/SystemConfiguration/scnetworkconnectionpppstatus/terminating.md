# SCNetworkConnectionPPPStatus.terminating

**Framework**: System Configuration  
**Kind**: case

PPP networking and link protocols are terminating.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
case terminating
```

## See Also

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
- [SCNetworkConnectionPPPStatus.disconnectingLink](scnetworkconnectionpppstatus/disconnectinglink.md)
  PPP is disconnecting the lower level (for example, the modem is hanging up).
- [SCNetworkConnectionPPPStatus.holdingLinkOff](scnetworkconnectionpppstatus/holdinglinkoff.md)
  PPP is disconnected and maintaining the link temporarily off.
- [SCNetworkConnectionPPPStatus.suspended](scnetworkconnectionpppstatus/suspended.md)
  PPP is suspended as a result of the suspend command (for example, when a V.92 Modem is On Hold).
- [SCNetworkConnectionPPPStatus.waitingForRedial](scnetworkconnectionpppstatus/waitingforredial.md)
  PPP has found a busy server and is waiting for redial.


---

*[View on Apple Developer](https://developer.apple.com/documentation/systemconfiguration/scnetworkconnectionpppstatus/terminating)*