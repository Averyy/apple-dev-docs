# SearchCriteria

**Framework**: App Intents  
**Kind**: protocol  
**Role**: Protocol

An interface for defining the criteria to use when searching your app’s content.

**Availability**:
- iOS 17.2+
- iPadOS 17.2+
- Mac Catalyst 17.2+
- macOS 14.2+
- tvOS 17.2+
- visionOS
- watchOS 10.2+

## Declaration

```swift
protocol SearchCriteria : _IntentValue, Hashable, Sendable
```

## Overview

The system uses this protocol to define the search criteria it supports. Use only the system-defined types that adopt this protocol, and don’t adopt this protocol in your own types.

## Topics

### Associated Types
- [associatedtype SearchScopes = Void](./searchcriteria/searchscopes.md)

## Relationships

### Inherits From
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
### Conforming Types
- [EntityCollectionSearchCriteria](./entitycollectionsearchcriteria.md)
- [StringSearchCriteria](./stringsearchcriteria.md)

## See Also

### Search
- [protocol ShowInAppSearchResultsIntent](./showinappsearchresultsintent.md)
  An app intent that displays a set of search results in the app’s interface.
- [struct StringSearchCriteria](./stringsearchcriteria.md)
  A type that tells your app to match its items against a provided string.
- [enum StringSearchScope](./stringsearchscope.md)
  Constants that describe the types of content your app includes in search results when the search criteria is a string.
- [struct EntityCollectionSearchCriteria](./entitycollectionsearchcriteria.md)
  Search request criteria that uses an entity collection to specify the items to retrieve.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/searchcriteria)*