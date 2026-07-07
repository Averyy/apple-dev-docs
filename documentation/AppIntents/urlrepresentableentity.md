# URLRepresentableEntity

**Framework**: App Intents  
**Kind**: protocol

An app entity with a URL representation.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
protocol URLRepresentableEntity : AppEntity, CustomURLRepresentationParameterConvertible
```

#### Overview

Add support for `URLRepresentableEntity` to your app entities to add a URL representation. This allows Apple Intelligence, Siri, and Shortcuts to treat the entity like a universal link to specific content, allowing actions to open the URL or to make it sharable.

Note that you need to use a universal link for your URL representation, you can’t use a custom URL scheme. For more information about universal links, see [`Allowing apps and websites to link to your content`](https://developer.apple.com/documentation/Xcode/allowing-apps-and-websites-to-link-to-your-content).

## Topics

### Type Aliases
- [URLRepresentableEntity.URLRepresentation](urlrepresentableentity/urlrepresentation-swift.typealias.md)
### Type Properties
- [static var urlRepresentation: Self.URLRepresentation](urlrepresentableentity/urlrepresentation-swift.type.property.md)

## Relationships

### Inherits From
- [AppEntity](appentity.md)
- [AppValue](appvalue.md)
- [CustomLocalizedStringResourceConvertible](../Foundation/CustomLocalizedStringResourceConvertible.md)
- [CustomURLRepresentationParameterConvertible](customurlrepresentationparameterconvertible.md)
- [DisplayRepresentable](displayrepresentable.md)
- [Identifiable](../Swift/Identifiable.md)
- [InstanceDisplayRepresentable](instancedisplayrepresentable.md)
- [PersistentlyIdentifiable](persistentlyidentifiable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [TypeDisplayRepresentable](typedisplayrepresentable.md)

## See Also

- [struct EntityURLRepresentation](entityurlrepresentation.md)
  The URL representation of an app entity.
- [protocol CustomURLRepresentationParameterConvertible](customurlrepresentationparameterconvertible.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/urlrepresentableentity)*