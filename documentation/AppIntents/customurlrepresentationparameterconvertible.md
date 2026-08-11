# CustomURLRepresentationParameterConvertible

**Framework**: App Intents  
**Kind**: protocol

An interface that allows a type to express its contents in a URL representation.

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
protocol CustomURLRepresentationParameterConvertible
```

#### Overview

Apply this protocol to the custom types you use to build the URL for an app intent or app entity. When you construct a URL representation, you can incorporate the properties of your app intent or app entity type into the URL you produce. The [`EntityURLRepresentation`](entityurlrepresentation.md), [`IntentURLRepresentation`](intenturlrepresentation.md), and [`EnumURLRepresentation`](enumurlrepresentation.md) types automatically convert properties with [`String`](https://developer.apple.com/documentation/Swift/String), [`Int`](https://developer.apple.com/documentation/Swift/Int), or [`URL`](https://developer.apple.com/documentation/Foundation/URL) values to the required string data for the representation. For other types, adopt this protocol and use the [`urlRepresentationParameter`](customurlrepresentationparameterconvertible/urlrepresentationparameter.md) property to deliver a string that represents your type’s content.

## Topics

### Instance Properties
- [var urlRepresentationParameter: String?](customurlrepresentationparameterconvertible/urlrepresentationparameter.md)
  The string representation of the type’s content.

## Relationships

### Inherited By
- [URLRepresentableEntity](urlrepresentableentity.md)
- [URLRepresentableEnum](urlrepresentableenum.md)

## See Also

- [protocol URLRepresentableEntity](urlrepresentableentity.md)
  An interface you apply to an app entity type so the system can handle it like a universal link.
- [struct EntityURLRepresentation](entityurlrepresentation.md)
  The type that provides the URL for an app entity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/customurlrepresentationparameterconvertible)*