# URLRepresentableEnum

**Framework**: App Intents  
**Kind**: protocol

An interface you apply to an app enum type so the system can handle it like a universal link.

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
protocol URLRepresentableEnum : AppEnum, CustomURLRepresentationParameterConvertible
```

#### Overview

If your app already supports universal links for content, use this protocol to express your app enum types as URLs. When your app enum supports this protocol, the system can use the provided URL to refer to the item. Having a URL representation for your app entity also makes it easier to share the contents of that entity with Siri, Shortcuts, and other system features.

> ❗ **Important**: This protocol requires your app to support universal links. You can’t use this protocol with a custom URL scheme or other approaches. For information about how to add support for universal links, see [`Allowing apps and websites to link to your content`](https://developer.apple.com/documentation/xcode/allowing-apps-and-websites-to-link-to-your-content).

Construct URLs using static text and the value of your app enum. For more information on how to create the URL representation, see [`EnumURLRepresentation`](enumurlrepresentation.md).

## Topics

### Type Aliases
- [URLRepresentableEnum.URLRepresentation](urlrepresentableenum/urlrepresentation-swift.typealias.md)
  The type that provides the URL for the app enum.
### Type Properties
- [static var urlRepresentation: Self.URLRepresentation](urlrepresentableenum/urlrepresentation-swift.type.property.md)
  The URL representation of the app enum.

## Relationships

### Inherits From
- [AppEnum](appenum.md)
- [AppValue](appvalue.md)
- [CaseDisplayRepresentable](casedisplayrepresentable.md)
- [CaseIterable](../swift/caseiterable.md)
- [CustomLocalizedStringResourceConvertible](../foundation/customlocalizedstringresourceconvertible.md)
- [CustomURLRepresentationParameterConvertible](customurlrepresentationparameterconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [PersistentlyIdentifiable](persistentlyidentifiable.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)
- [StaticDisplayRepresentable](staticdisplayrepresentable.md)
- [TypeDisplayRepresentable](typedisplayrepresentable.md)

## See Also

- [struct EnumURLRepresentation](enumurlrepresentation.md)
  The type that provides the URL for an app enum.
- [protocol CustomURLRepresentationParameterConvertible](customurlrepresentationparameterconvertible.md)
  An interface that allows a type to express its contents in a URL representation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/urlrepresentableenum)*