# CLSProgressReportingCapability

**Framework**: ClassKit  
**Kind**: class  
**Role**: Class

A progress reporting capability supported by a context.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
class CLSProgressReportingCapability
```

```objc
@interface CLSProgressReportingCapability : CLSObject
```

#### Overview

You use activities to report metrics about a student’s progress through the task associated with a context. Every activity automatically measures time spent performing the task, but you can provide additional information, like the completion percentage, or a final score.

To help teachers understand what to expect from a context, create a set of [`CLSProgressReportingCapability`](./clsprogressreportingcapability.md) instances — one for each kind of metric the context reports. Add the complete set to the context by calling the [`addProgressReportingCapabilities(_:)`](./clscontext/addprogressreportingcapabilities%28_%29.md) method.

When you create a reporting capability, include a brief description of the capability as a localized string in the [`details`](./clsprogressreportingcapability/details.md) property. Schoolwork presents this to teachers to provide additional information about the metric.

## Topics

### Creating a Progress Reporting Capability
- [init(kind: CLSProgressReportingCapability.Kind, details: String?)](./clsprogressreportingcapability/init%28kind,details%29.md)
  Creates a new progress reporting capability of the given type with a descriptive string.
### Characterizing the Capability
- [var details: String?](./clsprogressreportingcapability/details.md)
  A description of the capability presented to teachers.
- [var kind: CLSProgressReportingCapability.Kind](./clsprogressreportingcapability/kind-swift.property.md)
  The kind of progress reporting capability.
- [CLSProgressReportingCapability.Kind](./clsprogressreportingcapability/kind-swift.enum.md)
  The available kinds of progress reporting that a context can perform.

## Relationships

### Inherits From
- [CLSObject](./clsobject.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)

## See Also

### Indicating progress reporting capabilities
- [var progressReportingCapabilities: Set<CLSProgressReportingCapability>](./clscontext/progressreportingcapabilities.md)
  The kinds of progress reporting that the context can perform.
- [func addProgressReportingCapabilities(Set<CLSProgressReportingCapability>)](./clscontext/addprogressreportingcapabilities%28_%29.md)
  Adds a progress reporting capability to the set of capabilities for the context.
- [func resetProgressReportingCapabilities()](./clscontext/resetprogressreportingcapabilities%28%29.md)
  Resets the set of capabilities for the context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/classkit/clsprogressreportingcapability)*