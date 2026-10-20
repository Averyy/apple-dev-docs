# AssistantSchemas.BrowserEntity

**Framework**: App Intents  
**Kind**: protocol  
**Role**: Protocol

Assistant schema conformance for app entities that describe data for web browsing functionality.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
protocol BrowserEntity : AssistantSchemas.Model
```

## Topics

### Instance Properties
- [var bookmark: some AssistantSchemas.Entity](./browserentity/bookmark.md)
  The app entity describes a bookmark.
- [var tab: some AssistantSchemas.Entity](./browserentity/tab.md)
  The app entity describes a browser tab.
- [var window: some AssistantSchemas.Entity](./browserentity/window.md)
  The app entity describes a browser window.

## Relationships

### Inherits From
- [AssistantSchemas.Model](./model.md)
### Conforming Types
- [AssistantSchema.EntitySchema](../assistantschema/entityschema.md)
- [AssistantSchemas.EntitySchema](./entityschema.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/assistantschemas/browserentity)*