# CrashDiagnostic.ObjectiveCExceptionReason

**Framework**: MetricKit  
**Kind**: struct

Detailed information about an uncaught Objective-C exception that caused a crash.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct ObjectiveCExceptionReason
```

## Topics

### Exception description
- [let composedMessage: String](crashdiagnostic/objectivecexceptionreason/composedmessage.md)
  A human-readable message string summarizing the reason for the exception.
- [let formatString: String](crashdiagnostic/objectivecexceptionreason/formatstring.md)
  A string representing the exception message before arguments are substituted.
- [let arguments: [String]](crashdiagnostic/objectivecexceptionreason/arguments.md)
  Arguments passed to the format string.
### Exception type
- [let exceptionType: String](crashdiagnostic/objectivecexceptionreason/exceptiontype.md)
  A human-readable string denoting type of the exception.
- [let className: String](crashdiagnostic/objectivecexceptionreason/classname.md)
  The class name of the exception
- [let exceptionName: String](crashdiagnostic/objectivecexceptionreason/exceptionname.md)
  The name of the exception.

## Relationships

### Conforms To
- [Decodable](../swift/decodable.md)
- [Encodable](../swift/encodable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/crashdiagnostic/objectivecexceptionreason)*