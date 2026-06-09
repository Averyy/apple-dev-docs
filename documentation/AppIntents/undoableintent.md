# UndoableIntent

**Framework**: App Intents  
**Kind**: protocol

An interface you use to register undoable actions in your app intent code.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
protocol UndoableIntent : SystemIntent
```

## Mentions

- [Creating your first app intent](creating-your-first-app-intent.md)

#### Overview

Add support for this protocol if your app intent performs a task that someone might want to undo from your app’s interface. This protocol provides access to an instance of the [`UndoManager`](https://developer.apple.com/documentation/Foundation/UndoManager) type suitable for use in your app intent’s code. You can use this undo manager from either your app or an app extension you use to run app intents.

For more information about adding undo support to your code, see the [`UndoManager`](https://developer.apple.com/documentation/Foundation/UndoManager) type.

## Topics

### Getting the undo manager
- [var undoManager: UndoManager?](undoableintent/undomanager.md)
  The undo manager you use to register undo actions for your app intents.

## Relationships

### Inherits From
- [AppIntent](appintent.md)
- [PersistentlyIdentifiable](persistentlyidentifiable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [SystemIntent](systemintent.md)

## See Also

- [protocol CancellableIntent](cancellableintent.md)
  An interface to support the graceful cancellation of your app intent’s task.
- [protocol LongRunningIntent](longrunningintent.md)
  An interface you use to extend the background execution time of an app intent that performs a long-running task.
- [protocol PredictableIntent](predictableintent.md)
  An interface that indicates the system can suggest the intent as a potential action to run.
- [struct IntentPrediction](intentprediction.md)
  A prediction for an app intent that the system might display to someone when it’s relevant.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/undoableintent)*