# IntentValueExpressing

**Framework**: App Intents  
**Kind**: protocol

A protocol for types that can create intent value expressions.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
protocol IntentValueExpressing : Sendable
```

#### Overview

`IntentValueExpressing` enables types to participate in the lazy evaluation system of the App Intents framework. Types conforming to this protocol can create expressions that are evaluated only when needed, improving performance by deferring potentially expensive conversions.

This protocol forms the foundation of the lazy evaluation mechanism in the intent value conversion system.

## Topics

### Instance Methods
- [func makeExpression() -> IntentValueExpression](intentvalueexpressing/makeexpression.md)
  Creates an intent value expression that represents this value.

## Relationships

### Inherits From
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)
### Inherited By
- [IntentValueConvertible](intentvalueconvertible.md)
- [IntentValueConvertibleWrapper](intentvalueconvertiblewrapper.md)
### Conforming Types
- [IntentCurrencyAmount](intentcurrencyamount.md)
- [IntentFile](intentfile.md)
- [IntentPaymentMethod](intentpaymentmethod.md)
- [IntentPerson](intentperson.md)
- [IntentValueContainer](intentvaluecontainer.md)
- [StringSearchCriteria](stringsearchcriteria.md)
- [SystemShortcut](systemshortcut.md)

## See Also

- [protocol IntentValueConvertible](intentvalueconvertible.md)
  A protocol that allows the system to use types to as app intent parameters or properties.
- [protocol IntentValueConvertibleWrapper](intentvalueconvertiblewrapper.md)
  A protocol for types that wrap another intent value that supports conversion.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentvalueexpressing)*