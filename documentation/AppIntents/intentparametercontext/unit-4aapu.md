# unit

**Framework**: App Intents  
**Kind**: property  
**Role**: Instance Property

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS
- watchOS 9.0+

## Declaration

```swift
var unit: IntentParameter<Measurement<UnitTemperature>>.Temperature? { get }
```

Available when `Value` conforms to `_IntentValue`, `Value` conforms to `Sendable`, and `Value.ValueType` is `Measurement<UnitTemperature>`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentparametercontext/unit-4aapu)*