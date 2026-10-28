# undoManager

**Framework**: App Intents  
**Kind**: property  
**Role**: Instance Property

The undo manager you use to register undo actions for your app intents.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
@MainActor
var undoManager: UndoManager? { get }
```

## Discussion

In your app intent’s [`perform()`](../appintent/perform%28%29.md) method, use this property to get an undo manager suitable for registering undoable actions. The system makes every effort to find a suitable undo manager given the current state of your app or app extension. However, if a suitable undo manager isn’t available, the value of this property is `nil`.

Use the undo manager in this property only to register your undoable actions. App intents don’t initiate calls to the [`undo()`](../../Foundation/undomanager/undo%28%29.md) or [`redo()`](../../Foundation/undomanager/redo%28%29.md) methods of the undo manager. Your app initiates undo and redo operations in response to interactions with its menus or interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/undoableintent/undomanager)*