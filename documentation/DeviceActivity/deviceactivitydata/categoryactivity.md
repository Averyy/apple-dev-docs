# DeviceActivityData.CategoryActivity

**Framework**: Device Activity  
**Kind**: struct  
**Role**: Structure

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
- [var category: ActivityCategory](./categoryactivity/category.md)
  Access the category of the activity.
### Measuring activity
- [var totalActivityDuration: TimeInterval](./categoryactivity/totalactivityduration.md)
  Access the total activity time for this category.
### Accessing contributing activities
- [var applications: DeviceActivityResults<DeviceActivityData.ApplicationActivity>](./categoryactivity/applications.md)
  Access the application activity that contributed to this category’s total activity time.
- [var webDomains: DeviceActivityResults<DeviceActivityData.WebDomainActivity>](./categoryactivity/webdomains.md)
  Access the web domain activity that contributed to this category’s total activity time.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)

## See Also

### Organizing activity by type
- [DeviceActivityData.ApplicationActivity](./applicationactivity.md)
  Activity data for an application.
- [DeviceActivityData.WebDomainActivity](./webdomainactivity.md)
  Activity data for a web domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/deviceactivity/deviceactivitydata/categoryactivity)*