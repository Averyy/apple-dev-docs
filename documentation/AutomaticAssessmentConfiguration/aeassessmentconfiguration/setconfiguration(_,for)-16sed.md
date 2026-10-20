# setConfiguration(_:for:)

**Framework**: Automatic Assessment Configuration  
**Kind**: method  
**Role**: Instance Method

Adds an executable participant to the list of participants available during an assessment.

**Availability**:
- Mac Catalyst 27.0+
- macOS 27.0+

## Declaration

```swift
func setConfiguration(_ configuration: AEAssessmentBinaryExecutableConfiguration, for binaryExecutable: AEAssessmentBinaryExecutable)
```

```objc
- (void) setConfiguration:(AEAssessmentBinaryExecutableConfiguration *) configuration forBinaryExecutable:(AEAssessmentBinaryExecutable *) binaryExecutable;
```

#### Discussion

Ignores an executable whose [`binaryExecutableURL`](../aeassessmentbinaryexecutable/binaryexecutableurl.md) isn’t a file URL.

> **See Also**: [`AEAssessmentBinaryExecutable`](../aeassessmentbinaryexecutable.md)

## Parameters

- `configuration`: The configuration of the executable participant.
- `binaryExecutable`: The executable that you want to configure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/automaticassessmentconfiguration/aeassessmentconfiguration/setconfiguration(_:for:)-16sed)*