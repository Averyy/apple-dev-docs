# IntentValueConvertible

**Framework**: App Intents  
**Kind**: protocol

A protocol that allows the system to use types to as app intent parameters or properties.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
protocol IntentValueConvertible : IntentValueExpressing
```

#### Overview

A type that conforms to `IntentValueConvertible` enables the App Intents framework to convert it to and from intent value containers. This protocol forms the foundation of the App Intents type conversion system, enabling seamless data exchange between your app and the AppIntents framework.

To make a custom type usable in AppIntents, conform it to this protocol by implementing the required [`makeContainer(context:)`](intentvalueconvertible/makecontainer(context:).md) method.

## Topics

### Instance Methods
- [func makeContainer(context: IntentValueContainer.ConversionContext) -> IntentValueContainer](intentvalueconvertible/makecontainer(context:).md)
  Creates an intent value container that represents this value.

## Relationships

### Inherits From
- [IntentValueExpressing](intentvalueexpressing.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)
### Inherited By
- [IntentValueConvertibleWrapper](intentvalueconvertiblewrapper.md)
### Conforming Types
- [IntentCurrencyAmount](intentcurrencyamount.md)
- [IntentFile](intentfile.md)
- [IntentPaymentMethod](intentpaymentmethod.md)
- [IntentPerson](intentperson.md)
- [StringSearchCriteria](stringsearchcriteria.md)
- [SystemShortcut](systemshortcut.md)

## See Also

- [protocol IntentValueConvertibleWrapper](intentvalueconvertiblewrapper.md)
  A protocol for types that wrap another intent value that supports conversion.
- [protocol IntentValueExpressing](intentvalueexpressing.md)
  A protocol for types that can create intent value expressions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentvalueconvertible)*