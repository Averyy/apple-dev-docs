# AEAssessmentBinaryExecutableConfiguration

**Framework**: Automatic Assessment Configuration  
**Kind**: class

The configuration applied to an [`AEAssessmentBinaryExecutable`](aeassessmentbinaryexecutable.md) participant.

**Availability**:
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)

## Declaration

```swift
class AEAssessmentBinaryExecutableConfiguration
```

#### Overview

A non-bundled executable (such as a launchd daemon) is headless, so it supports only the subset of participant policies that apply to a process without UI: network access and whether the assessment requires it. The UI-oriented policies of [`AEAssessmentParticipantConfiguration`](aeassessmentparticipantconfiguration.md) (allowed menu items, graceful termination) do not apply.

> **Note**: [`AEAssessmentBinaryExecutable`](aeassessmentbinaryexecutable.md), [`AEAssessmentParticipantConfiguration`](aeassessmentparticipantconfiguration.md).

## Topics

### Initializers
- [init()](aeassessmentbinaryexecutableconfiguration/init.md)
### Instance Properties
- [var allowsNetworkAccess: Bool](aeassessmentbinaryexecutableconfiguration/allowsnetworkaccess.md)
  Whether the executable may access the network during an assessment. Defaults to `YES`.
- [var isRequired: Bool](aeassessmentbinaryexecutableconfiguration/isrequired.md)
  Whether the assessment requires this executable. Defaults to `NO`.
### Type Methods
- [class func new() -> Self](aeassessmentbinaryexecutableconfiguration/new.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/automaticassessmentconfiguration/aeassessmentbinaryexecutableconfiguration)*