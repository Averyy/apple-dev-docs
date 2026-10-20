# LADomainStateCompanion

**Framework**: Local Authentication  
**Kind**: class  
**Role**: Class

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+

## Declaration

```swift
class LADomainStateCompanion
```

```objc
@interface LADomainStateCompanion : NSObject
```

## Topics

### Instance Properties
- [var availableCompanionTypes: Set<LACompanionType>](./ladomainstatecompanion/availablecompaniontypes-1t7ur.md)
- [var stateHash: Data?](./ladomainstatecompanion/statehash.md)
  Contains combined state hash data for all available companion types. . Returns `nil` if no companion devices are paired.
### Instance Methods
- [func stateHash(for: LACompanionType) -> Data?](./ladomainstatecompanion/statehash%28for%29.md)
  Returns state hash data for the given companion type.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/localauthentication/ladomainstatecompanion)*