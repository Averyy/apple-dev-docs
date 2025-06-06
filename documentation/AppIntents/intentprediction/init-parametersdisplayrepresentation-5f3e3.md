# init(parameters:displayRepresentation:)

**Framework**: App Intents  
**Kind**: init

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
init<V0, P0>(parameters: T, displayRepresentation: @escaping (V0) -> DisplayRepresentation) where T == KeyPath<Intent, P0>, V0 : _IntentValue, V0 : Sendable, P0 : IntentParameter<V0>
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentprediction/init(parameters:displayrepresentation:)-5f3e3)*