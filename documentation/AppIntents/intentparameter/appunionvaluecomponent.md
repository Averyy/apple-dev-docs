# IntentParameter.AppUnionValueComponent

**Framework**: App Intents  
**Kind**: enum  
**Role**: Enumeration

The components of a union value parameter available for use in parameter summaries.

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
enum AppUnionValueComponent
```

Available when `Value` conforms to `_IntentValue`, `Value` conforms to `Sendable`, and `Value.ValueType` conforms to `AppUnionValue`.

## Topics

### Enumeration Cases
- [IntentParameter.AppUnionValueComponent.type](./appunionvaluecomponent/type.md)
  The case name component of this union value parameter.
- [IntentParameter.AppUnionValueComponent.value](./appunionvaluecomponent/value.md)
  The associated value of the selected case

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentparameter/appunionvaluecomponent)*