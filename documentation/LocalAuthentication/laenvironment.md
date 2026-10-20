# LAEnvironment

**Framework**: Local Authentication  
**Kind**: class  
**Role**: Class

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

```objc
@interface LAEnvironment : NSObject
```

## Topics

### Classes
- [LAEnvironment.Mechanism](./laenvironment/mechanism.md)
- [LAEnvironment.MechanismBiometry](./laenvironment/mechanismbiometry.md)
- [LAEnvironment.MechanismCompanion](./laenvironment/mechanismcompanion.md)
- [LAEnvironment.MechanismUserPassword](./laenvironment/mechanismuserpassword.md)
- [LAEnvironment.State](./laenvironment/state-swift.class.md)
### Protocols
- [LAEnvironment.Observer](./laenvironment/observer.md)
### Instance Properties
- [var state: LAEnvironment.State](./laenvironment/state-swift.property.md)
  The environment state information.
### Instance Methods
- [func addObserver(any LAEnvironment.Observer)](./laenvironment/addobserver%28_%29.md)
- [func removeObserver(any LAEnvironment.Observer)](./laenvironment/removeobserver%28_%29.md)
### Type Properties
- [class var currentUser: LAEnvironment](./laenvironment/currentuser.md)
  Environment of the current user.

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

*[View on Apple Developer](https://developer.apple.com/documentation/localauthentication/laenvironment)*