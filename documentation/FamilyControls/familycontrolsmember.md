# FamilyControlsMember

**Framework**: FamilyControls  
**Kind**: enum

The type of account that Family Controls is currently managing.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+

## Declaration

```swift
@objc
enum FamilyControlsMember
```

## Topics

### Enumeration Cases
- [FamilyControlsMember.child](familycontrolsmember/child.md)
  A value indicating that Family Controls is managing a child account, so that a parent or guardian must enter their authorization credentials.
- [FamilyControlsMember.individual](familycontrolsmember/individual.md)
  A value indicating that Family Controls is managing an individual account, so that the user can enter their authorization credentials.
### Instance Properties
- [var description: String](familycontrolsmember/description.md)
  A nonlocalized description of the type of account, suitable for debugging.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/familycontrols/familycontrolsmember)*