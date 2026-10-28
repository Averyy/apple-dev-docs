# reportInterval

**Framework**: Network Extension  
**Kind**: property  
**Role**: Instance Property

The time interval (in seconds) at which the system sends reports of blocked URLs.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+

## Declaration

```swift
var reportInterval: TimeInterval { get set }
```

## Discussion

This value defaults to `86400`, equal to one day. The minimum allowed interval is `3600` (one hour).

## See Also

### Producing filtering reports
- [var reportEndpoint: String?](./reportendpoint.md)
  The endpoint that the filter manager sends blocked URL reports to.
- [var reportFormat: NEURLFilterManager.ReportFormat](./reportformat-swift.property.md)
  The format the manager uses to send blocked URL reports.
- [NEURLFilterManager.ReportFormat](./reportformat-swift.enum.md)
  An enumertion of report format types used when reporting blocked URLs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/neurlfiltermanager/reportinterval)*