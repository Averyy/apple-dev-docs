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

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/deviceactivity/deviceactivitydata/user-swift.struct/familyrole)*