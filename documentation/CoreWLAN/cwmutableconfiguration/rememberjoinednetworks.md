# rememberJoinedNetworks

**Framework**: Core WLAN  
**Kind**: property  
**Role**: Instance Property

A Boolean value that determines whether to remember all joined Wi-Fi networks unless the user specifies otherwise when joining a particular Wi-Fi network.

**Availability**:
- macOS 10.7+

## Declaration

```swift
var rememberJoinedNetworks: Bool { get set }
```

```objc
@property BOOL rememberJoinedNetworks;
```

## See Also

### Configuring Settings
- [var requireAdministratorForAssociation: Bool](./requireadministratorforassociation.md)
  A Boolean value that determines whether to require an administrator password to change networks.
- [var requireAdministratorForPower: Bool](./requireadministratorforpower.md)
  A Boolean value that determines whether to require an administrator password to change the interface power state.
- [var requireAdministratorForIBSSMode: Bool](./requireadministratorforibssmode.md)
  A Boolean value that determines whether to require an administrator password to create a computer-to-computer network.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corewlan/cwmutableconfiguration/rememberjoinednetworks)*