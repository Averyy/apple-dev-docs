# applications

**Framework**: DeviceActivity  
**Kind**: property

The applications that the event includes.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+

## Declaration

```swift
var applications: Set<ApplicationToken> { get }
```

## See Also

- [var categories: Set<ActivityCategoryToken>](deviceactivityevent/categories.md)
  The categories that the event includes.
- [var webDomains: Set<WebDomainToken>](deviceactivityevent/webdomains.md)
  The web domains that the event includes.
- [var threshold: DateComponents](deviceactivityevent/threshold.md)
  The amount of time to monitor the provided applications, categories, and web domains.


---

*[View on Apple Developer](https://developer.apple.com/documentation/deviceactivity/deviceactivityevent/applications)*