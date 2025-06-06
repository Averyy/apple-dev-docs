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
init<V0, V1, V2, V3, V4, V5, P0, P1, P2, P3, P4, P5, K0, K1, K2, K3, K4, K5>(parameters: T, displayRepresentation: @escaping (V0, V1, V2, V3, V4, V5) -> DisplayRepresentation) where T == (K0, K1, K2, K3, K4, K5), V0 : _IntentValue, V0 : Sendable, V1 : _IntentValue, V1 : Sendable, V2 : _IntentValue, V2 : Sendable, V3 : _IntentValue, V3 : Sendable, V4 : _IntentValue, V4 : Sendable, V5 : _IntentValue, V5 : Sendable, P0 : IntentParameter<V0>, P1 : IntentParameter<V1>, P2 : IntentParameter<V2>, P3 : IntentParameter<V3>, P4 : IntentParameter<V4>, P5 : IntentParameter<V5>, K0 : KeyPath<Intent, P0>, K1 : KeyPath<Intent, P1>, K2 : KeyPath<Intent, P2>, K3 : KeyPath<Intent, P3>, K4 : KeyPath<Intent, P4>, K5 : KeyPath<Intent, P5>
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentprediction/init(parameters:displayrepresentation:)-2ct6i)*