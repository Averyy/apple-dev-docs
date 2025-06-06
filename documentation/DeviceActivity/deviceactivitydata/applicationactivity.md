# DeviceActivityData.ApplicationActivity

**Framework**: DeviceActivity  
**Kind**: struct

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+

## Declaration

```swift
struct ApplicationActivity
```

## Topics

### Operators
- [static func == (DeviceActivityData.ApplicationActivity, DeviceActivityData.ApplicationActivity) -> Bool](deviceactivitydata/applicationactivity/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Instance Properties
- [var application: Application](deviceactivitydata/applicationactivity/application.md)
  The application that accumulated the activity.
- [var hashValue: Int](deviceactivitydata/applicationactivity/hashvalue.md)
  The hash value.
- [var numberOfNotifications: Int](deviceactivitydata/applicationactivity/numberofnotifications.md)
  The number of notifications made by the application.
- [var numberOfPickups: Int](deviceactivitydata/applicationactivity/numberofpickups.md)
  The number of pickups made directly to the application.
- [var totalActivityDuration: TimeInterval](deviceactivitydata/applicationactivity/totalactivityduration.md)
  The total activity for this application.
### Instance Methods
- [func hash(into: inout Hasher)](deviceactivitydata/applicationactivity/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Default Implementations
- [Equatable Implementations](deviceactivitydata/applicationactivity/equatable-implementations.md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/deviceactivity/deviceactivitydata/applicationactivity)*