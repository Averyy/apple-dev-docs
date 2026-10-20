# requireAdministratorForPower

**Framework**: Core WLAN  
**Kind**: property  
**Role**: Instance Property

Require an administrator password to change the interface power state.

**Availability**:
- macOS 10.7+

## Declaration

```swift
var requireAdministratorForPower: Bool { get }
```

```objc
@property (readonly) BOOL requireAdministratorForPower;
```

## See Also

### Instance Properties
- [var networkProfiles: NSOrderedSet](./networkprofiles.md)
  An array of remembered CWNetworkProfile objects.
- [var rememberJoinedNetworks: Bool](./rememberjoinednetworks.md)
  AirPort client will remember all joined networks.
- [var requireAdministratorForAssociation: Bool](./requireadministratorforassociation.md)
  Require an administrator password to change networks.
- [var requireAdministratorForIBSSMode: Bool](./requireadministratorforibssmode.md)
  Require an administrator password to create a computer-to-computer network.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corewlan/cwconfiguration/requireadministratorforpower)*