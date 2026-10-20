# USDPreviewSession.ChangeListDelegate

**Framework**: Spatial Preview  
**Kind**: protocol  
**Role**: Protocol

A protocol to provide shared undo/redo tracking in a USDPreviewSession.

**Availability**:
- macOS 27.0+
- visionOS

## Declaration

```swift
@MainActor
protocol ChangeListDelegate : AnyObject
```

## Topics

### Responding to changes
- [func willApplyChanges(instanceIdentifier: String, operationIdentifier: UInt)](./changelistdelegate/willapplychanges%28instanceidentifier,operationidentifier%29.md)
  An event emitted to the ChangeListDelegate indicating the start of a USD change.
- [func didApplyChanges(instanceIdentifier: String, operationIdentifier: UInt)](./changelistdelegate/didapplychanges%28instanceidentifier,operationidentifier%29.md)
  An event emitted to the ChangelistDelegate indicating the end of a USD change.
### Handling undo and redo
- [func onUndoRequest()](./changelistdelegate/onundorequest%28%29.md)
  An undo has been requested in the session
- [func onRedoRequest()](./changelistdelegate/onredorequest%28%29.md)
  An redo has been requested in the session
### Deprecated
- [func didApplyChanges(USDPreviewSession.Event)](./changelistdelegate/didapplychanges%28_%29.md)
- [func willApplyChanges(USDPreviewSession.Event)](./changelistdelegate/willapplychanges%28_%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatialpreview/usdpreviewsession/changelistdelegate)*