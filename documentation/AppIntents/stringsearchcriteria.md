# StringSearchCriteria

**Framework**: App Intents  
**Kind**: struct

A type that tells your app to match its items against a provided string.

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
struct StringSearchCriteria
```

#### Overview

Use this type in app intents that match your app’s content against a string-based value. When you define an app intent using the [`search`](appschema/systemintent/search.md) schema or the [`ShowInAppSearchResultsIntent`](showinappsearchresultsintent.md) protocol, apply this type to the [`criteria`](showinappsearchresultsintent/criteria-swift.property.md) property. When your app intent runs, the system sets that property to an instance of this structure and fills it with the search term. When you use this type in your app intent, use the accompanying [`StringSearchScope`](stringsearchscope.md) type for the [`searchScopes`](showinappsearchresultsintent/searchscopes.md) property.

## Topics

### Creating the search criteria
- [init(term: String)](stringsearchcriteria/init(term:).md)
  Initializes the type with the specified search term.
### Getting the search term
- [var term: String](stringsearchcriteria/term.md)
  The string to use when matching items in your app.
### Getting related types
- [static var defaultResolverSpecification: some ResolverSpecification](stringsearchcriteria/defaultresolverspecification.md)
- [StringSearchCriteria.Specification](stringsearchcriteria/specification.md)
- [StringSearchCriteria.UnwrappedType](stringsearchcriteria/unwrappedtype.md)
- [StringSearchCriteria.ValueType](stringsearchcriteria/valuetype.md)

## Relationships

### Conforms To
- [Copyable](../swift/copyable.md)
- [Equatable](../swift/equatable.md)
- [Escapable](../swift/escapable.md)
- [Hashable](../swift/hashable.md)
- [IntentValueConvertible](intentvalueconvertible.md)
- [IntentValueExpressing](intentvalueexpressing.md)
- [SearchCriteria](searchcriteria.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [protocol ShowInAppSearchResultsIntent](showinappsearchresultsintent.md)
  An app intent that displays a set of search results in the app’s interface.
- [enum StringSearchScope](stringsearchscope.md)
  Constants that describe the types of content your app includes in search results when the search criteria is a string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/stringsearchcriteria)*