# connectedDate

**Framework**: Network Extension  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (readonly, nullable) NSDate * connectedDate;
```

#### Discussion

This property contains the date and time when the connection status changed to `NEVPNStatusConnected` after previously being set to `NEVPNStatusDisconnected`. This property is set to nil whenever the status changes to `NEVPNStatusDisconnected`.

## See Also

### Getting VPN connection status
- [var manager: NEVPNManager](./manager.md)
- [var status: NEVPNStatus](./status.md)
  The current status of the VPN connection.
- [enum NEVPNStatus](../nevpnstatus.md)
  The possible states of a VPN connection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nevpnconnection/connecteddate)*