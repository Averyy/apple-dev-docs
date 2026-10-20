# NEVPNStatus.disconnecting

**Framework**: Network Extension  
**Kind**: case  
**Role**: Case

The VPN is in the process of disconnecting.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
case disconnecting
```

```c
NEVPNStatusDisconnecting
```

## See Also

### Statuses
- [NEVPNStatus.reasserting](./reasserting.md)
  The VPN is in the process of reconnecting.
- [NEVPNStatus.connected](./connected.md)
  The VPN is connected.
- [NEVPNStatus.connecting](./connecting.md)
  The VPN is in the process of connecting.
- [NEVPNStatus.disconnected](./disconnected.md)
  The VPN is disconnected.
- [NEVPNStatus.invalid](./invalid.md)
  The associated VPN configuration doesn’t exist in the Network Extension preferences or isn’t enabled.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nevpnstatus/disconnecting)*