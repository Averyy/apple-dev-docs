# VideoCategory

**Framework**: App Intents  
**Kind**: enum

**Availability**:
- iOS 17.2+
- iPadOS 17.2+
- Mac Catalyst 17.2+
- macOS 14.2+
- tvOS 17.2+
- visionOS 1.0+

## Declaration

```swift
enum VideoCategory
```

## Topics

### Enumeration Cases
- [VideoCategory.freeform](videocategory/freeform.md)
  The app supports searching for freeform video content like what may uploaded to social media platforms. This should not be used in cases of highly structured content like movies and episodic tv shows.
- [VideoCategory.movies](videocategory/movies.md)
  The app supports searching for structured movie content.
- [VideoCategory.tv](videocategory/tv.md)
  The app supports searching for structured tv content including shows, seasons, or episodes.
### Initializers
- [init?(rawValue: String)](videocategory/init(rawvalue:).md)
  Creates a new instance with the specified raw value.
### Instance Properties
- [var rawValue: String](videocategory/rawvalue-swift.property.md)
  The corresponding value of the raw type.
### Type Aliases
- [VideoCategory.AllCases](videocategory/allcases-swift.typealias.md)
  A type that can represent a collection of all values of this type.
- [VideoCategory.RawValue](videocategory/rawvalue-swift.typealias.md)
  The raw type that can be used to represent all values of the conforming type.
- [VideoCategory.Specification](videocategory/specification.md)
- [VideoCategory.UnwrappedType](videocategory/unwrappedtype.md)
- [VideoCategory.ValueType](videocategory/valuetype.md)
### Type Properties
- [static var allCases: [VideoCategory]](videocategory/allcases-swift.type.property.md)
  A collection of all values of this type.
- [static var caseDisplayRepresentations: [VideoCategory : DisplayRepresentation]](videocategory/casedisplayrepresentations.md)
  A dictionary that maps each value to the visual elements that represent it.
- [static var typeDisplayRepresentation: TypeDisplayRepresentation](videocategory/typedisplayrepresentation.md)
  A short, localized, human-readable name for the type.
### Default Implementations
- [AppEnum Implementations](videocategory/appenum-implementations.md)
- [CaseDisplayRepresentable Implementations](videocategory/casedisplayrepresentable-implementations.md)
- [Equatable Implementations](videocategory/equatable-implementations.md)
- [PersistentlyIdentifiable Implementations](videocategory/persistentlyidentifiable-implementations.md)
- [RawRepresentable Implementations](videocategory/rawrepresentable-implementations.md)

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
- [StaticDisplayRepresentable](staticdisplayrepresentable.md)
- [TypeDisplayRepresentable](typedisplayrepresentable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/videocategory)*