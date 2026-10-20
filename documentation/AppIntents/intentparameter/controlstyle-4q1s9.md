# controlStyle

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
final var controlStyle: IntentParameter<Value>.IntControlStyle? { get }
```

Available when `Value` conforms to `_IntentValue`, `Value` conforms to `Sendable`, and `Value.ValueType` is `Int`.

## See Also

### Accessing the control style
- [IntentParameter.IntControlStyle](./intcontrolstyle.md)
  An enum that describes the control style of an Integer parameter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentparameter/controlstyle-4q1s9)*