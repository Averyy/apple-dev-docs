# appendInterpolation(_:)

**Framework**: App Intents  
**Kind**: method

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
mutating func appendInterpolation<ValueType, Subject>(_ subject: Subject) where ValueType : _IntentValue, ValueType : Sendable, Subject : KeyPath<Intent, IntentParameter<ValueType>>
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/parametersummarystring/stringinterpolation/appendinterpolation(_:))*