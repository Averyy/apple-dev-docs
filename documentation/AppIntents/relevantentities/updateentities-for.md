# updateEntities(_:for:)

**Framework**: App Intents  
**Kind**: method

Donates suggested entities for a single context.

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