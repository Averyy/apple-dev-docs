# DeviceActivityName

**Framework**: DeviceActivity  
**Kind**: struct

The unique name of an activity.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+

## Declaration

```swift
struct DeviceActivityName
```

#### Overview

Use `DeviceActivityName` to associate an activity with some of your application’s data. It’s not possible to have multiple activities with the same name. Monitoring a second activity with the same name as a previous activity overwrites the schedule for the first one.

## Topics

### Creating an Instance
- [init(rawValue: String)](deviceactivityname/init(rawvalue:).md)
  Creates a new instance with the specified raw value.
- [init(String)](deviceactivityname/init(_:).md)
  Creates a new instance with the specified raw value.
- [var rawValue: String](deviceactivityname/rawvalue-swift.property.md)
  The corresponding value of the raw type.
### Identifying and Comparing Errors
- [var hashValue: Int](deviceactivityname/hashvalue.md)
  The hash value.
- [func hash(into: inout Hasher)](deviceactivityname/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
- [static func != (Self, Self) -> Bool](deviceactivityname/!=(_:_:).md)
  Returns a Boolean value that indicates whether two values aren’t equal.
### Type Aliases
- [DeviceActivityName.RawValue](deviceactivityname/rawvalue-swift.typealias.md)
  The raw type that can be used to represent all values of the conforming type.
### Default Implementations
- [Equatable Implementations](deviceactivityname/equatable-implementations.md)
- [RawRepresentable Implementations](deviceactivityname/rawrepresentable-implementations.md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)

## See Also

- [struct DeviceActivityEvent](deviceactivityevent.md)
  An event that represents an application, category, or website activity.
- [struct DeviceActivitySchedule](deviceactivityschedule.md)
  A calendar-based schedule for when to monitor a device’s activity.
- [struct DeviceActivityCenter](deviceactivitycenter.md)
  A class that enables an application’s extension to start monitoring scheduled device activity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/deviceactivity/deviceactivityname)*