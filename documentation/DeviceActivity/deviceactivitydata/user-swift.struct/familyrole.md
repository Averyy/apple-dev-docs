# DeviceActivityData.User.FamilyRole

**Framework**: DeviceActivity  
**Kind**: enum

A type describing the user’s role in their iCloud family.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+

## Declaration

```swift
enum FamilyRole
```

#### Overview

If the user is not signed into an iCloud account or in an iCloud family, then they are an `individual`.

## Topics

### Enumeration Cases
- [DeviceActivityData.User.FamilyRole.child](deviceactivitydata/user-swift.struct/familyrole/child.md)
  A child that is being managed by a parent or guardian in their iCloud family.
- [DeviceActivityData.User.FamilyRole.individual](deviceactivitydata/user-swift.struct/familyrole/individual.md)
  An individual that has authorized your app with `FamilyControls`.
### Initializers
- [init?(rawValue: Int)](deviceactivitydata/user-swift.struct/familyrole/init(rawvalue:).md)
  Creates a new instance with the specified raw value.
### Instance Properties
- [var rawValue: Int](deviceactivitydata/user-swift.struct/familyrole/rawvalue-swift.property.md)
  The corresponding value of the raw type.
### Type Aliases
- [DeviceActivityData.User.FamilyRole.RawValue](deviceactivitydata/user-swift.struct/familyrole/rawvalue-swift.typealias.md)
  The raw type that can be used to represent all values of the conforming type.
### Default Implementations
- [Equatable Implementations](deviceactivitydata/user-swift.struct/familyrole/equatable-implementations.md)
- [RawRepresentable Implementations](deviceactivitydata/user-swift.struct/familyrole/rawrepresentable-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/deviceactivity/deviceactivitydata/user-swift.struct/familyrole)*