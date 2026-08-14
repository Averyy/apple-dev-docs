# DeviceActivityData.CategoryActivity

**Framework**: Device Activity  
**Kind**: struct

Categorized representation of application and web domain activity.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+

## Declaration

```swift
struct CategoryActivity
```

## Topics

### Identifying the category
- [var category: ActivityCategory](deviceactivitydata/categoryactivity/category.md)
  Access the category of the activity.
### Measuring activity
- [var totalActivityDuration: TimeInterval](deviceactivitydata/categoryactivity/totalactivityduration.md)
  Access the total activity time for this category.
### Accessing contributing activities
- [var applications: DeviceActivityResults<DeviceActivityData.ApplicationActivity>](deviceactivitydata/categoryactivity/applications.md)
  Access the application activity that contributed to this category’s total activity time.
- [var webDomains: DeviceActivityResults<DeviceActivityData.WebDomainActivity>](deviceactivitydata/categoryactivity/webdomains.md)
  Access the web domain activity that contributed to this category’s total activity time.

## Relationships

### Conforms To
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)

## See Also

- [DeviceActivityData.ApplicationActivity](deviceactivitydata/applicationactivity.md)
  Activity data for an application.
- [DeviceActivityData.WebDomainActivity](deviceactivitydata/webdomainactivity.md)
  Activity data for a web domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/deviceactivity/deviceactivitydata/categoryactivity)*