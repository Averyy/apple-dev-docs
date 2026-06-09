# Browser

**Framework**: App Intents

Make your web browser’s actions available in the Shortcuts app by adopting schemas for common browsing actions.

#### Overview

The `.browser` domain defines app schemas that provide a structured representation for common browsing actions and content. Apply schemas in the `.browser` domain to make your browser’s functionality available as actions in the Shortcuts app. Schemas in this domain don’t make your conforming types discoverable by Apple Intelligence and Siri.

> 💡 **Tip**: Xcode generates a template implementation when you type `browser_` and select a schema from the suggestions list.

For more information about app schemas, see [`App schema domains`](app-schema-domains.md).

## Topics

### Actions
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
- [AppSchema.BrowserIntent](appschema/browserintent.md)
  Identifies intent schemas in the browser domain.
### Content and parameter types
- [var bookmark: some AppSchemaEntity](appschema/browserentity/bookmark.md)
  An entity schema for a bookmark.
- [var readingListItem: some AppSchemaEntity](appschema/browserentity/readinglistitem.md)
  An entity schema for a reading list item.
- [var tab: some AppSchemaEntity](appschema/browserentity/tab.md)
  An entity schema for a tab.
- [var tabGroup: some AppSchemaEntity](appschema/browserentity/tabgroup.md)
  An entity schema for a tab group.
- [var window: some AppSchemaEntity](appschema/browserentity/window.md)
  An entity schema for a window.
- [AppSchema.BrowserEntity](appschema/browserentity.md)
  Identifies entity schemas in the browser domain.
### Types for static parameters
- [var clearHistoryTimeFrame: some AppSchemaEnum](appschema/browserenum/clearhistorytimeframe.md)
  An enum schema for a clear history time frame parameter.
- [AppSchema.BrowserEnum](appschema/browserenum.md)
  Identifies enum schemas in the browser domain.
### Deprecated schemas
- [var search: some AppSchemaIntent](appschema/browserintent/search.md)
  An intent schema that searches for the given string on the web.

## See Also

- [Books](app-schema-domain-books.md)
  Make your ebook reader’s actions available in the Shortcuts app by adopting schemas for common reading actions.
- [Journaling](app-schema-domain-journaling.md)
  Make your journaling app’s actions available in the Shortcuts app by adopting schemas for journal-entry management.
- [Presentation](app-schema-domain-presentation.md)
  Make your presentation app’s actions available in the Shortcuts app by adopting schemas for common presentation actions.
- [Reader](app-schema-domain-reader.md)
  Make your document reader’s actions available in the Shortcuts app by adopting schemas for document viewing and manipulation.
- [Spreadsheet](app-schema-domain-spreadsheet.md)
  Make your spreadsheet app’s actions available in the Shortcuts app by adopting schemas for spreadsheet management.
- [Whiteboard](app-schema-domain-whiteboard.md)
  Make your whiteboard app’s actions available in the Shortcuts app by adopting schemas for common whiteboard actions.
- [Word processor](app-schema-domain-word-processor.md)
  Make your word processor’s actions available in the Shortcuts app by adopting schemas for document editing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/app-schema-domain-browser)*