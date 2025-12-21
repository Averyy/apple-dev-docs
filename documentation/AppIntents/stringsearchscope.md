# StringSearchScope

**Framework**: App Intents  
**Kind**: enum

Constants that help the system understand the in-app search functionality and its searchable content.

**Availability**:
- iOS 17.2+
- iPadOS 17.2+
- Mac Catalyst ?+
- macOS 14.2+
- tvOS 17.2+
- visionOS ?+
- watchOS 10.2+

## Declaration

```swift
enum StringSearchScope
```

## Topics

### Search scopes
- [StringSearchScope.freeformVideo](stringsearchscope/freeformvideo.md)
  The app supports searching for free-form video content like videos people upload to social media platforms.
- [StringSearchScope.general](stringsearchscope/general.md)
  The app offers a general search functionality that’s exposed to the system.
- [StringSearchScope.movies](stringsearchscope/movies.md)
  The app supports searching for structured movie content.
- [StringSearchScope.tv](stringsearchscope/tv.md)
  The app supports searching for structured TV content including shows, seasons, or episodes.
### Type Aliases
- [StringSearchScope.Specification](stringsearchscope/specification.md)
- [StringSearchScope.UnwrappedType](stringsearchscope/unwrappedtype.md)
- [StringSearchScope.ValueType](stringsearchscope/valuetype.md)

## Relationships

### Conforms To
- [AppEnum](appenum.md)
- [AppValue](appvalue.md)
- [CaseDisplayRepresentable](casedisplayrepresentable.md)
- [CaseIterable](../Swift/CaseIterable.md)
- [CustomLocalizedStringResourceConvertible](../Foundation/CustomLocalizedStringResourceConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [PersistentlyIdentifiable](persistentlyidentifiable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [StaticDisplayRepresentable](staticdisplayrepresentable.md)
- [TypeDisplayRepresentable](typedisplayrepresentable.md)

## See Also

- [static var searchScopes: Self.Criteria.SearchScopes](showinappsearchresultsintent/searchscopes.md)
  Values that help the system understand the scope of an app intent that shows the results of a string-based search.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/stringsearchscope)*