# AssistantSchemas.BrowserEntity

**Framework**: App Intents  
**Kind**: protocol

Assistant schema conformance for app entities that describe data for web browsing functionality.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst ?+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
protocol BrowserEntity : AssistantSchemas.Model
```

## Mentions

- [Making browser actions available to Siri and Apple Intelligence](making-browser-actions-available-to-siri-and-apple-intelligence.md)

## Topics

### Instance Properties
- [var bookmark: some AssistantSchemas.Entity](assistantschemas/browserentity/bookmark.md)
  The app entity describes a bookmark.
- [var tab: some AssistantSchemas.Entity](assistantschemas/browserentity/tab.md)
  The app entity describes a browser tab.
- [var window: some AssistantSchemas.Entity](assistantschemas/browserentity/window.md)
  The app entity describes a browser window.

## Relationships

### Inherits From
- [AssistantSchemas.Model](assistantschemas/model.md)
### Conforming Types
- [AssistantSchema.EntitySchema](assistantschema/entityschema.md)
- [AssistantSchemas.EntitySchema](assistantschemas/entityschema.md)

## See Also

- [Making browser actions available to Siri and Apple Intelligence](making-browser-actions-available-to-siri-and-apple-intelligence.md)
  Create app intents and entities to integrate your app’s web browsing functionality with Siri and Apple Intelligence.
- [AssistantSchemas.BrowserIntent](assistantschemas/browserintent.md)
  Assistant schema conformance for app intents that offer web browsing functionality.
- [AssistantSchemas.BrowserEnum](assistantschemas/browserenum.md)
  Assistant schema conformance for types you use for web browsing functionality.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/assistantschemas/browserentity)*