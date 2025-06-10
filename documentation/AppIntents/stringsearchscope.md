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
### Providing descriptions
- [static var caseDisplayRepresentations: [StringSearchScope : DisplayRepresentation]](stringsearchscope/casedisplayrepresentations.md)
  A dictionary that maps each value to the visual elements that represent it.
- [static var typeDisplayRepresentation: TypeDisplayRepresentation](stringsearchscope/typedisplayrepresentation.md)
  A short, localized, human-readable name for the type.
### Creating a search scope
- [init?(rawValue: String)](stringsearchscope/init(rawvalue:).md)
  Creates a new instance with the specified raw value.
### Instance Properties
- [var rawValue: String](stringsearchscope/rawvalue-swift.property.md)
  The corresponding value of the raw type.
### Type Aliases
- [StringSearchScope.AllCases](stringsearchscope/allcases-swift.typealias.md)
  A type that can represent a collection of all values of this type.
- [StringSearchScope.RawValue](stringsearchscope/rawvalue-swift.typealias.md)
  The raw type that can be used to represent all values of the conforming type.
- [StringSearchScope.Specification](stringsearchscope/specification.md)
- [StringSearchScope.UnwrappedType](stringsearchscope/unwrappedtype.md)
- [StringSearchScope.ValueType](stringsearchscope/valuetype.md)
### Type Properties
- [static var allCases: [StringSearchScope]](stringsearchscope/allcases-swift.type.property.md)
  A collection of all values of this type.
### Default Implementations
- [AppEnum Implementations](stringsearchscope/appenum-implementations.md)
- [CaseDisplayRepresentable Implementations](stringsearchscope/casedisplayrepresentable-implementations.md)
- [Equatable Implementations](stringsearchscope/equatable-implementations.md)
- [PersistentlyIdentifiable Implementations](stringsearchscope/persistentlyidentifiable-implementations.md)
- [RawRepresentable Implementations](stringsearchscope/rawrepresentable-implementations.md)

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