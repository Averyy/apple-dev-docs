# RelevantEntities

**Framework**: App Intents  
**Kind**: struct

A type you use to donate your app’s songs, albums, artists, and other media items to play during workouts.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
struct RelevantEntities
```

## Mentions

- [Donating your app’s data and actions to the system](donating-your-apps-data-and-actions-to-the-system.md)

#### Overview

Use the shared `RelevantEntities` object to donate songs, albums, artists, playlists, radio stations, podcasts, or other media-related content to the system. Base your donations on whatever criteria makes sense for your app. For example, you might donate songs that someone listens to frequently or donate new items that you think someone might like based on their tastes. The system uses your donations to offer suggestions for content someone can play during a workout or other scenario.

When you donate media items using this type, provide all the items at once using the `RelevantEntities/updateSuggestedEntities(_:)` method. Apps provide only one set of suggestions at a time, and those suggestions remain active until you clear them. Each time you call the `RelevantEntities/updateSuggestedEntities(_:)` method, the system replaces your app’s previous suggestions with the new set. If you don’t have any suggestions, you can specify an empty array when calling the method. If someone doesn’t launch your app, the system automatically expires your app’s suggestions after approximately four weeks.

## Topics

### Getting the shared type
- [static let shared: RelevantEntities](relevantentities/shared.md)
  The shared instance of this class.
### Donating entities
- [func updateEntities([any AppEntity], for: AppEntityContext) async throws](relevantentities/updateentities(_:for:).md)
  Donates suggested entities for a single context.
### Removing the current donations
- [func removeAllEntities() async throws](relevantentities/removeallentities.md)
  Removes all suggested entities across all contexts.
- [func removeAllEntities(for: AppEntityContext) async throws](relevantentities/removeallentities(for:).md)
  Removes all donated entities for the given context.
- [func removeEntities([any AppEntity]) async throws](relevantentities/removeentities(_:).md)
  Removes the specified entities across all contexts.
- [func removeEntities([any AppEntity], from: AppEntityContext) async throws](relevantentities/removeentities(_:from:).md)
  Removes specific entities from the given context.

## Relationships

### Conforms To
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [struct AppEntityContext](appentitycontext.md)
  The context used to scope suggested entity donations to a specific domain.
- [struct AudioContext](audiocontext.md)
  Specifies the type of audio activity to associate with a suggested entity, allowing the system to surface relevant suggestions at the right moment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/relevantentities)*