# LAEnvironment

**Framework**: Local Authentication  
**Kind**: class

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
class LAEnvironment
```

## Topics

### Classes
- [LAEnvironment.Mechanism](laenvironment/mechanism.md)
- [LAEnvironment.MechanismBiometry](laenvironment/mechanismbiometry.md)
- [LAEnvironment.MechanismCompanion](laenvironment/mechanismcompanion.md)
- [LAEnvironment.MechanismUserPassword](laenvironment/mechanismuserpassword.md)
- [LAEnvironment.State](laenvironment/state-swift.class.md)
### Protocols
- [LAEnvironment.Observer](laenvironment/observer.md)
### Instance Properties
- [var state: LAEnvironment.State](laenvironment/state-swift.property.md)
  The environment state information.
### Instance Methods
- [func addObserver(any LAEnvironment.Observer)](laenvironment/addobserver(_:).md)
- [func removeObserver(any LAEnvironment.Observer)](laenvironment/removeobserver(_:).md)
### Type Properties
- [class var currentUser: LAEnvironment](laenvironment/currentuser.md)
  Environment of the current user.

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

*[View on Apple Developer](https://developer.apple.com/documentation/localauthentication/laenvironment)*