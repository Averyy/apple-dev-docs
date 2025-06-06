# DeviceActivityFilter.Users

**Framework**: DeviceActivity  
**Kind**: struct

A type your app uses to indicate which users to include in a device activity report.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+

## Declaration

```swift
struct Users
```

## Topics

### Operators
- [static func == (DeviceActivityFilter.Users, DeviceActivityFilter.Users) -> Bool](deviceactivityfilter/users-swift.struct/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Instance Properties
- [var hashValue: Int](deviceactivityfilter/users-swift.struct/hashvalue.md)
  The hash value.
### Instance Methods
- [func hash(into: inout Hasher)](deviceactivityfilter/users-swift.struct/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Type Properties
- [static let all: DeviceActivityFilter.Users](deviceactivityfilter/users-swift.struct/all.md)
  Filters data for all users that the current iCloud user has permission to report device activity.
- [static let children: DeviceActivityFilter.Users](deviceactivityfilter/users-swift.struct/children.md)
  Filters data for the children in the current user’s iCloud family.
### Default Implementations
- [Equatable Implementations](deviceactivityfilter/users-swift.struct/equatable-implementations.md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/deviceactivity/deviceactivityfilter/users-swift.struct)*