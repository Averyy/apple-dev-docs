# NEVPNIKEv2PPKConfiguration

**Framework**: Network Extension  
**Kind**: class

A class that manages parameters of a post-quantum pre-shared key (PPK).

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
class NEVPNIKEv2PPKConfiguration
```

#### Discussion

Instances of this class are thread safe. The class conforms to RFC 8784.

## Topics

### Creating a PPK configuration
- [init(identifier: String, keychainReference: Data)](nevpnikev2ppkconfiguration/init(identifier:keychainreference:).md)
  Initializes a quantum-secure pre-shared key (PPK) configuration.
### Accessing the configuration parameters
- [var identifier: String](nevpnikev2ppkconfiguration/identifier.md)
  The identifier for the PPK.
- [var keychainReference: Data](nevpnikev2ppkconfiguration/keychainreference.md)
  A persistent reference to the key in the keychain.
- [var isMandatory: Bool](nevpnikev2ppkconfiguration/ismandatory.md)
  A Boolean value that indicates whether it’s mandatory for the VPN server to use this PPK.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [var allowPostQuantumKeyExchangeFallback: Bool](nevpnprotocolikev2/allowpostquantumkeyexchangefallback.md)
  A Boolean value that indicates whether servers that don’t support post-quantum key exchanges can skip them.
- [var ppkConfiguration: NEVPNIKEv2PPKConfiguration?](nevpnprotocolikev2/ppkconfiguration.md)
  The configuration for a post-quantum pre-shared key (PPK).


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nevpnikev2ppkconfiguration)*