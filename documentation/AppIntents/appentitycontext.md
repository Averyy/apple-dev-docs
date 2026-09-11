# AppEntityContext

**Framework**: App Intents  
**Kind**: struct

The context used to scope suggested entity donations to a specific domain.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
struct AppEntityContext
```

#### Overview

Pass a `AppEntityContext` when donating or removing entities via [`RelevantEntities`](relevantentities.md) to associate suggestions with the appropriate part of the app experience.

Use extensions defined by framework overlays (such as the HealthKit overlay) to create context values for specific domains.

## Topics

### Type Methods
- [static func audio(AudioContext) -> AppEntityContext](appentitycontext/audio(_:).md)
  An audio-related context.

## Relationships

### Conforms To
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [struct RelevantEntities](relevantentities.md)
  A type you use to donate your app’s songs, albums, artists, and other media items to play during workouts.
- [struct AudioContext](audiocontext.md)
  Specifies the type of audio activity to associate with a suggested entity, allowing the system to surface relevant suggestions at the right moment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appentitycontext)*