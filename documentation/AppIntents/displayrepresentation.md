# DisplayRepresentation

**Framework**: App Intents  
**Kind**: struct

A type that describes the user interface presentation of a custom type.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst ?+
- macOS 13.0+
- tvOS 16.0+
- visionOS ?+
- watchOS 9.0+

## Declaration

```swift
struct DisplayRepresentation
```

## Mentions

- [Integrating custom data types into your intents](integrating-custom-types-into-your-intents.md)
- [Making app entities available in Spotlight](making-app-entities-available-in-spotlight.md)

## Topics

### Creating a representation
- [init(title: LocalizedStringResource, subtitle: LocalizedStringResource?, image: DisplayRepresentation.Image?)](displayrepresentation/init(title:subtitle:image:).md)
### Displaying the content
- [var title: LocalizedStringResource](displayrepresentation/title.md)
- [var subtitle: LocalizedStringResource?](displayrepresentation/subtitle.md)
- [var image: DisplayRepresentation.Image?](displayrepresentation/image-swift.property.md)
- [DisplayRepresentation.Image](displayrepresentation/image-swift.struct.md)
### Initializers
- [init(title: LocalizedStringResource, subtitle: LocalizedStringResource?, image: DisplayRepresentation.Image?, synonyms: [LocalizedStringResource])](displayrepresentation/init(title:subtitle:image:synonyms:).md)
### Instance Properties
- [var synonyms: [LocalizedStringResource]](displayrepresentation/synonyms.md)
  A list of localized phrases that are synonyms of this particular display representation

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByExtendedGraphemeClusterLiteral](../Swift/ExpressibleByExtendedGraphemeClusterLiteral.md)
- [ExpressibleByStringLiteral](../Swift/ExpressibleByStringLiteral.md)
- [ExpressibleByUnicodeScalarLiteral](../Swift/ExpressibleByUnicodeScalarLiteral.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [protocol DisplayRepresentable](displayrepresentable.md)
  An interface for providing a dynamic visual representation of a specific type and instances of that type.
- [protocol InstanceDisplayRepresentable](instancedisplayrepresentable.md)
  An interface for providing the visual representation for an instance of a specific type.
- [protocol TypeDisplayRepresentable](typedisplayrepresentable.md)
  An interface for providing the visual representation of a specific type.
- [struct TypeDisplayRepresentation](typedisplayrepresentation.md)
  A type that describes the user interface presentation of a custom type.
- [protocol StaticDisplayRepresentable](staticdisplayrepresentable.md)
  An interface for providing a static visual representation of a specific type.
- [protocol CaseDisplayRepresentable](casedisplayrepresentable.md)
  An interface for providing the visual representation for an iterable collection of values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/displayrepresentation)*