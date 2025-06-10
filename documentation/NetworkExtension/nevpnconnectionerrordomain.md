# NEVPNConnectionErrorDomain

**Framework**: Network Extension  
**Kind**: var

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

#### Discussion

Match this constant to the [`domain`](https://developer.apple.com/documentation/Foundation/NSError/domain) of an [`NSError`](https://developer.apple.com/documentation/Foundation/NSError) encountered when calling methods on [`NEVPNConnection`](nevpnconnection.md). The [`NEDNSSettingsManagerError`](nednssettingsmanagererror.md) enumeration defines possible [`code`](https://developer.apple.com/documentation/Foundation/NSError/code) values for these errors.

## See Also

- [func fetchLastDisconnectError(completionHandler: ((any Error)?) -> Void)](nevpnconnection/fetchlastdisconnecterror(completionhandler:).md)
  Retrives the most recent error that caused the VPN to disconnect.
- [enum NEVPNConnectionError](nevpnconnectionerror.md)
  Error codes specific to VPN connections.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nevpnconnectionerrordomain)*