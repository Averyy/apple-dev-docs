# configuration

**Framework**: Automatic Assessment Configuration  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic, copy, readonly) AEAssessmentConfiguration * configuration;
```

## Discussion

You configure a session when you create it with the [`init(configuration:)`](./init%28configuration%29.md) initializer. You can later change the configuration by calling the [`update(to:)`](./update%28to%29.md) method. Read the [`configuration`](./configuration.md) property to obtain the session’s current configuration.

## See Also

### Managing session configuration
- [func update(to: AEAssessmentConfiguration)](./update%28to%29.md)
  Changes the session to use the specified configuration.
- [class var supportsMultipleParticipants: Bool](./supportsmultipleparticipants.md)
  A Boolean that indicates whether the current device or platform supports a configuration with one or more participant applications.
- [class var supportsConfigurationUpdates: Bool](./supportsconfigurationupdates.md)
  A Boolean that indicates whether the current device or platform supports updating a session’s configuration after the session has begun.


---

*[View on Apple Developer](https://developer.apple.com/documentation/automaticassessmentconfiguration/aeassessmentsession/configuration)*