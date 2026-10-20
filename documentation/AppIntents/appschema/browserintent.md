# AppSchema.BrowserIntent

**Framework**: App Intents  
**Kind**: protocol  
**Role**: Protocol

Identifies intent schemas in the browser domain.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
protocol BrowserIntent : AppSchema.Kind
```

## Topics

### Instance Properties
- [var bookmarkTab: some AppSchemaIntent](./browserintent/bookmarktab.md)
  An intent schema that creates a new bookmark for this tab.
- [var bookmarkURL: some AppSchemaIntent](./browserintent/bookmarkurl.md)
  An intent schema that creates a new bookmark for a given URL.
- [var clearHistory: some AppSchemaIntent](./browserintent/clearhistory.md)
  An intent schema that clears history, and related cookies and other website data.
- [var closeTabs: some AppSchemaIntent](./browserintent/closetabs.md)
  An intent schema that closes the selected tabs.
- [var closeWindows: some AppSchemaIntent](./browserintent/closewindows.md)
  An intent schema that closes the selected windows.
- [var createTab: some AppSchemaIntent](./browserintent/createtab.md)
  An intent schema that creates a new tab with a URL loaded, or blank if omitted.
- [var createWindow: some AppSchemaIntent](./browserintent/createwindow.md)
  An intent schema that creates a new browser window.
- [var deleteBookmarks: some AppSchemaIntent](./browserintent/deletebookmarks.md)
  An intent schema that deletes the selected bookmarks.
- [var findOnPage: some AppSchemaIntent](./browserintent/findonpage.md)
  An intent schema that finds the given text on the selected tab.
- [var openBookmark: some AppSchemaIntent](./browserintent/openbookmark.md)
  An intent schema that opens the specified bookmark.
- [var openURLInTab: some AppSchemaIntent](./browserintent/openurlintab.md)
  An intent schema that navigates a tab to the given URL.
- [var search: some AppSchemaIntent](./browserintent/search.md)
  An intent schema that searches for the given string on the web.
- [var switchTab: some AppSchemaIntent](./browserintent/switchtab.md)
  An intent schema that switches to an existing tab.

## Relationships

### Inherits From
- [AppSchema.Kind](./kind.md)
### Conforming Types
- [AppSchema.Intent](./intent.md)

## See Also

### Actions
- [var bookmarkTab: some AppSchemaIntent](./browserintent/bookmarktab.md)
  An intent schema that creates a new bookmark for this tab.
- [var bookmarkURL: some AppSchemaIntent](./browserintent/bookmarkurl.md)
  An intent schema that creates a new bookmark for a given URL.
- [var clearHistory: some AppSchemaIntent](./browserintent/clearhistory.md)
  An intent schema that clears history, and related cookies and other website data.
- [var closeTabs: some AppSchemaIntent](./browserintent/closetabs.md)
  An intent schema that closes the selected tabs.
- [var closeWindows: some AppSchemaIntent](./browserintent/closewindows.md)
  An intent schema that closes the selected windows.
- [var createTab: some AppSchemaIntent](./browserintent/createtab.md)
  An intent schema that creates a new tab with a URL loaded, or blank if omitted.
- [var createWindow: some AppSchemaIntent](./browserintent/createwindow.md)
  An intent schema that creates a new browser window.
- [var deleteBookmarks: some AppSchemaIntent](./browserintent/deletebookmarks.md)
  An intent schema that deletes the selected bookmarks.
- [var findOnPage: some AppSchemaIntent](./browserintent/findonpage.md)
  An intent schema that finds the given text on the selected tab.
- [var openBookmark: some AppSchemaIntent](./browserintent/openbookmark.md)
  An intent schema that opens the specified bookmark.
- [var openURLInTab: some AppSchemaIntent](./browserintent/openurlintab.md)
  An intent schema that navigates a tab to the given URL.
- [var switchTab: some AppSchemaIntent](./browserintent/switchtab.md)
  An intent schema that switches to an existing tab.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appschema/browserintent)*