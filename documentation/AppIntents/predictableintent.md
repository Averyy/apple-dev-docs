# PredictableIntent

**Framework**: App Intents  
**Kind**: protocol

An interface that indicates the system can suggest the intent as a potential action to run.

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
protocol PredictableIntent : AppIntent
```

## Mentions

- [Donating your app’s data and actions to the system](donating-your-apps-data-and-actions-to-the-system.md)

#### Overview

Add support for the `PredictableIntent` protocol to an app intent to improve the descriptions that the system displays for your app intent. When making proactive suggestions in interfaces like the Siri Suggestions widget, the system displays the descriptions you provide using this protocol. Create descriptions that explain your action clearly and concisely using only the parameters you find relevant. For example, you might build a description that incorporates only one of several of the app intent’s parameters, if doing so leads to a more concise phrase.

In your implementation of this protocol, provide one or more [`IntentPrediction`](intentprediction.md) types in the [`predictionConfiguration`](predictableintent/predictionconfiguration.md) property. In each intent prediction, convey the purpose of your app intent using zero or more parameters. The following example shows an app intent offers a description using only the `name` parameter of the app intent.

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

### Specifying the prediction data
- [static var predictionConfiguration: Self.Prediction](predictableintent/predictionconfiguration.md)
  A collection of predictions the system can use when it suggests the app intent.
### Getting the supporting types
- [struct IntentPrediction](intentprediction.md)
  A prediction for an app intent that the system might display to someone when it’s relevant.
- [associatedtype Prediction : IntentPredictionConfiguration](predictableintent/prediction.md)
- [protocol IntentPredictionConfiguration](intentpredictionconfiguration.md)
  An interface that provides the configuration for a single prediction.
- [enum IntentPredictionsBuilder](intentpredictionsbuilder.md)
  A result builder that allows you to declaratively describe the predictions for an app intent.

## Relationships

### Inherits From
- [AppIntent](appintent.md)
- [PersistentlyIdentifiable](persistentlyidentifiable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [protocol UndoableIntent](undoableintent.md)
  An interface you use to register undoable actions in your app intent code.
- [protocol CancellableIntent](cancellableintent.md)
  An interface to support the graceful cancellation of your app intent’s task.
- [protocol LongRunningIntent](longrunningintent.md)
  An interface you use to extend the background execution time of an app intent that performs a long-running task.
- [struct IntentPrediction](intentprediction.md)
  A prediction for an app intent that the system might display to someone when it’s relevant.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/predictableintent)*