# init(_:_:_:_:_:)

**Framework**: App Intents  
**Kind**: init  
**Role**: Initializer

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
convenience init<V0, P0, V1, P1, V2, P2, V3, P3, V4, P4>(_ k0: KeyPath<Intent, P0>, _ k1: KeyPath<Intent, P1>, _ k2: KeyPath<Intent, P2>, _ k3: KeyPath<Intent, P3>, _ k4: KeyPath<Intent, P4>) where V0 : _IntentValue, V0 : Sendable, P0 : IntentParameter<V0>, V1 : _IntentValue, V1 : Sendable, P1 : IntentParameter<V1>, V2 : _IntentValue, V2 : Sendable, P2 : IntentParameter<V2>, V3 : _IntentValue, V3 : Sendable, P3 : IntentParameter<V3>, V4 : _IntentValue, V4 : Sendable, P4 : IntentParameter<V4>
```

Available when `Intent` conforms to `AppIntent`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentparameterdependency/init(_:_:_:_:_:))*