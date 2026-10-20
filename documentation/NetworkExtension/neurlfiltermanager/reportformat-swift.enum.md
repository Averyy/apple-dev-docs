# NEURLFilterManager.ReportFormat

**Framework**: Network Extension  
**Kind**: enum  
**Role**: Enumeration

An enumertion of report format types used when reporting blocked URLs.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+

## Declaration

```swift
enum ReportFormat
```

## Topics

### Report formats
- [NEURLFilterManager.ReportFormat.json](./reportformat-swift.enum/json.md)
  JSON format for reports.
- [NEURLFilterManager.ReportFormat.protobuf](./reportformat-swift.enum/protobuf.md)
  Protocol Buffers format for reports.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Producing filtering reports
- [var reportEndpoint: String?](./reportendpoint.md)
  The endpoint that the filter manager sends blocked URL reports to.
- [var reportFormat: NEURLFilterManager.ReportFormat](./reportformat-swift.property.md)
  The format the manager uses to send blocked URL reports.
- [var reportInterval: TimeInterval](./reportinterval.md)
  The time interval (in seconds) at which the system sends reports of blocked URLs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/neurlfiltermanager/reportformat-swift.enum)*