# HistoryObserver

**Framework**: SwiftData  
**Kind**: class

Monitors a model container’s data stores for remote changes and notifies when new history transactions are available.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
final class HistoryObserver
```

#### Overview

`HistoryObserver` automatically listens for `ModelContainer/remoteChange` notifications and determines whether the incoming changes are relevant based on the models you specify at initialization. When relevant changes are detected, the observer updates its [`eventCounter`](historyobserver/eventcounter.md) property.

Use `HistoryObserver` as an `@Observable` object and react to changes in [`eventCounter`](historyobserver/eventcounter.md) from a SwiftUI view or other observer.

The observer tracks its position in each data store’s transaction history using `historyTokens`, enabling incremental processing of only new transactions since the last check.

You can scope the observer to specific model types using the `observedModels` parameter. When provided with a non-empty array, the observer filters incoming transactions to only those containing changes for the specified types (and optionally their related models). When the array is empty (the default), the observer responds to any history change in the container.

Example usage:

```swift
let observer = try HistoryObserver(
    observedModels: [Trip.self],
    modelContainer: container
)
```

## Topics

### Creating a history observer
- [convenience init(historyTokens: [String : any HistoryToken]?, observedModels: [any PersistentModel.Type], authors: Set<String>, modelContainer: ModelContainer, isolation: isolated (any Actor)?) throws](historyobserver/init(historytokens:observedmodels:authors:modelcontainer:isolation:).md)
  Creates a history observer that reports changes through its observable [`eventCounter`](historyobserver/eventcounter.md) property.
### Accessing observer properties
- [var eventCounter: Int](historyobserver/eventcounter.md)
  A counter that increments each time the observer detects relevant changes.
- [let modelContainer: ModelContainer](historyobserver/modelcontainer.md)
  The model container whose data stores this observer monitors for changes.
- [let observedModels: [any PersistentModel.Type]](historyobserver/observedmodels.md)
  The model types that the observer filters for when evaluating history transactions.
- [let authors: Set<String>](historyobserver/authors.md)
  The transaction authors that the observer filters for when evaluating history transactions.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Escapable](../Swift/Escapable.md)
- [Observable](../Observation/Observable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class ResultsObserver](resultsobserver.md)
  Observes and tracks changes to a collection of persistent models in a model context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftdata/historyobserver)*