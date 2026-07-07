# URLRepresentableEnum

**Framework**: App Intents  
**Kind**: protocol

An app enum with a URL representation.

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

Add support for `URLRepresentableEnum` to your app enums to add a URL representation. This allows Apple Intelligence, Siri, and Shortcuts to treat the enum like a universal link to specific content, allowing actions to open the URL or to make it sharable.

Note that you need to use a universal link for your URL representation, you can’t use a custom URL scheme. For more information about universal links, see [`Allowing apps and websites to link to your content`](https://developer.apple.com/documentation/Xcode/allowing-apps-and-websites-to-link-to-your-content).

## Topics

### Type Aliases
- [URLRepresentableEnum.URLRepresentation](urlrepresentableenum/urlrepresentation-swift.typealias.md)
### Type Properties
- [static var urlRepresentation: Self.URLRepresentation](urlrepresentableenum/urlrepresentation-swift.type.property.md)

## Relationships

### Inherits From
- [AppEnum](appenum.md)
- [AppValue](appvalue.md)
- [CaseDisplayRepresentable](casedisplayrepresentable.md)
- [CaseIterable](../Swift/CaseIterable.md)
- [CustomLocalizedStringResourceConvertible](../Foundation/CustomLocalizedStringResourceConvertible.md)
- [CustomURLRepresentationParameterConvertible](customurlrepresentationparameterconvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [PersistentlyIdentifiable](persistentlyidentifiable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [StaticDisplayRepresentable](staticdisplayrepresentable.md)
- [TypeDisplayRepresentable](typedisplayrepresentable.md)

## See Also

- [struct EnumURLRepresentation](enumurlrepresentation.md)
  The URL representation of an app enum.
- [protocol CustomURLRepresentationParameterConvertible](customurlrepresentationparameterconvertible.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/urlrepresentableenum)*