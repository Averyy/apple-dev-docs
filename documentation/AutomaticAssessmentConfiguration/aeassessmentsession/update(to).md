# update(to:)

**Framework**: Automatic Assessment Configuration  
**Kind**: method  
**Role**: Instance Method

Changes the session to use the specified configuration.

**Availability**:
- iOS 17.5+
- iPadOS 17.5+
- Mac Catalyst 15.0+
- macOS 12.0+

## Declaration

```swift
func update(to configuration: AEAssessmentConfiguration)
```

```objc
- (void) updateToConfiguration:(AEAssessmentConfiguration *) configuration;
```

#### Discussion

After you call this method, the session tries to apply the new configuration and then calls its delegate’s [`assessmentSessionDidUpdate(_:)`](../aeassessmentsessiondelegate/assessmentsessiondidupdate%28_%29.md) method to indicate success, or the delegate’s [`assessmentSession(_:failedToUpdateTo:error:)`](../aeassessmentsessiondelegate/assessmentsession%28_,failedtoupdateto,error%29.md) method to indicate failure. Wait to receive one of these callbacks before proceeding with an assessment, and be sure to handle the failure case.

## Parameters

- `configuration`: A new configuration to use for the session.

## See Also

### Managing session configuration
- [var configuration: AEAssessmentConfiguration](./configuration.md)
  The current configuration of the session.
- [class var supportsMultipleParticipants: Bool](./supportsmultipleparticipants.md)
  A Boolean that indicates whether the current device or platform supports a configuration with one or more participant applications.
- [class var supportsConfigurationUpdates: Bool](./supportsconfigurationupdates.md)
  A Boolean that indicates whether the current device or platform supports updating a session’s configuration after the session has begun.


---

*[View on Apple Developer](https://developer.apple.com/documentation/automaticassessmentconfiguration/aeassessmentsession/update(to:))*