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
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SetAlgebra](../Swift/SetAlgebra.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/systemconfiguration/scpreferencesnotification)*