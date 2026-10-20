# DeviceActivityData.WebDomainActivity

**Framework**: Device Activity  
**Kind**: struct  
**Role**: Structure

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
- [var webDomain: WebDomain](./webdomainactivity/webdomain.md)
  Access the web domain that accumulated the activity.
### Measuring activity
- [var totalActivityDuration: TimeInterval](./webdomainactivity/totalactivityduration.md)
  Access the total activity time for this web domain.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)

## See Also

### Organizing activity by type
- [DeviceActivityData.ApplicationActivity](./applicationactivity.md)
  Activity data for an application.
- [DeviceActivityData.CategoryActivity](./categoryactivity.md)
  Categorized representation of application and web domain activity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/deviceactivity/deviceactivitydata/webdomainactivity)*