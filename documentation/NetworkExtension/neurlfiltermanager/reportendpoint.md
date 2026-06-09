# reportEndpoint

**Framework**: Network Extension  
**Kind**: property

The endpoint that the filter manager sends blocked URL reports to.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst ?+
- macOS 27.0+ (Beta)

## Declaration

```swift
var reportEndpoint: String? { get set }
```

#### Discussion

When configured, the manager sends reports of blocked URLs to the specified endpoint on the PIR server URL. In other words, for a PIR server at `https://pir.example.com/` and an endpoint of `reports`, the manager sends reports to `https://pir.example.com/reports`.

The manager sends reports periodically, as determined by the [`reportInterval`](neurlfiltermanager/reportinterval.md) property, using the format specified by [`reportFormat`](neurlfiltermanager/reportformat-swift.property.md). Each report is an HTTPS POST request, containing a list of blocked URLs accumulated during the last reporting period. The system authenticates and sends reports over the same OHTTP relay as the PIR traffic. Due to the system’s schedulding mechanism, your reporting system should allow slight deviations between the scheduled time and the actual performance of the task.

Reporting is available only on supervised devices. If you set this property on a non-supervised device, the manager will save the configuration but won’t send any reports.

To disable reporting, set this property to `nil`.

## See Also

- [var reportFormat: NEURLFilterManager.ReportFormat](neurlfiltermanager/reportformat-swift.property.md)
  The format the manager uses to send blocked URL reports.
- [NEURLFilterManager.ReportFormat](neurlfiltermanager/reportformat-swift.enum.md)
  An enumertion of report format types used when reporting blocked URLs.
- [var reportInterval: TimeInterval](neurlfiltermanager/reportinterval.md)
  The time interval (in seconds) at which the system sends reports of blocked URLs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/neurlfiltermanager/reportendpoint)*