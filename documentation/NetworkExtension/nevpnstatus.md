# NEVPNStatus

**Framework**: Network Extension  
**Kind**: enum  
**Role**: Enumeration

The possible states of a VPN connection.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
enum NEVPNStatus
```

```c
enum NEVPNStatus : NSInteger;
```

## Overview

After the VPN transitions from the [`NEVPNStatus.disconnected`](./nevpnstatus/disconnected.md) to the [`NEVPNStatus.disconnecting`](./nevpnstatus/disconnecting.md) state, the system doesn’t close TCP connections, but ignores packets to and from established network connections. When the VPN transitions to another state — for example, from a Wi-Fi to a cellular network — the system ignores network traffic and the VPN client typically reconnects to the VPN server.

## Topics

### Statuses
- [NEVPNStatus.disconnecting](./nevpnstatus/disconnecting.md)
  The VPN is in the process of disconnecting.
- [NEVPNStatus.reasserting](./nevpnstatus/reasserting.md)
  The VPN is in the process of reconnecting.
- [NEVPNStatus.connected](./nevpnstatus/connected.md)
  The VPN is connected.
- [NEVPNStatus.connecting](./nevpnstatus/connecting.md)
  The VPN is in the process of connecting.
- [NEVPNStatus.disconnected](./nevpnstatus/disconnected.md)
  The VPN is disconnected.
- [NEVPNStatus.invalid](./nevpnstatus/invalid.md)
  The associated VPN configuration doesn’t exist in the Network Extension preferences or isn’t enabled.
### Initializers
- [init?(rawValue: Int)](./nevpnstatus/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Getting VPN connection status
- [var manager: NEVPNManager](./nevpnconnection/manager.md)
- [var status: NEVPNStatus](./nevpnconnection/status.md)
  The current status of the VPN connection.
- [var connectedDate: Date?](./nevpnconnection/connecteddate.md)
  The date and time when the connection status changed to `NEVPNStatusConnected`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nevpnstatus)*