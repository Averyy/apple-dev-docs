# init(_:_:)

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
convenience init<V0, P0, V1, P1>(_ k0: KeyPath<Intent, P0>, _ k1: KeyPath<Intent, P1>) where V0 : _IntentValue, V0 : Sendable, P0 : IntentParameter<V0>, V1 : _IntentValue, V1 : Sendable, P1 : IntentParameter<V1>
```

Available when `Intent` conforms to `AppIntent`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentparameterdependency/init(_:_:))*