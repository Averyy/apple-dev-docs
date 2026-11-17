# bookmarkTab

**Framework**: App Intents  
**Kind**: property  
**Role**: Instance Property

An intent schema that creates a new bookmark for this tab.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
var bookmarkTab: some AppSchemaIntent { get }
```

## Discussion

To make your app’s actions available to Apple Intelligence, conform your [`AppIntent`](../../appintent.md) to a schema that describes your action to the system. If your app’s functionality aligns with the `browser` domain and one of your app’s actions matches the `bookmarkTab` schema, you can generate the properties and protocol conformance the schema requires for your intent implementation with the `@AppIntent(schema: .browser.bookmarkTab)` Swift macro.

The following example shows an intent that conforms to the `bookmarkTab` schema. You can create a type that conforms to the schema by adding the `@AppIntent` macro above the type’s declaration. Xcode inserts a template type into your code for you, which includes the macro, when you type the first few characters of `browser_bookmarkTab` and select it from the code-completion suggestions:

```swift
@AppIntent(schema: .browser.bookmarkTab)
struct BookmarkTabIntent {
    /// Tab to bookmark.
    var tab: <#TabEntity#>

    /// Bookmark name.
    var name: String?

    func perform() async throws -> some ReturnsValue<<#BookmarkEntity#>> {
        <#code#>
    }
}
```

The schema supports the following system experiences:

- Shortcuts

For more information about the App Intents framework and the experiences it supports, see [Getting started with the App Intents framework](../../getting-started-with-the-app-intents-framework.md).

## Parameters for the bookmark-tab intent

Each parameter in the code listing above plays a specific role when your app performs this action. The following table describes what each parameter represents and any behavior to account for when you set it.

| Parameter | Type | Origin | Discussion |
| --- | --- | --- | --- |
| `tab` | `@AppEntity(schema: .browser.tab)` | Your app | Tab to bookmark. `TabEntity` is a placeholder name for a type that conforms to the [`tab`](../browserentity/tab.md) entity schema, which your app defines and implements. |
| `name` | `String?` | Swift | Bookmark name. |

## See Also

### Actions
- [var bookmarkURL: some AppSchemaIntent](./bookmarkurl.md)
  An intent schema that creates a new bookmark for a given URL.
- [var clearHistory: some AppSchemaIntent](./clearhistory.md)
  An intent schema that clears history, and related cookies and other website data.
- [var closeTabs: some AppSchemaIntent](./closetabs.md)
  An intent schema that closes the selected tabs.
- [var closeWindows: some AppSchemaIntent](./closewindows.md)
  An intent schema that closes the selected windows.
- [var createTab: some AppSchemaIntent](./createtab.md)
  An intent schema that creates a new tab with a URL loaded, or blank if omitted.
- [var createWindow: some AppSchemaIntent](./createwindow.md)
  An intent schema that creates a new browser window.
- [var deleteBookmarks: some AppSchemaIntent](./deletebookmarks.md)
  An intent schema that deletes the selected bookmarks.
- [var findOnPage: some AppSchemaIntent](./findonpage.md)
  An intent schema that finds the given text on the selected tab.
- [var openBookmark: some AppSchemaIntent](./openbookmark.md)
  An intent schema that opens the specified bookmark.
- [var openURLInTab: some AppSchemaIntent](./openurlintab.md)
  An intent schema that navigates a tab to the given URL.
- [var switchTab: some AppSchemaIntent](./switchtab.md)
  An intent schema that switches to an existing tab.
- [AppSchema.BrowserIntent](../browserintent.md)
  Identifies intent schemas in the browser domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appschema/browserintent/bookmarktab)*