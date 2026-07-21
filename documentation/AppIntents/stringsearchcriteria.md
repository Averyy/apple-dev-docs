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

### Initializers
- [init(term: String)](stringsearchcriteria/init(term:).md)
  Initializes the type with the specified search term.
### Instance Properties
- [var term: String](stringsearchcriteria/term.md)
  The string to use when matching items in your app.
### Type Aliases
- [StringSearchCriteria.Specification](stringsearchcriteria/specification.md)
- [StringSearchCriteria.UnwrappedType](stringsearchcriteria/unwrappedtype.md)
- [StringSearchCriteria.ValueType](stringsearchcriteria/valuetype.md)
### Type Properties
- [static var defaultResolverSpecification: some ResolverSpecification](stringsearchcriteria/defaultresolverspecification.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Escapable](../Swift/Escapable.md)
- [Hashable](../Swift/Hashable.md)
- [IntentValueConvertible](intentvalueconvertible.md)
- [IntentValueExpressing](intentvalueexpressing.md)
- [SearchCriteria](searchcriteria.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var criteria: Self.Criteria](showinappsearchresultsintent/criteria-swift.property.md)
  The information to use when performing the search.
- [protocol SearchCriteria](searchcriteria.md)
  An interface for defining the criteria to use when searching your app’s content.
- [associatedtype Criteria : SearchCriteria](showinappsearchresultsintent/criteria-swift.associatedtype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/stringsearchcriteria)*