# networkProfiles

**Framework**: Core WLAN  
**Kind**: property  
**Role**: Instance Property

An array of remembered CWNetworkProfile objects.

**Availability**:
- macOS 10.7+

## Declaration

```swift
@NSCopying
var networkProfiles: NSOrderedSet { get }
```

```objc
@property (copy, readonly) NSOrderedSet<CWNetworkProfile *> * networkProfiles;
```

## Discussion

The order of this array corresponds to the order in which the the CWNetworkProfile objects participate in the auto-join process.

## See Also

### Instance Properties
- [var rememberJoinedNetworks: Bool](./rememberjoinednetworks.md)
  AirPort client will remember all joined networks.
- [var requireAdministratorForAssociation: Bool](./requireadministratorforassociation.md)
  Require an administrator password to change networks.
- [var requireAdministratorForIBSSMode: Bool](./requireadministratorforibssmode.md)
  Require an administrator password to create a computer-to-computer network.
- [var requireAdministratorForPower: Bool](./requireadministratorforpower.md)
  Require an administrator password to change the interface power state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corewlan/cwconfiguration/networkprofiles)*