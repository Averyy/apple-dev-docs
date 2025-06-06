# appendInterpolation(_:)

**Framework**: App Intents  
**Kind**: method

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
mutating func appendInterpolation<ValueType, Subject>(_ subject: Subject) where ValueType : _IntentValue, ValueType : Sendable, Subject : KeyPath<Intent, IntentParameter<ValueType>>
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intenturlrepresentation/stringinterpolation/appendinterpolation(_:))*