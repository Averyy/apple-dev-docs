# SCPreferencesNotification

**Framework**: System Configuration  
**Kind**: struct  
**Role**: Structure

The type of notification (used with the [`SCPreferencesCallBack`](./scpreferencescallback.md) callback).

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS

## Declaration

```swift
struct SCPreferencesNotification
```

```c
enum SCPreferencesNotification : uint32_t;
```

## Mentions

- [notificationType](./api-1808421-notificationtype.md)

## Topics

### Constants
- [static var commit: SCPreferencesNotification](./scpreferencesnotification/commit.md)
  Indicates when new preferences have been saved.
- [static var apply: SCPreferencesNotification](./scpreferencesnotification/apply.md)
  Indicates when a request has been made to apply the currently saved preferences to the active system configuration.
### Initializers
- [init(rawValue: UInt32)](./scpreferencesnotification/init%28rawvalue%29.md)
  Creates a preferences notification structure with the specified raw value.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../Swift/optionset.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [SetAlgebra](../Swift/setalgebra.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/systemconfiguration/scpreferencesnotification)*