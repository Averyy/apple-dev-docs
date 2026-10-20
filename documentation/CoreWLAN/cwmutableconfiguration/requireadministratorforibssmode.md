# requireAdministratorForIBSSMode

**Framework**: Core WLAN  
**Kind**: property  
**Role**: Instance Property

A Boolean value that determines whether to require an administrator password to create a computer-to-computer network.

**Availability**:
- macOS 10.7+ - Deprecated in 11.0

## Declaration

```swift
var requireAdministratorForIBSSMode: Bool { get set }
```

```objc
@property BOOL requireAdministratorForIBSSMode;
```

## See Also

### Configuring Settings
- [var rememberJoinedNetworks: Bool](./rememberjoinednetworks.md)
  A Boolean value that determines whether to remember all joined Wi-Fi networks unless the user specifies otherwise when joining a particular Wi-Fi network.
- [var requireAdministratorForAssociation: Bool](./requireadministratorforassociation.md)
  A Boolean value that determines whether to require an administrator password to change networks.
- [var requireAdministratorForPower: Bool](./requireadministratorforpower.md)
  A Boolean value that determines whether to require an administrator password to change the interface power state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corewlan/cwmutableconfiguration/requireadministratorforibssmode)*