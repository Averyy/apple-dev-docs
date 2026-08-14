# IntentValueConvertibleWrapper

**Framework**: App Intents  
**Kind**: protocol

A protocol for types that wrap another intent value that supports conversion.

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
protocol IntentValueConvertibleWrapper : IntentValueConvertible
```

#### Overview

`IntentValueConvertibleWrapper` enables you to create specialized types that derive their `IntentValueConvertible` conformance from an underlying base type. This pattern allows you to extend existing convertible types with additional functionality while preserving their ability to work within the AppIntents framework.

Use this protocol when you want to create a type that:

- Wraps an existing `IntentValueConvertible` type
- Adds domain-specific properties or methods
- Maintains compatibility with the AppIntents framework

#### Example

```swift
struct LandmarkEntity: IntentValueConvertibleWrapper {
    var baseValue: AnyAppEntity

    init(baseValue: AnyAppEntity) {
        self.baseValue = baseValue
    }

    var continent: String {
        get throws {
            try baseValue.continent
        }
    }
}
```

## Topics

### Associated Types
- [associatedtype BaseValue : IntentValueConvertible](intentvalueconvertiblewrapper/basevalue-swift.associatedtype.md)
  The underlying type that provides protocol conformance.
### Initializers
- [init(baseValue: Self.BaseValue) throws](intentvalueconvertiblewrapper/init(basevalue:).md)
  Creates a new instance that wraps the specified base value.
### Instance Properties
- [var baseValue: Self.BaseValue](intentvalueconvertiblewrapper/basevalue-swift.property.md)
  The underlying value that this type wraps.

## Relationships

### Inherits From
- [IntentValueConvertible](intentvalueconvertible.md)
- [IntentValueExpressing](intentvalueexpressing.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [protocol IntentValueConvertible](intentvalueconvertible.md)
  A protocol that allows the system to use types to as app intent parameters or properties.
- [protocol IntentValueExpressing](intentvalueexpressing.md)
  A protocol for types that can create intent value expressions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentvalueconvertiblewrapper)*