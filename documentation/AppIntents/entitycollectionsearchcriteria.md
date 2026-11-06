# EntityCollectionSearchCriteria

**Framework**: App Intents  
**Kind**: struct  
**Role**: Structure

Search request criteria that uses an entity collection to specify the items to retrieve.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
struct EntityCollectionSearchCriteria<Entity> where Entity : AppEntity
```

## Overview

If you implement a [`ShowInAppSearchResultsIntent`](./showinappsearchresultsintent.md) type to display your app’s search results interface, use this type to receive the search criteria as a collection of entity identifiers. When the system needs to display search results in your app, it creates the [`ShowInAppSearchResultsIntent`](./showinappsearchresultsintent.md) to ask your app to display them. The system can use this type to specify the results as a set of entity identifiers for your app to display and place them in the `ShowInAppSearchResultsType/criteria` property of your app intent. Use the information in this type to retrieve and display the entities.

Typically, the system creates an instance of this type and delivers it to your [`ShowInAppSearchResultsIntent`](./showinappsearchresultsintent.md). If you donate the same app intent after someone performs a search directly from your app, you can use this type to specify the entities your interface displayed.

## Topics

### Initializers
- [init(entities: EntityCollection<Entity>)](./entitycollectionsearchcriteria/init%28entities%29.md)
  Creates a new search criteria type with the specified entity collection.
### Instance Properties
- [var entities: EntityCollection<Entity>](./entitycollectionsearchcriteria/entities.md)
  The entity collection with the search results to display.
### Type Aliases
- [EntityCollectionSearchCriteria.Specification](./entitycollectionsearchcriteria/specification.md)
- [EntityCollectionSearchCriteria.UnwrappedType](./entitycollectionsearchcriteria/unwrappedtype.md)
- [EntityCollectionSearchCriteria.ValueType](./entitycollectionsearchcriteria/valuetype.md)
### Type Properties
- [static var defaultResolverSpecification: some ResolverSpecification](./entitycollectionsearchcriteria/defaultresolverspecification.md)

## Relationships

### Conforms To
- [Copyable](../Swift/copyable.md)
- [Equatable](../Swift/equatable.md)
- [Escapable](../Swift/escapable.md)
- [Hashable](../Swift/hashable.md)
- [IntentValueConvertible](./intentvalueconvertible.md)
- [IntentValueExpressing](./intentvalueexpressing.md)
- [SearchCriteria](./searchcriteria.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Search
- [protocol ShowInAppSearchResultsIntent](./showinappsearchresultsintent.md)
  An app intent that displays a set of search results in the app’s interface.
- [struct StringSearchCriteria](./stringsearchcriteria.md)
  A type that tells your app to match its items against a provided string.
- [enum StringSearchScope](./stringsearchscope.md)
  Constants that describe the types of content your app includes in search results when the search criteria is a string.
- [protocol SearchCriteria](./searchcriteria.md)
  An interface for defining the criteria to use when searching your app’s content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/entitycollectionsearchcriteria)*