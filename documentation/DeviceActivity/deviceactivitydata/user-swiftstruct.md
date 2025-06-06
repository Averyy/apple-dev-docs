# DeviceActivityData.User

**Framework**: DeviceActivity  
**Kind**: struct

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+

## Declaration

```swift
struct User
```

## Topics

### Operators
- [static func == (DeviceActivityData.User, DeviceActivityData.User) -> Bool](deviceactivitydata/user-swift.struct/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Instance Properties
- [var appleID: String?](deviceactivitydata/user-swift.struct/appleid.md)
  The AppleID of the user.
- [var hashValue: Int](deviceactivitydata/user-swift.struct/hashvalue.md)
  The hash value.
- [var nameComponents: PersonNameComponents?](deviceactivitydata/user-swift.struct/namecomponents.md)
  The user’s name.
- [var role: DeviceActivityData.User.FamilyRole](deviceactivitydata/user-swift.struct/role.md)
  The type of the user.
### Instance Methods
- [func hash(into: inout Hasher)](deviceactivitydata/user-swift.struct/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Enumerations
- [DeviceActivityData.User.FamilyRole](deviceactivitydata/user-swift.struct/familyrole.md)
  A type describing the user’s role in their iCloud family.
### Default Implementations
- [Equatable Implementations](deviceactivitydata/user-swift.struct/equatable-implementations.md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/deviceactivity/deviceactivitydata/user-swift.struct)*