# DeviceActivityData.ApplicationActivity

**Framework**: Device Activity  
**Kind**: struct

Activity data for an application.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+

## Declaration

```swift
struct ApplicationActivity
```

## Topics

### Identifying the application
- [var application: Application](deviceactivitydata/applicationactivity/application.md)
  Access the application that accumulated the activity.
### Measuring activity
- [var totalActivityDuration: TimeInterval](deviceactivitydata/applicationactivity/totalactivityduration.md)
  Access the total activity time for this application.
### Tracking usage
- [var numberOfPickups: Int](deviceactivitydata/applicationactivity/numberofpickups.md)
  Access the number of pickups made directly to the application.
- [var numberOfNotifications: Int](deviceactivitydata/applicationactivity/numberofnotifications.md)
  Access the number of notifications made by the application.

## Relationships

### Conforms To
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)

## See Also

- [DeviceActivityData.CategoryActivity](deviceactivitydata/categoryactivity.md)
  Categorized representation of application and web domain activity.
- [DeviceActivityData.WebDomainActivity](deviceactivitydata/webdomainactivity.md)
  Activity data for a web domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/deviceactivity/deviceactivitydata/applicationactivity)*