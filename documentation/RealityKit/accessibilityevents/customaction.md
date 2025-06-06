# AccessibilityEvents.CustomAction

**Framework**: RealityKit  
**Kind**: struct

An accessibility event for a custom action defined in your app.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS ?+

## Declaration

```swift
struct CustomAction
```

## Topics

### Initializers
- [init(key: LocalizedStringResource, entity: Entity)](accessibilityevents/customaction/init(key:entity:).md)
### Instance Properties
- [var entity: Entity](accessibilityevents/customaction/entity.md)
  The receiver of the action.
- [var key: LocalizedStringResource](accessibilityevents/customaction/key.md)
  The localized string key identifying this action.

## Relationships

### Conforms To
- [Event](event.md)
- [Sendable](../Swift/Sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/accessibilityevents/customaction)*