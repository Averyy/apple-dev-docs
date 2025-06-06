# setActionIsDiscardable(_:)

**Framework**: Foundation  
**Kind**: method

Sets whether the next undo or redo action is discardable.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func setActionIsDiscardable(_ discardable: Bool)
```

#### Discussion

Specifies that the latest undo action may be safely discarded when a document can not be saved for any reason.

An example might be an undo action that changes the viewable area of a document.

To find out if an undo group contains only discardable actions, look for the `NSUndoManagerGroupIsDiscardableKey` in the [`userInfo`](nsnotification/userinfo.md) dictionary of the [`NSUndoManagerWillCloseUndoGroup`](nsnotification/name-swift.struct/nsundomanagerwillcloseundogroup.md).

## Parameters

- `discardable`: Specifies if the action is discardable.   if the next undo or redo action can be discarded;   otherwise.

## See Also

- [var undoActionIsDiscardable: Bool](undomanager/undoactionisdiscardable.md)
  A Boolean value that indicates whether the next undo action is discardable.
- [var redoActionIsDiscardable: Bool](undomanager/redoactionisdiscardable.md)
  A Boolean value that indicates whether the next redo action is discardable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/undomanager/setactionisdiscardable(_:))*