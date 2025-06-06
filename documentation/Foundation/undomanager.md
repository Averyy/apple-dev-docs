# UndoManager

**Framework**: Foundation  
**Kind**: class

A general-purpose recorder of operations that enables undo and redo.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class UndoManager
```

#### Overview

You register an undo operation by calling one of the methods described in Registering undo operations. You specify the name of the object that’s changing (or the owner of that object) and provide a closure, method, or invocation to revert its state.

After you register an undo operation, you can call [`undo()`](undomanager/undo().md) on the undo manager to revert to the state of the last undo operation. When undoing an action, [`UndoManager`](undomanager.md) saves the operations you revert to so that you can call [`redo()`](undomanager/redo().md) automatically.

Typically, apps with UI interactions work with [`UndoManager`](undomanager.md). For example, UIKit implements undo and redo in its text view object, making it easy for you to undo and redo actions in objects along the responder chain. [`UndoManager`](undomanager.md) also serves as a general-purpose state manager, which you can use to undo and redo many kinds of actions. For example, an interactive command-line utility can use this class to undo the last command run, or a networking library can undo a request by sending another request that invalidates the previous one.

## Topics

### Registering undo operations
- [func registerUndo<TargetType>(withTarget: TargetType, handler: (TargetType) -> Void)](undomanager/registerundo(withtarget:handler:).md)
  Registers the specified closure to implement a single undo operation that the target receives.
- [func registerUndo(withTarget: Any, selector: Selector, object: Any?)](undomanager/registerundo(withtarget:selector:object:).md)
  Registers the selector of the specified target to implement a single undo operation that the target receives.
- [func prepare(withInvocationTarget: Any) -> Any](undomanager/prepare(withinvocationtarget:).md)
  Prepares the undo manager for invocation-based undo with the given target as the subject of the next undo operation.
### Checking undo ability
- [var canUndo: Bool](undomanager/canundo.md)
  A Boolean value that indicates whether the manager has any actions to undo.
- [var canRedo: Bool](undomanager/canredo.md)
  A Boolean value that indicates whether the manager has any actions to redo.
### Performing undo and redo
- [func undo()](undomanager/undo.md)
  Closes the top-level undo group if necessary, and then performs undo operations on the group.
- [func undoNestedGroup()](undomanager/undonestedgroup.md)
  Performs the undo operations in the last undo group (whether top-level or nested), recording the operations on the redo stack as a single group.
- [func redo()](undomanager/redo.md)
  Performs the operations in the last group on the redo stack, if there are any, recording them on the undo stack as a single group.
### Managing undo and redo stack depth
- [var levelsOfUndo: Int](undomanager/levelsofundo.md)
  The maximum number of top-level undo groups the undo manager holds.
- [var undoCount: Int](undomanager/undocount.md)
  The number of times you can invoke undo before there are no actions left to undo.
- [var redoCount: Int](undomanager/redocount.md)
  The number of times you can invoke redo before there are no actions left to redo.
### Creating undo groups
- [func beginUndoGrouping()](undomanager/beginundogrouping.md)
  Marks the beginning of an undo group.
- [func endUndoGrouping()](undomanager/endundogrouping.md)
  Marks the end of an undo group.
- [var groupsByEvent: Bool](undomanager/groupsbyevent.md)
  A Boolean value that indicates whether the manager automatically creates undo groups around each pass of the run loop.
- [var groupingLevel: Int](undomanager/groupinglevel.md)
  The number of nested undo groups (or redo groups, if redo is the most recent operation) in the current event loop.
### Enabling and disabling undo
- [func disableUndoRegistration()](undomanager/disableundoregistration.md)
  Disables the recording of undo operations.
- [func enableUndoRegistration()](undomanager/enableundoregistration.md)
  Enables the recording of undo operations.
- [var isUndoRegistrationEnabled: Bool](undomanager/isundoregistrationenabled.md)
  A Boolean value that indicates whether the recording of undo operations is enabled.
### Checking whether undo or redo is in process
- [var isUndoing: Bool](undomanager/isundoing.md)
  Returns a Boolean value that indicates whether the manager is in the process of performing an undo action.
- [var isRedoing: Bool](undomanager/isredoing.md)
  Returns a Boolean value that indicates whether the manager is in the process of performing a redo action.
### Clearing undo operations
- [func removeAllActions()](undomanager/removeallactions.md)
  Clears the undo and redo stacks and reenables the manager.
- [func removeAllActions(withTarget: Any)](undomanager/removeallactions(withtarget:).md)
  Clears the undo and redo stacks of all operations involving the specified target as the recipient of the undo message.
### Managing the action name
- [var undoActionName: String](undomanager/undoactionname.md)
  The name identifying the undo action.
- [var redoActionName: String](undomanager/redoactionname.md)
  The name identifying the redo action.
- [func setActionName(String)](undomanager/setactionname(_:).md)
  Sets the name of the action associated with the Undo or Redo command.
### Getting and localizing the menu item title
- [var undoMenuItemTitle: String](undomanager/undomenuitemtitle.md)
  The title of the Undo menu command, such as Undo Paste.
- [var redoMenuItemTitle: String](undomanager/redomenuitemtitle.md)
  The title of the Redo menu command, such as Redo Paste.
- [func undoMenuTitle(forUndoActionName: String) -> String](undomanager/undomenutitle(forundoactionname:).md)
  Returns the localized title of the Undo menu command for the identified action.
- [func redoMenuTitle(forUndoActionName: String) -> String](undomanager/redomenutitle(forundoactionname:).md)
  Returns the localized title of the Redo menu command for the identified action.
### Working with user info
- [func setActionUserInfoValue(Any?, forKey: UndoManager.UserInfoKey)](undomanager/setactionuserinfovalue(_:forkey:).md)
  Sets a user info value for an undo or redo action.
- [func undoActionUserInfoValue(forKey: UndoManager.UserInfoKey) -> Any?](undomanager/undoactionuserinfovalue(forkey:).md)
  Retrieves the undo action’s user info value for the given key.
- [func redoActionUserInfoValue(forKey: UndoManager.UserInfoKey) -> Any?](undomanager/redoactionuserinfovalue(forkey:).md)
  Retrieves the redo action’s user info value for the given key.
- [UndoManager.UserInfoKey](undomanager/userinfokey.md)
  An extensible namespace for undo and redo user info keys.
### Working with run loops
- [var runLoopModes: [RunLoop.Mode]](undomanager/runloopmodes.md)
  The modes governing the types of input to handle during a cycle of the run loop.
- [let NSUndoCloseGroupingRunLoopOrdering: Int](nsundoclosegroupingrunloopordering.md)
  A priority to use when using a run loop to close an undo group.
### Using discardable undo and redo actions
- [func setActionIsDiscardable(Bool)](undomanager/setactionisdiscardable(_:).md)
  Sets whether the next undo or redo action is discardable.
- [var undoActionIsDiscardable: Bool](undomanager/undoactionisdiscardable.md)
  A Boolean value that indicates whether the next undo action is discardable.
- [var redoActionIsDiscardable: Bool](undomanager/redoactionisdiscardable.md)
  A Boolean value that indicates whether the next redo action is discardable.
### Working with notifications
- [static let NSUndoManagerCheckpoint: NSNotification.Name](nsnotification/name-swift.struct/nsundomanagercheckpoint.md)
  Posted whenever an undo manager opens or closes an undo group (except when it opens a top-level group) and when checking the redo stack.
- [static let NSUndoManagerDidOpenUndoGroup: NSNotification.Name](nsnotification/name-swift.struct/nsundomanagerdidopenundogroup.md)
  Posted whenever an undo manager opens an undo group.
- [static let NSUndoManagerDidRedoChange: NSNotification.Name](nsnotification/name-swift.struct/nsundomanagerdidredochange.md)
  Posted just after an undo manager performs a redo operation.
- [static let NSUndoManagerDidUndoChange: NSNotification.Name](nsnotification/name-swift.struct/nsundomanagerdidundochange.md)
  Posted just after an undo manager performs an undo operation.
- [static let NSUndoManagerWillCloseUndoGroup: NSNotification.Name](nsnotification/name-swift.struct/nsundomanagerwillcloseundogroup.md)
  Posted before an undo manager closes an undo group.
- [static let NSUndoManagerDidCloseUndoGroup: NSNotification.Name](nsnotification/name-swift.struct/nsundomanagerdidcloseundogroup.md)
  Posted after an undo manager closes an undo group.
- [static let NSUndoManagerWillRedoChange: NSNotification.Name](nsnotification/name-swift.struct/nsundomanagerwillredochange.md)
  Posted just before an undo manager performs a redo operation.
- [static let NSUndoManagerWillUndoChange: NSNotification.Name](nsnotification/name-swift.struct/nsundomanagerwillundochange.md)
  Posted just before an undo manager performs an undo operation.
- [let NSUndoManagerGroupIsDiscardableKey: String](nsundomanagergroupisdiscardablekey.md)
  A key, used in a notification’s user info, that indicates the undo group contains only discardable actions.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/undomanager)*