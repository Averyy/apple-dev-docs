# stopVPNTunnel()

**Framework**: Network Extension  
**Kind**: method  
**Role**: Instance Method

Start the process of disconnecting the VPN.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
func stopVPNTunnel()
```

```objc
- (void) stopVPNTunnel;
```

## Discussion

This method returns immediately after starting the process of disconnecting the VPN. In order to be notified when the VPN is fully disconnected, register to observe the [`NEVPNStatusDidChangeNotification`](../nevpnstatusdidchangenotification.md) notification on the [`NEVPNConnection`](../nevpnconnection.md) object and examine the status property when the notification is received.

## See Also

### Controlling the VPN connection
- [func startVPNTunnel() throws](./startvpntunnel%28%29.md)
  Start the process of connecting the VPN.
- [func startVPNTunnel(options: [String : NSObject]?) throws](./startvpntunnel%28options%29.md)
  Start the process of connecting the VPN.
- [let NEVPNConnectionStartOptionUsername: String](../nevpnconnectionstartoptionusername.md)
- [let NEVPNConnectionStartOptionPassword: String](../nevpnconnectionstartoptionpassword.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nevpnconnection/stopvpntunnel())*