# NEProviderStopReason.sleep

**Framework**: Network Extension  
**Kind**: case  
**Role**: Case

A stop reason indicating the configuration enabled disconnect on sleep and the device went to sleep.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
case sleep
```

```c
NEProviderStopReasonSleep
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

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/neproviderstopreason/sleep)*