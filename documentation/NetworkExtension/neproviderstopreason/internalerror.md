# NEProviderStopReason.internalError

**Framework**: Network Extension  
**Kind**: case  
**Role**: Case

The provider encountered an internal error.

**Availability**:
- iOS 18.1+
- iPadOS 18.1+
- Mac Catalyst 18.1+
- macOS 15.1+
- tvOS 18.1+
- visionOS 2.1+

## Declaration

```swift
case internalError
```

```c
NEProviderStopReasonInternalError
```

## See Also

### Stop Reasons
- [NEProviderStopReason.none](./none.md)
  No specific reason.
- [NEProviderStopReason.userInitiated](./userinitiated.md)
  The user stopped the provider extension.
- [NEProviderStopReason.providerFailed](./providerfailed.md)
  The provider failed to function correctly.
- [NEProviderStopReason.noNetworkAvailable](./nonetworkavailable.md)
  No network connectivity is currently available.
- [NEProviderStopReason.unrecoverableNetworkChange](./unrecoverablenetworkchange.md)
  The device’s network connectivity changed.
- [NEProviderStopReason.providerDisabled](./providerdisabled.md)
  The provider was disabled.
- [NEProviderStopReason.authenticationCanceled](./authenticationcanceled.md)
  The authentication process was canceled.
- [NEProviderStopReason.configurationFailed](./configurationfailed.md)
  The configuration is invalid.
- [NEProviderStopReason.idleTimeout](./idletimeout.md)
  The session timed out.
- [NEProviderStopReason.configurationDisabled](./configurationdisabled.md)
  The configuration was disabled.
- [NEProviderStopReason.configurationRemoved](./configurationremoved.md)
  The configuration was removed.
- [NEProviderStopReason.superceded](./superceded.md)
  The configuration was superceded by a higher-priority configuration.
- [NEProviderStopReason.userLogout](./userlogout.md)
  The user logged out.
- [NEProviderStopReason.userSwitch](./userswitch.md)
  The current console user changed.
- [NEProviderStopReason.appUpdate](./appupdate.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/neproviderstopreason/internalerror)*