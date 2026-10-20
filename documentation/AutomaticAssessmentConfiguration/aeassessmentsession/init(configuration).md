# init(configuration:)

**Framework**: Automatic Assessment Configuration  
**Kind**: init  
**Role**: Initializer

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

```objc
- (instancetype) initWithConfiguration:(AEAssessmentConfiguration *) configuration;
```

#### Discussion

After creating a new session, assign its [`delegate`](./delegate.md) property before calling the [`begin()`](./begin%28%29.md) method to start a session. Wait for the delegate to receive the [`assessmentSessionDidBegin(_:)`](../aeassessmentsessiondelegate/assessmentsessiondidbegin%28_%29.md) call before starting an assessment.

## Parameters

- `configuration`: Configuration information for the session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/automaticassessmentconfiguration/aeassessmentsession/init(configuration:))*