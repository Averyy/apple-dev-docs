# ShowInAppSearchResultsIntent

**Framework**: App Intents  
**Kind**: protocol

An app intent that displays a set of search results in the app’s interface.

**Availability**:
- iOS 17.2+
- iPadOS 17.2+
- Mac Catalyst 17.2+
- macOS 14.2+
- tvOS 17.2+
- visionOS ?+
- watchOS 10.2+

## Declaration

```swift
protocol ShowInAppSearchResultsIntent : SystemIntent
```

## Mentions

- [Making app entities available in Spotlight](making-app-entities-available-in-spotlight.md)
- [Creating your first app intent](creating-your-first-app-intent.md)

#### Overview

The system uses this protocol to route search requests for your app’s entities to your app. If your app has a search interface, implement this protocol in a custom type and use it to display the entities that match the provided search criteria. If your app supports multiple entity types and displays results for each of them differently, provide separate implementations of this type for each entity.

In your custom type, specify the search criteria you support and the search scope for your app’s content. For most implementations, use the [`StringSearchCriteria`](stringsearchcriteria.md) type to match the provided string against the text found in your app’s entities. For most entity types, include the [`StringSearchScope.general`](stringsearchscope/general.md) option in the [`searchScopes`](showinappsearchresultsintent/searchscopes.md) property. If your content includes media, update the search scopes to reflect the type of content your app includes. Use your custom type’s [`perform()`](appintent/perform().md) method to run the search and display the results in your app’s search interface.

The following example shows an implementation of this protocol that uses a string-based search term to locate items. The [`perform()`](appintent/perform().md) method fetches the string value and passes it to an app-specific type responsible for performing the search and displaying the results.

```swift
struct MySearchIntent: ShowInAppSearchResultsIntent {
    static let title: LocalizedStringResource = "Search my entities."

    static let searchScopes: [StringSearchScope] = [.general]
    @Parameter var criteria: StringSearchCriteria

    @Dependency var searchManager: SearchManager    // A custom app object.

     func perform() async throws -> some IntentResult {
        let searchTerm = criteria.term       // Get the string value to match against.
        searchManager.displayResults(searchTerm)
        return .result()
    }
}
```

This app intent needs to run from your app, and not from your app extension. If you implement your app intent code in a shared framework, make sure the [`allowedExecutionTargets`](appintent/allowedexecutiontargets.md) property includes your app. The protocol also provides a default implementation of the [`supportedModes`](appintent/supportedmodes.md) property that includes the foreground runtime.

> ❗ **Important**: To support Apple Intelligence, define your custom type using the [`search`](appschema/systemintent/search.md) schema, which adds support for this protocol automatically to your type.

## Topics

### Providing the search criteria
- [var criteria: Self.Criteria](showinappsearchresultsintent/criteria-swift.property.md)
  The information to use when performing the search.
- [associatedtype Criteria : SearchCriteria](showinappsearchresultsintent/criteria-swift.associatedtype.md)
- [protocol SearchCriteria](searchcriteria.md)
  An interface for defining the criteria to use when searching your app’s content.
### Limiting the search scope
- [static var searchScopes: Self.Criteria.SearchScopes](showinappsearchresultsintent/searchscopes.md)
  The scope of the search in your app’s content.

## Relationships

### Inherits From
- [AppIntent](appintent.md)
- [PersistentlyIdentifiable](persistentlyidentifiable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)
- [SystemIntent](systemintent.md)

## See Also

- [struct StringSearchCriteria](stringsearchcriteria.md)
  A type that tells your app to match its items against a provided string.
- [enum StringSearchScope](stringsearchscope.md)
  Constants that describe the types of content your app includes in search results when the search criteria is a string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/showinappsearchresultsintent)*