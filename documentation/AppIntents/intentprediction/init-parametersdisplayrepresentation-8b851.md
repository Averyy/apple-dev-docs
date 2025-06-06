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
init<V0, V1, V2, P0, P1, P2, K0, K1, K2>(parameters: T, displayRepresentation: @escaping (V0, V1, V2) -> DisplayRepresentation) where T == (K0, K1, K2), V0 : _IntentValue, V0 : Sendable, V1 : _IntentValue, V1 : Sendable, V2 : _IntentValue, V2 : Sendable, P0 : IntentParameter<V0>, P1 : IntentParameter<V1>, P2 : IntentParameter<V2>, K0 : KeyPath<Intent, P0>, K1 : KeyPath<Intent, P1>, K2 : KeyPath<Intent, P2>
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentprediction/init(parameters:displayrepresentation:)-8b851)*