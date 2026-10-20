# manager

**Framework**: Network Extension  
**Kind**: property  
**Role**: Instance Property

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
var manager: NEVPNManager { get }
```

```objc
@property (readonly) NEVPNManager * manager;
```

## See Also

### Getting VPN connection status
- [var status: NEVPNStatus](./status.md)
  The current status of the VPN connection.
- [enum NEVPNStatus](../nevpnstatus.md)
  The possible states of a VPN connection.
- [var connectedDate: Date?](./connecteddate.md)
  The date and time when the connection status changed to `NEVPNStatusConnected`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nevpnconnection/manager)*