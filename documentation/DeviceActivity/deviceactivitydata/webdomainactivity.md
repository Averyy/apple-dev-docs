# DeviceActivityData.WebDomainActivity

**Framework**: Device Activity  
**Kind**: struct

Activity data for a web domain.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+

## Declaration

```swift
struct WebDomainActivity
```

## Topics

### Identifying the web domain
- [var webDomain: WebDomain](deviceactivitydata/webdomainactivity/webdomain.md)
  Access the web domain that accumulated the activity.
### Measuring activity
- [var totalActivityDuration: TimeInterval](deviceactivitydata/webdomainactivity/totalactivityduration.md)
  Access the total activity time for this web domain.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)

## See Also

- [DeviceActivityData.ApplicationActivity](deviceactivitydata/applicationactivity.md)
  Activity data for an application.
- [DeviceActivityData.CategoryActivity](deviceactivitydata/categoryactivity.md)
  Categorized representation of application and web domain activity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/deviceactivity/deviceactivitydata/webdomainactivity)*