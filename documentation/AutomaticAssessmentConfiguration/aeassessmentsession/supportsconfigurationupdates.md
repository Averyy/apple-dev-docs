# supportsConfigurationUpdates

**Framework**: Automatic Assessment Configuration  
**Kind**: property  
**Role**: Type Property

A Boolean that indicates whether the current device or platform supports updating a session’s configuration after the session has begun.

**Availability**:
- iOS 17.5+
- iPadOS 17.5+
- Mac Catalyst 17.5+
- macOS 14.5+

## Declaration

```swift
class var supportsConfigurationUpdates: Bool { get }
```

```objc
@property (class, assign, readonly) BOOL supportsConfigurationUpdates;
```

## See Also

### Managing session configuration
- [func update(to: AEAssessmentConfiguration)](./update%28to%29.md)
  Changes the session to use the specified configuration.
- [var configuration: AEAssessmentConfiguration](./configuration.md)
  The current configuration of the session.
- [class var supportsMultipleParticipants: Bool](./supportsmultipleparticipants.md)
  A Boolean that indicates whether the current device or platform supports a configuration with one or more participant applications.


---

*[View on Apple Developer](https://developer.apple.com/documentation/automaticassessmentconfiguration/aeassessmentsession/supportsconfigurationupdates)*