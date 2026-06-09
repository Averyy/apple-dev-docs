# AppSchema.BrowserIntent

**Framework**: App Intents  
**Kind**: protocol

Identifies intent schemas in the browser domain.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst ?+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
protocol BrowserIntent : AppSchema.Kind
```

## Topics

### Instance Properties
- [var bookmarkTab: some AppSchemaIntent](appschema/browserintent/bookmarktab.md)
  An intent schema that creates a new bookmark for this tab.
- [var bookmarkURL: some AppSchemaIntent](appschema/browserintent/bookmarkurl.md)
  An intent schema that creates a new bookmark for a given URL.
- [var clearHistory: some AppSchemaIntent](appschema/browserintent/clearhistory.md)
  An intent schema that clears history, and related cookies and other website data.
- [var closeTabs: some AppSchemaIntent](appschema/browserintent/closetabs.md)
  An intent schema that closes the selected tabs.
- [var closeWindows: some AppSchemaIntent](appschema/browserintent/closewindows.md)
  An intent schema that closes the selected windows.
- [var createTab: some AppSchemaIntent](appschema/browserintent/createtab.md)
  An intent schema that creates a new tab with a URL loaded, or blank if omitted.
- [var createWindow: some AppSchemaIntent](appschema/browserintent/createwindow.md)
  An intent schema that creates a new browser window.
- [var deleteBookmarks: some AppSchemaIntent](appschema/browserintent/deletebookmarks.md)
  An intent schema that deletes the selected bookmarks.
- [var findOnPage: some AppSchemaIntent](appschema/browserintent/findonpage.md)
  An intent schema that finds the given text on the selected tab.
- [var openBookmark: some AppSchemaIntent](appschema/browserintent/openbookmark.md)
  An intent schema that opens the specified bookmark.
- [var openURLInTab: some AppSchemaIntent](appschema/browserintent/openurlintab.md)
  An intent schema that navigates a tab to the given URL.
- [var search: some AppSchemaIntent](appschema/browserintent/search.md)
  An intent schema that searches for the given string on the web.
- [var switchTab: some AppSchemaIntent](appschema/browserintent/switchtab.md)
  An intent schema that switches to an existing tab.

## Relationships

### Inherits From
- [AppSchema.Kind](appschema/kind.md)
### Conforming Types
- [AppSchema.Intent](appschema/intent.md)

## See Also

- [var bookmarkTab: some AppSchemaIntent](appschema/browserintent/bookmarktab.md)
  An intent schema that creates a new bookmark for this tab.
- [var bookmarkURL: some AppSchemaIntent](appschema/browserintent/bookmarkurl.md)
  An intent schema that creates a new bookmark for a given URL.
- [var clearHistory: some AppSchemaIntent](appschema/browserintent/clearhistory.md)
  An intent schema that clears history, and related cookies and other website data.
- [var closeTabs: some AppSchemaIntent](appschema/browserintent/closetabs.md)
  An intent schema that closes the selected tabs.
- [var closeWindows: some AppSchemaIntent](appschema/browserintent/closewindows.md)
  An intent schema that closes the selected windows.
- [var createTab: some AppSchemaIntent](appschema/browserintent/createtab.md)
  An intent schema that creates a new tab with a URL loaded, or blank if omitted.
- [var createWindow: some AppSchemaIntent](appschema/browserintent/createwindow.md)
  An intent schema that creates a new browser window.
- [var deleteBookmarks: some AppSchemaIntent](appschema/browserintent/deletebookmarks.md)
  An intent schema that deletes the selected bookmarks.
- [var findOnPage: some AppSchemaIntent](appschema/browserintent/findonpage.md)
  An intent schema that finds the given text on the selected tab.
- [var openBookmark: some AppSchemaIntent](appschema/browserintent/openbookmark.md)
  An intent schema that opens the specified bookmark.
- [var openURLInTab: some AppSchemaIntent](appschema/browserintent/openurlintab.md)
  An intent schema that navigates a tab to the given URL.
- [var switchTab: some AppSchemaIntent](appschema/browserintent/switchtab.md)
  An intent schema that switches to an existing tab.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appschema/browserintent)*