# DeviceActivityData.ApplicationActivity

**Framework**: Device Activity  
**Kind**: struct  
**Role**: Structure

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
- [var application: Application](./applicationactivity/application.md)
  Access the application that accumulated the activity.
### Measuring activity
- [var totalActivityDuration: TimeInterval](./applicationactivity/totalactivityduration.md)
  Access the total activity time for this application.
### Tracking usage
- [var numberOfPickups: Int](./applicationactivity/numberofpickups.md)
  Access the number of pickups made directly to the application.
- [var numberOfNotifications: Int](./applicationactivity/numberofnotifications.md)
  Access the number of notifications made by the application.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)

## See Also

### Organizing activity by type
- [DeviceActivityData.CategoryActivity](./categoryactivity.md)
  Categorized representation of application and web domain activity.
- [DeviceActivityData.WebDomainActivity](./webdomainactivity.md)
  Activity data for a web domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/deviceactivity/deviceactivitydata/applicationactivity)*