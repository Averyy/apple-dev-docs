# threshold

**Framework**: DeviceActivity  
**Kind**: property

The amount of time to monitor the provided applications, categories, and web domains.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+

## Declaration

```swift
var threshold: DateComponents { get }
```

#### Discussion

Once the activity exceeds the threshold, the system invokes the [`eventDidReachThreshold(_:activity:)`](deviceactivitymonitor/eventdidreachthreshold(_:activity:).md) method of the application extension’s principal class.

## See Also

- [var applications: Set<ApplicationToken>](deviceactivityevent/applications.md)
  The applications that the event includes.
- [var categories: Set<ActivityCategoryToken>](deviceactivityevent/categories.md)
  The categories that the event includes.
- [var webDomains: Set<WebDomainToken>](deviceactivityevent/webdomains.md)
  The web domains that the event includes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/deviceactivity/deviceactivityevent/threshold)*