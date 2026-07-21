# ShowInAppSearchResultsIntent

**Framework**: App Intents  
**Kind**: protocol

An app intent that takes a person to search results for a specified search term.

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

Provide a [`SearchCriteria`](searchcriteria.md) to specify a search term for this intent. You can provide several `ShowInAppSearchResultsIntent` implementations where each intent conforms to a different search criteria.

## Topics

### Scoping the search
- [static var searchScopes: Self.Criteria.SearchScopes](showinappsearchresultsintent/searchscopes.md)
  The scope of the search in your app’s content.
- [enum StringSearchScope](stringsearchscope.md)
  Constants that help the system understand the in-app search functionality and its searchable content.
### Defining the search criteria
- [var criteria: Self.Criteria](showinappsearchresultsintent/criteria-swift.property.md)
  The information to use when performing the search.
- [protocol SearchCriteria](searchcriteria.md)
  An interface for defining the criteria to use when searching your app’s content.
- [struct StringSearchCriteria](stringsearchcriteria.md)
  A type that tells your app to match its items against a provided string.
- [associatedtype Criteria : SearchCriteria](showinappsearchresultsintent/criteria-swift.associatedtype.md)

## Relationships

### Inherits From
- [AppIntent](appintent.md)
- [PersistentlyIdentifiable](persistentlyidentifiable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [SystemIntent](systemintent.md)

## See Also

- [protocol OpenIntent](openintent.md)
  Open the associated item.
- [struct OpenURLIntent](openurlintent.md)
  An intent that opens a universal link.
- [protocol SetValueIntent](setvalueintent.md)
  An intent that contains a value which can be set.
- [protocol DeleteIntent](deleteintent.md)
  Delete the associated entity(s).
- [protocol DeprecatedAppIntent](deprecatedappintent.md)
  An app intent that marks an action as deprecated and informs people which action to use instead.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/showinappsearchresultsintent)*