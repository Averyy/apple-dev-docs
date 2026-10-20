# AccessibilityEvents.CustomAction

**Framework**: RealityKit  
**Kind**: struct  
**Role**: Structure

An accessibility event for a custom action defined in your app.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 26.0+
- visionOS

## Declaration

```swift
struct CustomAction
```

## Topics

### Initializers
- [init(key: LocalizedStringResource, entity: Entity)](./customaction/init%28key,entity%29.md)
### Instance Properties
- [var entity: Entity](./customaction/entity.md)
  The receiver of the action.
- [var key: LocalizedStringResource](./customaction/key.md)
  The localized string key identifying this action.

## Relationships

### Conforms To
- [Event](../event.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/accessibilityevents/customaction)*