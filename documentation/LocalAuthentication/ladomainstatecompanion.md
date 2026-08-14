# LADomainStateCompanion

**Framework**: Local Authentication  
**Kind**: class

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+

## Declaration

```swift
class LADomainStateCompanion
```

## Topics

### Instance Properties
- [var availableCompanionTypes: Set<LACompanionType>](ladomainstatecompanion/availablecompaniontypes-1t7ur.md)
- [var stateHash: Data?](ladomainstatecompanion/statehash.md)
  Contains combined state hash data for all available companion types. . Returns `nil` if no companion devices are paired.
### Instance Methods
- [func stateHash(for: LACompanionType) -> Data?](ladomainstatecompanion/statehash(for:).md)
  Returns state hash data for the given companion type.

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/localauthentication/ladomainstatecompanion)*