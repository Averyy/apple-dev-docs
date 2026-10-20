# rememberJoinedNetworks

**Framework**: Core WLAN  
**Kind**: property  
**Role**: Instance Property

AirPort client will remember all joined networks.

**Availability**:
- macOS 10.7+

## Declaration

```swift
var rememberJoinedNetworks: Bool { get }
```

```objc
@property (readonly) BOOL rememberJoinedNetworks;
```

## See Also

### Instance Properties
- [var networkProfiles: NSOrderedSet](./networkprofiles.md)
  An array of remembered CWNetworkProfile objects.
- [var requireAdministratorForAssociation: Bool](./requireadministratorforassociation.md)
  Require an administrator password to change networks.
- [var requireAdministratorForIBSSMode: Bool](./requireadministratorforibssmode.md)
  Require an administrator password to create a computer-to-computer network.
- [var requireAdministratorForPower: Bool](./requireadministratorforpower.md)
  Require an administrator password to change the interface power state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corewlan/cwconfiguration/rememberjoinednetworks)*