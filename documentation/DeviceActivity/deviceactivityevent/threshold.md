# threshold

**Framework**: Device Activity  
**Kind**: property  
**Role**: Instance Property

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

Once the activity exceeds the threshold, the system invokes the [`eventDidReachThreshold(_:activity:)`](../deviceactivitymonitor/eventdidreachthreshold%28_,activity%29.md) method of the application extension’s principal class.

## See Also

### Including Objects in an Event
- [var applications: Set<ApplicationToken>](./applications.md)
  The applications that the event includes.
- [var categories: Set<ActivityCategoryToken>](./categories.md)
  The categories that the event includes.
- [var webDomains: Set<WebDomainToken>](./webdomains.md)
  The web domains that the event includes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/deviceactivity/deviceactivityevent/threshold)*