# NEURLFilterManager.ReportFormat

**Framework**: Network Extension  
**Kind**: enum

An enumertion of report format types used when reporting blocked URLs.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)

## Declaration

```swift
enum ReportFormat
```

## Topics

### Report formats
- [NEURLFilterManager.ReportFormat.json](neurlfiltermanager/reportformat-swift.enum/json.md)
  JSON format for reports.
- [NEURLFilterManager.ReportFormat.protobuf](neurlfiltermanager/reportformat-swift.enum/protobuf.md)
  Protocol Buffers format for reports.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var reportEndpoint: String?](neurlfiltermanager/reportendpoint.md)
  The endpoint that the filter manager sends blocked URL reports to.
- [var reportFormat: NEURLFilterManager.ReportFormat](neurlfiltermanager/reportformat-swift.property.md)
  The format the manager uses to send blocked URL reports.
- [var reportInterval: TimeInterval](neurlfiltermanager/reportinterval.md)
  The time interval (in seconds) at which the system sends reports of blocked URLs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/neurlfiltermanager/reportformat-swift.enum)*