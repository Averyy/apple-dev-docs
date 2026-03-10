# openBookmark

**Framework**: App Intents  
**Kind**: property

The app intent conforms to the Assistant schema for opening a bookmarked URL.

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
var openBookmark: some AssistantSchemas.Intent { get }
```

#### Overview

Use Swift macros that generate additional properties and add protocol conformance for your app intent implementation. The following example shows an app intent that conforms to the `.browser.openBookmark` schema:

```swift
@AppIntent(schema: .browser.openBookmark)
struct OpenBookmarkIntent: OpenIntent {
    @Parameter
    var tab: TabEntity?

    @Parameter
    var target: BookmarkEntity

    func perform() async throws -> some IntentResult {
        .result()
    }
}
```

## See Also

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
- [var openURLInTab: some AssistantSchemas.Intent](assistantschemas/browserintent/openurlintab.md)
  The app intent conforms to the Assistant schema for loading a URL in a browser tab.
- [var switchTab: some AssistantSchemas.Intent](assistantschemas/browserintent/switchtab.md)
  The app intent conforms to the schema for switching to a specific tab.
- [AssistantSchemas.BrowserIntent](assistantschemas/browserintent.md)
  Assistant schema conformance for app intents that offer web browsing functionality.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/assistantschemas/browserintent/openbookmark)*