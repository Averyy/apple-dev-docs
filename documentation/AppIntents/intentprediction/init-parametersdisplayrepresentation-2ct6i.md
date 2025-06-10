# init(parameters:displayRepresentation:)

**Framework**: App Intents  
**Kind**: init

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst ?+
- macOS 13.0+
- tvOS 16.0+
- visionOS ?+
- watchOS 9.0+

## Declaration

```swift
init<V0, V1, V2, V3, V4, V5, P0, P1, P2, P3, P4, P5, K0, K1, K2, K3, K4, K5>(parameters: T, displayRepresentation: @escaping (V0, V1, V2, V3, V4, V5) -> DisplayRepresentation) where T == (K0, K1, K2, K3, K4, K5), V0 : _IntentValue, V0 : Sendable, V1 : _IntentValue, V1 : Sendable, V2 : _IntentValue, V2 : Sendable, V3 : _IntentValue, V3 : Sendable, V4 : _IntentValue, V4 : Sendable, V5 : _IntentValue, V5 : Sendable, P0 : IntentParameter<V0>, P1 : IntentParameter<V1>, P2 : IntentParameter<V2>, P3 : IntentParameter<V3>, P4 : IntentParameter<V4>, P5 : IntentParameter<V5>, K0 : KeyPath<Intent, P0>, K1 : KeyPath<Intent, P1>, K2 : KeyPath<Intent, P2>, K3 : KeyPath<Intent, P3>, K4 : KeyPath<Intent, P4>, K5 : KeyPath<Intent, P5>
```

## See Also

- [init(displayRepresentation: () -> DisplayRepresentation)](intentprediction/init(displayrepresentation:).md)
- [init<V0, V1, V2, V3, V4, V5, V6, V7, V8, V9, V10, P0, P1, P2, P3, P4, P5, P6, P7, P8, P9, P10, K0, K1, K2, K3, K4, K5, K6, K7, K8, K9, K10>(parameters: T, displayRepresentation: (V0, V1, V2, V3, V4, V5, V6, V7, V8, V9, V10) -> DisplayRepresentation)](intentprediction/init(parameters:displayrepresentation:)-1zdkp.md)
- [init<V0, V1, V2, V3, V4, V5, V6, V7, V8, V9, V10, V11, V12, V13, V14, P0, P1, P2, P3, P4, P5, P6, P7, P8, P9, P10, P11, P12, P13, P14, K0, K1, K2, K3, K4, K5, K6, K7, K8, K9, K10, K11, K12, K13, K14>(parameters: T, displayRepresentation: (V0, V1, V2, V3, V4, V5, V6, V7, V8, V9, V10, V11, V12, V13, V14) -> DisplayRepresentation)](intentprediction/init(parameters:displayrepresentation:)-2lf5t.md)
- [init<V0, V1, V2, V3, V4, V5, V6, V7, V8, V9, V10, V11, V12, V13, V14, P0, P1, P2, P3, P4, P5, P6, P7, P8, P9, P10, P11, P12, P13, P14, K0, K1, K2, K3, K4, K5, K6, K7, K8, K9, K10, K11, K12, K13, K14>(parameters: T, displayRepresentation: (V0, V1, V2, V3, V4, V5, V6, V7, V8, V9, V10, V11, V12, V13, V14) -> DisplayRepresentation)](intentprediction/init(parameters:displayrepresentation:)-2lf5t.md)
- [init<V0, V1, P0, P1, K0, K1>(parameters: T, displayRepresentation: (V0, V1) -> DisplayRepresentation)](intentprediction/init(parameters:displayrepresentation:)-39wfu.md)
- [init<V0, V1, V2, V3, V4, V5, V6, V7, V8, V9, P0, P1, P2, P3, P4, P5, P6, P7, P8, P9, K0, K1, K2, K3, K4, K5, K6, K7, K8, K9>(parameters: T, displayRepresentation: (V0, V1, V2, V3, V4, V5, V6, V7, V8, V9) -> DisplayRepresentation)](intentprediction/init(parameters:displayrepresentation:)-3wlt7.md)
- [init<V0, P0>(parameters: T, displayRepresentation: (V0) -> DisplayRepresentation)](intentprediction/init(parameters:displayrepresentation:)-5f3e3.md)
- [init<V0, V1, V2, V3, V4, V5, V6, V7, V8, V9, V10, V11, V12, P0, P1, P2, P3, P4, P5, P6, P7, P8, P9, P10, P11, P12, K0, K1, K2, K3, K4, K5, K6, K7, K8, K9, K10, K11, K12>(parameters: T, displayRepresentation: (V0, V1, V2, V3, V4, V5, V6, V7, V8, V9, V10, V11, V12) -> DisplayRepresentation)](intentprediction/init(parameters:displayrepresentation:)-620xt.md)
- [init<V0, V1, V2, V3, V4, P0, P1, P2, P3, P4, K0, K1, K2, K3, K4>(parameters: T, displayRepresentation: (V0, V1, V2, V3, V4) -> DisplayRepresentation)](intentprediction/init(parameters:displayrepresentation:)-6i80a.md)
- [init<V0, V1, V2, V3, V4, V5, V6, V7, P0, P1, P2, P3, P4, P5, P6, P7, K0, K1, K2, K3, K4, K5, K6, K7>(parameters: T, displayRepresentation: (V0, V1, V2, V3, V4, V5, V6, V7) -> DisplayRepresentation)](intentprediction/init(parameters:displayrepresentation:)-781f1.md)
- [init<V0, V1, V2, P0, P1, P2, K0, K1, K2>(parameters: T, displayRepresentation: (V0, V1, V2) -> DisplayRepresentation)](intentprediction/init(parameters:displayrepresentation:)-8b851.md)
- [init<V0, V1, V2, V3, V4, V5, V6, P0, P1, P2, P3, P4, P5, P6, K0, K1, K2, K3, K4, K5, K6>(parameters: T, displayRepresentation: (V0, V1, V2, V3, V4, V5, V6) -> DisplayRepresentation)](intentprediction/init(parameters:displayrepresentation:)-9ibp3.md)
- [init<V0, V1, V2, V3, V4, V5, V6, V7, V8, P0, P1, P2, P3, P4, P5, P6, P7, P8, K0, K1, K2, K3, K4, K5, K6, K7, K8>(parameters: T, displayRepresentation: (V0, V1, V2, V3, V4, V5, V6, V7, V8) -> DisplayRepresentation)](intentprediction/init(parameters:displayrepresentation:)-alik.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentprediction/init(parameters:displayrepresentation:)-2ct6i)*