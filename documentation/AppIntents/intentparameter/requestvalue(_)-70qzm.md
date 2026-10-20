# requestValue(_:)

**Framework**: App Intents  
**Kind**: method  
**Role**: Instance Method

Request a value from the user for this parameter.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS
- watchOS 9.0+

> **Deprecated**: Use `requestValue(_:)` or `needsValueError(_:)` instead

## Declaration

```swift
final func requestValue(_ dialog: IntentDialog? = nil) -> any Error
```

Available when `Value` conforms to `_IntentValue` and `Sendable`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentparameter/requestvalue(_:)-70qzm)*