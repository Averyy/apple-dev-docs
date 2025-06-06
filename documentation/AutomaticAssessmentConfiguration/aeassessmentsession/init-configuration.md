# init(configuration:)

**Framework**: Automatic Assessment Configuration  
**Kind**: init

Creates a new assessment session.

**Availability**:
- iOS 13.4+
- iPadOS 13.4+
- Mac Catalyst 14.0+
- macOS 10.15.4+

## Declaration

```swift
init(configuration: AEAssessmentConfiguration)
```

#### Discussion

After creating a new session, assign its [`delegate`](aeassessmentsession/delegate.md) property before calling the [`begin()`](aeassessmentsession/begin().md) method to start a session. Wait for the delegate to receive the [`assessmentSessionDidBegin(_:)`](aeassessmentsessiondelegate/assessmentsessiondidbegin(_:).md) call before starting an assessment.

## Parameters

- `configuration`: Configuration information for the session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/automaticassessmentconfiguration/aeassessmentsession/init(configuration:))*