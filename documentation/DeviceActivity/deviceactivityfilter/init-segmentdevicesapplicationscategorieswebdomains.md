# init(segment:devices:applications:categories:webDomains:)

**Framework**: DeviceActivity  
**Kind**: init

Creates a new filter for the current user.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+

## Declaration

```swift
init(segment segmentInterval: DeviceActivityFilter.SegmentInterval = .hourly(), devices: DeviceActivityFilter.Devices? = nil, applications: Set<ApplicationToken> = [], categories: Set<ActivityCategoryToken> = [], webDomains: Set<WebDomainToken> = [])
```

#### Discussion

If you specify `applications`, `categories` or `webDomains`, then the system provides activity data for the requested application, categories, and web domains only. Conversely, if you do not specify any `applications`, `categories`, or `webDomains`, then the system provides data for all types of device activity. If you do not specify any `devices`, then the filter only includes data for the current device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/deviceactivity/deviceactivityfilter/init(segment:devices:applications:categories:webdomains:))*