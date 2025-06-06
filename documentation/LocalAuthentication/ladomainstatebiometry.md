# LADomainStateBiometry

**Framework**: Local Authentication  
**Kind**: class

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
class LADomainStateBiometry
```

## Topics

### Instance Properties
- [var biometryType: LABiometryType](ladomainstatebiometry/biometrytype.md)
  Indicates biometry type available on the device.
- [var stateHash: Data?](ladomainstatebiometry/statehash.md)
  Contains state hash data for the available biometry type. Returns `nil` if no biometry entities are enrolled.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/localauthentication/ladomainstatebiometry)*