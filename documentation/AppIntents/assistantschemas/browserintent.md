# AssistantSchemas.BrowserIntent

**Framework**: App Intents  
**Kind**: protocol

Assistant schema conformance for app intents that offer web browsing functionality.

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
protocol BrowserIntent : AssistantSchemas.Model
```

## Mentions

- [Making browser actions available to Siri and Apple Intelligence](making-browser-actions-available-to-siri-and-apple-intelligence.md)

## Topics

### Instance Properties
- [var bookmarkTab: some AssistantSchemas.Intent](assistantschemas/browserintent/bookmarktab.md)
  The app intent conforms to the schema for creating a new bookmark for a browser tab.
- [var bookmarkURL: some AssistantSchemas.Intent](assistantschemas/browserintent/bookmarkurl.md)
  The app intent conforms to the schema for creating a bookmark for a URL.
- [var clearHistory: some AssistantSchemas.Intent](assistantschemas/browserintent/clearhistory.md)
  The app intent conforms to the schema for clearing the browser history.
- [var closeTabs: some AssistantSchemas.Intent](assistantschemas/browserintent/closetabs.md)
  The app intent conforms to the schema for closing a browser tab.
- [var closeWindows: some AssistantSchemas.Intent](assistantschemas/browserintent/closewindows.md)
  The app intent conforms to the schema for closing one or more browser windows.
- [var createTab: some AssistantSchemas.Intent](assistantschemas/browserintent/createtab.md)
  The app intent conforms to the schema for creating a browser tab.
- [var createWindow: some AssistantSchemas.Intent](assistantschemas/browserintent/createwindow.md)
  The app intent conforms to the schema for creating a new browser window.
- [var deleteBookmarks: some AssistantSchemas.Intent](assistantschemas/browserintent/deletebookmarks.md)
  The app intent conforms to the schema for deleting a bookmark.
- [var findOnPage: some AssistantSchemas.Intent](assistantschemas/browserintent/findonpage.md)
  The app intent conforms to the schema for finding text on a web page.
- [var openBookmark: some AssistantSchemas.Intent](assistantschemas/browserintent/openbookmark.md)
  The app intent conforms to the Assistant schema for opening a bookmarked URL.
- [var openURLInTab: some AssistantSchemas.Intent](assistantschemas/browserintent/openurlintab.md)
  The app intent conforms to the Assistant schema for loading a URL in a browser tab.
- [var search: some AssistantSchemas.Intent](assistantschemas/browserintent/search.md)
  The app intent conforms to the Assistant schema for performing a web search.
- [var switchTab: some AssistantSchemas.Intent](assistantschemas/browserintent/switchtab.md)
  The app intent conforms to the schema for switching to a specific tab.

## Relationships

### Inherits From
- [AssistantSchemas.Model](assistantschemas/model.md)
### Conforming Types
- [AssistantSchema.IntentSchema](assistantschema/intentschema.md)
- [AssistantSchemas.IntentSchema](assistantschemas/intentschema.md)

## See Also

- [Making browser actions available to Siri and Apple Intelligence](making-browser-actions-available-to-siri-and-apple-intelligence.md)
  Create app intents and entities to integrate your app’s web browsing functionality with Siri and Apple Intelligence.
- [AssistantSchemas.BrowserEntity](assistantschemas/browserentity.md)
  Assistant schema conformance for app entities that describe data for web browsing functionality.
- [AssistantSchemas.BrowserEnum](assistantschemas/browserenum.md)
  Assistant schema conformance for types you use for web browsing functionality.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/assistantschemas/browserintent)*