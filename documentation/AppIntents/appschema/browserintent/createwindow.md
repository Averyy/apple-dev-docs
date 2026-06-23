# createWindow

**Framework**: App Intents  
**Kind**: property

An intent schema that creates a new browser window.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst ?+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
var createWindow: some AppSchemaIntent { get }
```

#### Discussion

To make your app’s actions available to Apple Intelligence, conform your [`AppIntent`](appintent.md) to a schema that describes your action to the system. If your app’s functionality aligns with the `browser` domain and one of your app’s actions matches the `createWindow` schema, you can generate the properties and protocol conformance the schema requires for your intent implementation with the `@AppIntent( .browser.createWindow)` Swift macro. To make your app work with Siri, see [`Apple Intelligence and Siri AI`](apple-intelligence-and-siri-ai.md).

The following example shows an intent that conforms to the `createWindow` schema:

```swift
@AppIntent(schema: .browser.createWindow)
struct CreateWindowIntent {
    var isPrivate: Bool

    func perform() async throws -> some ReturnsValue<<#WindowEntity#>> {
        <#code#>
    }
}
```

The schema supports the following system experiences:

- Shortcuts

For more information about the App Intents framework and the experiences it supports, see [`Getting started with the App Intents framework`](getting-started-with-the-app-intents-framework.md).

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appschema/browserintent/createwindow)*