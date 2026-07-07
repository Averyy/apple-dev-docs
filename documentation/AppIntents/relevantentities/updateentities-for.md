# updateEntities(_:for:)

**Framework**: App Intents  
**Kind**: method

Donates suggested entities for a single context.

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
func updateEntities(_ entities: [any AppEntity], for context: AppEntityContext) async throws
```

## Mentions

- [Donating your app’s data and actions to the system](donating-your-apps-data-and-actions-to-the-system.md)

#### Discussion

Replaces any previously donated entities associated with the given context.

> **Note**: An error if the donation fails.

## Parameters

- `entities`: The entities to donate.
- `context`: The context with which to associate the donated entities.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/relevantentities/updateentities(_:for:))*