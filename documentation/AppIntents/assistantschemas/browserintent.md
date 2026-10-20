# AssistantSchemas.BrowserIntent

**Framework**: App Intents  
**Kind**: protocol  
**Role**: Protocol

Assistant schema conformance for app intents that offer web browsing functionality.

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
protocol BrowserIntent : AssistantSchemas.Model
```

## Topics

### Instance Properties
- [var bookmarkTab: some AssistantSchemas.Intent](./browserintent/bookmarktab.md)
  The app intent conforms to the schema for creating a new bookmark for a browser tab.
- [var bookmarkURL: some AssistantSchemas.Intent](./browserintent/bookmarkurl.md)
  The app intent conforms to the schema for creating a bookmark for a URL.
- [var clearHistory: some AssistantSchemas.Intent](./browserintent/clearhistory.md)
  The app intent conforms to the schema for clearing the browser history.
- [var closeTabs: some AssistantSchemas.Intent](./browserintent/closetabs.md)
  The app intent conforms to the schema for closing a browser tab.
- [var closeWindows: some AssistantSchemas.Intent](./browserintent/closewindows.md)
  The app intent conforms to the schema for closing one or more browser windows.
- [var createTab: some AssistantSchemas.Intent](./browserintent/createtab.md)
  The app intent conforms to the schema for creating a browser tab.
- [var createWindow: some AssistantSchemas.Intent](./browserintent/createwindow.md)
  The app intent conforms to the schema for creating a new browser window.
- [var deleteBookmarks: some AssistantSchemas.Intent](./browserintent/deletebookmarks.md)
  The app intent conforms to the schema for deleting a bookmark.
- [var findOnPage: some AssistantSchemas.Intent](./browserintent/findonpage.md)
  The app intent conforms to the schema for finding text on a web page.
- [var openBookmark: some AssistantSchemas.Intent](./browserintent/openbookmark.md)
  The app intent conforms to the Assistant schema for opening a bookmarked URL.
- [var openURLInTab: some AssistantSchemas.Intent](./browserintent/openurlintab.md)
  The app intent conforms to the Assistant schema for loading a URL in a browser tab.
- [var search: some AssistantSchemas.Intent](./browserintent/search.md)
  The app intent conforms to the Assistant schema for performing a web search.
- [var switchTab: some AssistantSchemas.Intent](./browserintent/switchtab.md)
  The app intent conforms to the schema for switching to a specific tab.

## Relationships

### Inherits From
- [AssistantSchemas.Model](./model.md)
### Conforming Types
- [AssistantSchema.IntentSchema](../assistantschema/intentschema.md)
- [AssistantSchemas.IntentSchema](./intentschema.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/assistantschemas/browserintent)*