# CrashDiagnostic.ObjectiveCExceptionReason

**Framework**: MetricKit  
**Kind**: struct  
**Role**: Structure

Detailed information about an uncaught Objective-C exception that caused a crash.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+

## Declaration

```swift
struct ObjectiveCExceptionReason
```

## Topics

### Exception description
- [let composedMessage: String](./objectivecexceptionreason/composedmessage.md)
  A human-readable message string summarizing the reason for the exception.
- [let formatString: String](./objectivecexceptionreason/formatstring.md)
  A string representing the exception message before arguments are substituted.
- [let arguments: [String]](./objectivecexceptionreason/arguments.md)
  Arguments passed to the format string.
### Exception type
- [let exceptionType: String](./objectivecexceptionreason/exceptiontype.md)
  A human-readable string denoting type of the exception.
- [let className: String](./objectivecexceptionreason/classname.md)
  The class name of the exception
- [let exceptionName: String](./objectivecexceptionreason/exceptionname.md)
  The name of the exception.

## Relationships

### Conforms To
- [Decodable](../../Swift/decodable.md)
- [Encodable](../../Swift/encodable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/crashdiagnostic/objectivecexceptionreason)*