# NEVPNConnectionErrorDomain

**Framework**: Network Extension  
**Kind**: var  
**Role**: Global Variable

The domain for errors resulting from VPN connection calls.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
let NEVPNConnectionErrorDomain: String
```

```c
extern NSString * const NEVPNConnectionErrorDomain;
```

#### Discussion

Match this constant to the [`domain`](../Foundation/nserror/domain.md) of an [`NSError`](../Foundation/nserror.md) encountered when calling methods on [`NEVPNConnection`](./nevpnconnection.md). The [`NEDNSSettingsManagerError`](./nednssettingsmanagererror.md) enumeration defines possible [`code`](../Foundation/nserror/code.md) values for these errors.

## See Also

### Handling errors
- [func fetchLastDisconnectError(completionHandler: ((any Error)?) -> Void)](./nevpnconnection/fetchlastdisconnecterror%28completionhandler%29.md)
  Retrives the most recent error that caused the VPN to disconnect.
- [enum NEVPNConnectionError](./nevpnconnectionerror.md)
  Error codes specific to VPN connections.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nevpnconnectionerrordomain)*