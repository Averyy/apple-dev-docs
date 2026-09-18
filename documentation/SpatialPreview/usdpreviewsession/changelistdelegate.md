# USDPreviewSession.ChangeListDelegate

**Framework**: Spatial Preview  
**Kind**: protocol

A protocol to provide shared undo/redo tracking in a USDPreviewSession.

**Availability**:
- macOS 27.0+
- visionOS ?+

## Declaration

```swift
@MainActor
protocol ChangeListDelegate : AnyObject
```

## Topics

### Responding to changes
- [func willApplyChanges(instanceIdentifier: String, operationIdentifier: UInt)](usdpreviewsession/changelistdelegate/willapplychanges(instanceidentifier:operationidentifier:).md)
  An event emitted to the ChangeListDelegate indicating the start of a USD change.
- [func didApplyChanges(instanceIdentifier: String, operationIdentifier: UInt)](usdpreviewsession/changelistdelegate/didapplychanges(instanceidentifier:operationidentifier:).md)
  An event emitted to the ChangelistDelegate indicating the end of a USD change.
### Handling undo and redo
- [func onUndoRequest()](usdpreviewsession/changelistdelegate/onundorequest.md)
  An undo has been requested in the session
- [func onRedoRequest()](usdpreviewsession/changelistdelegate/onredorequest.md)
  An redo has been requested in the session
### Deprecated
- [func didApplyChanges(USDPreviewSession.Event)](usdpreviewsession/changelistdelegate/didapplychanges(_:).md)
- [func willApplyChanges(USDPreviewSession.Event)](usdpreviewsession/changelistdelegate/willapplychanges(_:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatialpreview/usdpreviewsession/changelistdelegate)*