# DeviceActivityData.CategoryActivity

**Framework**: DeviceActivity  
**Kind**: struct

A categorized representation of a user’s application and web domain activity.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+

## Declaration

```swift
struct CategoryActivity
```

## Topics

### Instance Properties
- [var applications: DeviceActivityResults<DeviceActivityData.ApplicationActivity>](deviceactivitydata/categoryactivity/applications.md)
  The user’s application activity that contributed to this category’s [`totalActivityDuration`](deviceactivitydata/categoryactivity/totalactivityduration.md).
- [var category: ActivityCategory](deviceactivitydata/categoryactivity/category.md)
  The category of the activity.
- [var totalActivityDuration: TimeInterval](deviceactivitydata/categoryactivity/totalactivityduration.md)
  The user’s total activity for this category.
- [var webDomains: DeviceActivityResults<DeviceActivityData.WebDomainActivity>](deviceactivitydata/categoryactivity/webdomains.md)
  The user’s web domain activity that contributed to this category’s [`totalActivityDuration`](deviceactivitydata/categoryactivity/totalactivityduration.md).

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/deviceactivity/deviceactivitydata/categoryactivity)*