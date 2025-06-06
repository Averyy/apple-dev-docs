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
mutating func appendInterpolation<Value, Subject>(_ subject: Subject) where Value : _IntentValue, Value : Sendable, Subject : KeyPath<Intent, IntentParameter<Value>>
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appshortcutphrase/stringinterpolation/appendinterpolation(_:)-5kcab)*