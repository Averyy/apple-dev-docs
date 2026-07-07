# reportInterval

**Framework**: Network Extension  
**Kind**: property

The time interval (in seconds) at which the system sends reports of blocked URLs.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)

## Declaration

```swift
var reportInterval: TimeInterval { get set }
```

#### Discussion

This value defaults to `86400`, equal to one day. The minimum allowed interval is `3600` (one hour).

## See Also

- [var reportEndpoint: String?](neurlfiltermanager/reportendpoint.md)
  The endpoint that the filter manager sends blocked URL reports to.
- [var reportFormat: NEURLFilterManager.ReportFormat](neurlfiltermanager/reportformat-swift.property.md)
  The format the manager uses to send blocked URL reports.
- [NEURLFilterManager.ReportFormat](neurlfiltermanager/reportformat-swift.enum.md)
  An enumertion of report format types used when reporting blocked URLs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/neurlfiltermanager/reportinterval)*