# UndoableIntent

**Framework**: App Intents  
**Kind**: protocol

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

## Topics

### Instance Properties
- [var undoManager: UndoManager?](undoableintent/undomanager.md)
  An app intent’s `perform` method should use this undo manager to register operations that undo the effect of the app intent’s performance

## Relationships

### Inherits From
- [AppIntent](appintent.md)
- [PersistentlyIdentifiable](persistentlyidentifiable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [SystemIntent](systemintent.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/undoableintent)*