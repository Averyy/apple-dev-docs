# type

**Framework**: App Intents  
**Kind**: property  
**Role**: Instance Property

The case name component of this union value parameter.

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
final var type: IntentParameter<Value>.AppUnionValueComponent { get }
```

Available when `Value` conforms to `_IntentValue`, `Value` conforms to `Sendable`, and `Value.ValueType` conforms to `AppUnionValue`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentparameter/type)*