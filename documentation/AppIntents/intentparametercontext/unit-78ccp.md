# unit

**Framework**: App Intents  
**Kind**: property  
**Role**: Instance Property

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS
- watchOS 10.0+

## Declaration

```swift
var unit: IntentParameter<Measurement<UnitAngle>>.Angle? { get }
```

Available when `Value` conforms to `_IntentValue`, `Value` conforms to `Sendable`, and `Value.ValueType` is `Measurement<UnitAngle>`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentparametercontext/unit-78ccp)*