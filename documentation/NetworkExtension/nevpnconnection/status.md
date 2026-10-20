# status

**Framework**: Network Extension  
**Kind**: property  
**Role**: Instance Property

The current status of the VPN connection.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
var status: NEVPNStatus { get }
```

```objc
@property (readonly) NEVPNStatus status;
```

## See Also

### Getting VPN connection status
- [var manager: NEVPNManager](./manager.md)
- [enum NEVPNStatus](../nevpnstatus.md)
  The possible states of a VPN connection.
- [var connectedDate: Date?](./connecteddate.md)
  The date and time when the connection status changed to `NEVPNStatusConnected`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nevpnconnection/status)*