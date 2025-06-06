# configuration

**Framework**: Automatic Assessment Configuration  
**Kind**: property

The current configuration of the session.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+

## Declaration

```swift
@NSCopying
var configuration: AEAssessmentConfiguration { get }
```

#### Discussion

You configure a session when you create it with the [`init(configuration:)`](aeassessmentsession/init(configuration:).md) initializer. You can later change the configuration by calling the [`update(to:)`](aeassessmentsession/update(to:).md) method. Read the [`configuration`](aeassessmentsession/configuration.md) property to obtain the session’s current configuration.

## See Also

- [func update(to: AEAssessmentConfiguration)](aeassessmentsession/update(to:).md)
  Changes the session to use the specified configuration.
- [class var supportsMultipleParticipants: Bool](aeassessmentsession/supportsmultipleparticipants.md)
  A Boolean that indicates whether the current device or platform supports a configuration with one or more participant applications.
- [class var supportsConfigurationUpdates: Bool](aeassessmentsession/supportsconfigurationupdates.md)
  A Boolean that indicates whether the current device or platform supports updating a session’s configuration after the session has begun.


---

*[View on Apple Developer](https://developer.apple.com/documentation/automaticassessmentconfiguration/aeassessmentsession/configuration)*