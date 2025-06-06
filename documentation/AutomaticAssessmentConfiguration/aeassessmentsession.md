# AEAssessmentSession

**Framework**: Automatic Assessment Configuration  
**Kind**: class

A session that your app uses to protect an assessment.

**Availability**:
- iOS 13.4+
- iPadOS 13.4+
- Mac Catalyst 14.0+
- macOS 10.15.4+

## Declaration

```swift
class AEAssessmentSession
```

#### Overview

Use the [`AEAssessmentSession`](aeassessmentsession.md) class to manage an assessment session. The system allows only one active session at a time across all processes. The first session to run gets exclusive access to the system; subsequent session attempts fail until the first session ends.

To create an assessment session, pass a new [`AEAssessmentConfiguration`](aeassessmentconfiguration.md) instance to the [`init(configuration:)`](aeassessmentsession/init(configuration:).md) method. Then, provide the session with a delegate that conforms to the [`AEAssessmentSessionDelegate`](aeassessmentsessiondelegate.md) protocol:

You can indicate exceptions to the restrictions imposed by an assessment session by setting the properties of the configuration instance, or you can use the default restrictions as shown above. The session tells its delegate about state changes during its life cycle. To start a session, call the session’s [`begin()`](aeassessmentsession/begin().md) method:

The method returns immediately, and the session starts disabling system features. After achieving the desired state, the session calls its delegate’s [`assessmentSessionDidBegin(_:)`](aeassessmentsessiondelegate/assessmentsessiondidbegin(_:).md) method. Only after receiving this callback is it safe to begin your assessment. Be sure to keep a strong reference to the session as long as you want it to remain active. If the system deallocates an active session, the session automatically ends.

> ❗ **Important**:  Prior to macOS 12.1, a DNS lookup that your app initiates during a session might fail. Be sure your app resolves all required domain names before beginning a session so that the system can cache the results. You can do this by using [`URLSession`](https://developer.apple.com/documentation/Foundation/URLSession) to send a `HEAD` request to each domain name that your app needs to access.

 Prior to macOS 12.1, a DNS lookup that your app initiates during a session might fail. Be sure your app resolves all required domain names before beginning a session so that the system can cache the results. You can do this by using [`URLSession`](https://developer.apple.com/documentation/Foundation/URLSession) to send a `HEAD` request to each domain name that your app needs to access.

After completing an assessment and hiding all sensitive information, call the session’s [`end()`](aeassessmentsession/end().md) method:

After making the call, wait for the session to call its delegate’s [`assessmentSessionDidEnd(_:)`](aeassessmentsessiondelegate/assessmentsessiondidend(_:).md) method before reporting assessment completion to the user.

During assessment, the session’s delegate might receive an [`assessmentSession(_:wasInterruptedWithError:)`](aeassessmentsessiondelegate/assessmentsession(_:wasinterruptedwitherror:).md) callback to indicate a failure. If this happens, immediately stop the assessment, hide all sensitive content, and end the session. Because it might take time for your app to finalize the assessment, the session relies on your app to call the session’s [`end()`](aeassessmentsession/end().md) method:

## Topics

### Creating a session
- [init(configuration: AEAssessmentConfiguration)](aeassessmentsession/init(configuration:).md)
  Creates a new assessment session.
### Managing session configuration
- [func update(to: AEAssessmentConfiguration)](aeassessmentsession/update(to:).md)
  Changes the session to use the specified configuration.
- [var configuration: AEAssessmentConfiguration](aeassessmentsession/configuration.md)
  The current configuration of the session.
- [class var supportsMultipleParticipants: Bool](aeassessmentsession/supportsmultipleparticipants.md)
  A Boolean that indicates whether the current device or platform supports a configuration with one or more participant applications.
- [class var supportsConfigurationUpdates: Bool](aeassessmentsession/supportsconfigurationupdates.md)
  A Boolean that indicates whether the current device or platform supports updating a session’s configuration after the session has begun.
### Responding to session updates
- [var delegate: (any AEAssessmentSessionDelegate)?](aeassessmentsession/delegate.md)
  A delegate to which the session provides state change updates.
- [protocol AEAssessmentSessionDelegate](aeassessmentsessiondelegate.md)
  An interface that the session uses to provide information about session state changes to a delegate.
### Starting and stopping a session
- [func begin()](aeassessmentsession/begin.md)
  Starts an assessment session.
- [func end()](aeassessmentsession/end.md)
  Ends an assessment session.
- [var isActive: Bool](aeassessmentsession/isactive.md)
  A Boolean that indicates whether an assessment session is running.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [Preparing an educational assessment app for distribution](preparing-an-educational-assessment-app-for-distribution.md)
  Ensure your app maintains academic integrity by reviewing assessment practices and managing system capabilities.
- [Build an Educational Assessment App](build-an-educational-assessment-app.md)
  Ensure the academic integrity of your assessment app by using Automatic Assessment Configuration.
- [class AEAssessmentConfiguration](aeassessmentconfiguration.md)
  Configuration information for an assessment session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/automaticassessmentconfiguration/aeassessmentsession)*