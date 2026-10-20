# AEAssessmentBinaryExecutableConfiguration

**Framework**: Automatic Assessment Configuration  
**Kind**: class  
**Role**: Class

The configuration applied to an [`AEAssessmentBinaryExecutable`](./aeassessmentbinaryexecutable.md) participant.

**Availability**:
- Mac Catalyst 27.0+
- macOS 27.0+

## Declaration

```swift
class AEAssessmentBinaryExecutableConfiguration
```

```objc
@interface AEAssessmentBinaryExecutableConfiguration : NSObject
```

#### Overview

A non-bundled executable (such as a launchd daemon) is headless, so it supports only the subset of participant policies that apply to a process without UI: network access and whether the assessment requires it. The UI-oriented policies of [`AEAssessmentParticipantConfiguration`](./aeassessmentparticipantconfiguration.md) do not apply.

> **See Also**: [`AEAssessmentBinaryExecutable`](./aeassessmentbinaryexecutable.md), [`AEAssessmentParticipantConfiguration`](./aeassessmentparticipantconfiguration.md).

## Topics

### Initializers
- [init()](./aeassessmentbinaryexecutableconfiguration/init%28%29.md)
### Instance Properties
- [var allowsNetworkAccess: Bool](./aeassessmentbinaryexecutableconfiguration/allowsnetworkaccess.md)
  Whether the executable may access the network during an assessment. Defaults to `YES`.
- [var isRequired: Bool](./aeassessmentbinaryexecutableconfiguration/isrequired.md)
  Whether the assessment requires this executable. Defaults to `NO`.
### Type Methods
- [class func new() -> Self](./aeassessmentbinaryexecutableconfiguration/new%28%29.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/automaticassessmentconfiguration/aeassessmentbinaryexecutableconfiguration)*