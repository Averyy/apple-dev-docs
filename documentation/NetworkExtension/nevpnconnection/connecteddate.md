# connectedDate

**Framework**: Network Extension  
**Kind**: property

The date and time when the connection status changed to `NEVPNStatusConnected`.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
var connectedDate: Date? { get }
```

#### Discussion

This property contains the date and time when the connection status changed to `NEVPNStatusConnected` after previously being set to `NEVPNStatusDisconnected`. This property is set to nil whenever the status changes to `NEVPNStatusDisconnected`.

## See Also

- [var manager: NEVPNManager](nevpnconnection/manager.md)
- [var status: NEVPNStatus](nevpnconnection/status.md)
  The current status of the VPN connection.
- [enum NEVPNStatus](nevpnstatus.md)
  The possible states of a VPN connection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nevpnconnection/connecteddate)*