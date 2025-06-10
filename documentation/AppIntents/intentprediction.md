# IntentPrediction

**Framework**: App Intents  
**Kind**: struct

A prediction for a specific app intent that the system might display to someone when it’s relevant.

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
struct IntentPrediction<Intent, T> where Intent : AppIntent
```

#### Overview

Includes the predicted parameters, and ways to get a user-visible description for a predicted or suggested action given those parameters.

## Topics

### Creating a prediction
- [init(displayRepresentation: () -> DisplayRepresentation)](intentprediction/init(displayrepresentation:).md)
- [init<V0, V1, V2, V3, V4, V5, V6, V7, V8, V9, V10, P0, P1, P2, P3, P4, P5, P6, P7, P8, P9, P10, K0, K1, K2, K3, K4, K5, K6, K7, K8, K9, K10>(parameters: T, displayRepresentation: (V0, V1, V2, V3, V4, V5, V6, V7, V8, V9, V10) -> DisplayRepresentation)](intentprediction/init(parameters:displayrepresentation:)-1zdkp.md)
- [init<V0, V1, V2, V3, V4, V5, P0, P1, P2, P3, P4, P5, K0, K1, K2, K3, K4, K5>(parameters: T, displayRepresentation: (V0, V1, V2, V3, V4, V5) -> DisplayRepresentation)](intentprediction/init(parameters:displayrepresentation:)-2ct6i.md)
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
### Initializers
- [init<V0, V1, V2, V3, V4, V5, V6, V7, V8, V9, V10, V11, P0, P1, P2, P3, P4, P5, P6, P7, P8, P9, P10, P11, K0, K1, K2, K3, K4, K5, K6, K7, K8, K9, K10, K11>(parameters: T, displayRepresentation: (V0, V1, V2, V3, V4, V5, V6, V7, V8, V9, V10, V11) -> DisplayRepresentation)](intentprediction/init(parameters:displayrepresentation:)-1uup3.md)
- [init<V0, V1, V2, V3, P0, P1, P2, P3, K0, K1, K2, K3>(parameters: T, displayRepresentation: (V0, V1, V2, V3) -> DisplayRepresentation)](intentprediction/init(parameters:displayrepresentation:)-n8dp.md)
- [init<V0, V1, V2, V3, V4, V5, V6, V7, V8, V9, V10, V11, V12, V13, P0, P1, P2, P3, P4, P5, P6, P7, P8, P9, P10, P11, P12, P13, K0, K1, K2, K3, K4, K5, K6, K7, K8, K9, K10, K11, K12, K13>(parameters: T, displayRepresentation: (V0, V1, V2, V3, V4, V5, V6, V7, V8, V9, V10, V11, V12, V13) -> DisplayRepresentation)](intentprediction/init(parameters:displayrepresentation:)-te8o.md)

## Relationships

### Conforms To
- [IntentPredictionConfiguration](intentpredictionconfiguration.md)

## See Also

- [protocol PredictableIntent](predictableintent.md)
  An interface that allows the system to suggest the app intent to someone in the future using predictions you provide.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentprediction)*