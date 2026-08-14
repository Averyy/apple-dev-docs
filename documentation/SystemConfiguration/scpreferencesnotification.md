# SCPreferencesNotification

**Framework**: System Configuration  
**Kind**: struct

The type of notification (used with the [`SCPreferencesCallBack`](scpreferencescallback.md) callback).

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
struct SCPreferencesNotification
```

## Mentions

- [notificationType](1808421-notificationtype.md)

## Topics

### Constants
- [static var commit: SCPreferencesNotification](scpreferencesnotification/commit.md)
  Indicates when new preferences have been saved.
- [static var apply: SCPreferencesNotification](scpreferencesnotification/apply.md)
  Indicates when a request has been made to apply the currently saved preferences to the active system configuration.
### Initializers
- [init(rawValue: UInt32)](scpreferencesnotification/init(rawvalue:).md)
  Creates a preferences notification structure with the specified raw value.

## Relationships

### Conforms To
- [BitwiseCopyable](../swift/bitwisecopyable.md)
- [Equatable](../swift/equatable.md)
- [ExpressibleByArrayLiteral](../swift/expressiblebyarrayliteral.md)
- [OptionSet](../swift/optionset.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)
- [SetAlgebra](../swift/setalgebra.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/systemconfiguration/scpreferencesnotification)*