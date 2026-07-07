# IntentPrediction

**Framework**: App Intents  
**Kind**: struct

A prediction for an app intent that the system might display to someone when it’s relevant.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS ?+
- watchOS 9.0+

## Declaration

```swift
struct IntentPrediction<Intent, T> where Intent : AppIntent
```

#### Overview

Use the `IntentPrediction` type to provide a description of your app intent that the system can use when offering proactive suggestions. You create this type from the [`predictionConfiguration`](predictableintent/predictionconfiguration.md) property of your app intent. Use the type to provide a [`DisplayRepresentation`](displayrepresentation.md) structure with a suitable description of your app intent’s purpose.

The following example shows an implementation of the [`predictionConfiguration`](predictableintent/predictionconfiguration.md) property that creates an `IntentPrediction` type. During creation of the type, the code passes the app intent’s `name` property to the `IntentPrediction` initializer, and maps it to the `name` parameter in the closure. The description incorporates this value in the text it provides.

```swift
struct CreateBook: AppIntent, PredictableIntent {
    @Parameter(title: "Book Name")
    var name: String?

    @Parameter(title: "Author", query: AuthorQuery.self)
    var author: AuthorEntity?

    static var predictionConfiguration: some IntentPredictionConfiguration {
        IntentPrediction(parameters: (\Self.$name)) { name in
            DisplayRepresentation(
                title: "Create a book named \(name)"
            )
        }
    }

    @MainActor
    func perform() async throws -> IntentResult<BookEntity> {
        ...
    }
}
```

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

- [protocol UndoableIntent](undoableintent.md)
  An interface you use to register undoable actions in your app intent code.
- [protocol CancellableIntent](cancellableintent.md)
  An interface to support the graceful cancellation of your app intent’s task.
- [protocol LongRunningIntent](longrunningintent.md)
  An interface you use to extend the background execution time of an app intent that performs a long-running task.
- [protocol PredictableIntent](predictableintent.md)
  An interface that indicates the system can suggest the intent as a potential action to run.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentprediction)*