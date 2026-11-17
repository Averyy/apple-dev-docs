# search

**Framework**: App Intents  
**Kind**: property  
**Role**: Instance Property

An intent schema that navigates to search results.

**Availability**:
- iOS 18.0+ - Deprecated in 27.0
- iPadOS 18.0+ - Deprecated in 27.0
- Mac Catalyst 18.0+ - Deprecated in 27.0
- macOS 15.0+ - Deprecated in 27.0
- visionOS 2.0+ - Deprecated in 27.0

> **Deprecated**: Use .system.searchInApp instead

## Declaration

```swift
var search: some AppSchemaIntent { get }
```

## Discussion

To make your app’s actions available to Apple Intelligence, conform your [`AppIntent`](../../appintent.md) to a schema that describes your action to the system. If your app’s functionality aligns with the `system` domain and one of your app’s actions matches the `search` schema, you can generate the properties and protocol conformance the schema requires for your intent implementation with the `@AppIntent(schema: .system.search)` Swift macro. To make your app work with Siri, see [Apple Intelligence and Siri AI](../../apple-intelligence-and-siri-ai.md).

The following example shows an intent that conforms to the `search` schema. You can create a type that conforms to the schema by adding the `@AppIntent` macro above the type’s declaration. Xcode inserts a template type into your code for you, which includes the macro, when you type the first few characters of `system_search` and select it from the code-completion suggestions:

```swift
@AppIntent(schema: .system.search)
struct SystemShowInAppSearchResultsIntent: ShowInAppSearchResultsIntent {
    /// The content categories this action covers, such as general results.
    static var searchScopes: [StringSearchScope] = [.general]

    /// Search criteria used when searching in app.
    var criteria: StringSearchCriteria

    func perform() async throws -> some IntentResult {
        <#code#>
    }
}
```

The schema supports the following system experiences:

- Siri
- Shortcuts

For more information about the App Intents framework and the experiences it supports, see [Getting started with the App Intents framework](../../getting-started-with-the-app-intents-framework.md).

## Parameters for the search intent

Each parameter in the code listing above plays a specific role when your app performs this action. The following table describes what each parameter represents and any behavior to account for when you set it.

| Parameter | Type | Origin | Discussion |
| --- | --- | --- | --- |
| `criteria` | `StringSearchCriteria` | App Intents | Search criteria used when searching in app. |


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appschema/systemintent/search)*