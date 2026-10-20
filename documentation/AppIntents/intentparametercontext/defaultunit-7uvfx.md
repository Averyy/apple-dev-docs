# defaultUnit

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
var defaultUnit: IntentParameter<Measurement<UnitDuration>>.Duration? { get }
```

Available when `Value` conforms to `_IntentValue`, `Value` conforms to `Sendable`, and `Value.ValueType` is `Measurement<UnitDuration>`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentparametercontext/defaultunit-7uvfx)*