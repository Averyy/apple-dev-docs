# USDPreviewSession.ChangeListDelegate

**Framework**: Spatial Preview  
**Kind**: protocol

Protocol to provide shared undo/redo tracking in a USDPreviewSession

**Availability**:
- macOS 27.0+ (Beta)
- visionOS ?+

## Declaration

```swift
@MainActor
protocol ChangeListDelegate : AnyObject
```

## Topics

### Instance Methods
- [func didApplyChanges(USDPreviewSession.Event)](usdpreviewsession/changelistdelegate/didapplychanges(_:).md)
- [func didApplyChanges(instanceIdentifier: String, operationIdentifier: UInt64)](usdpreviewsession/changelistdelegate/didapplychanges(instanceidentifier:operationidentifier:).md)
  Event emitted to the ChangelistDelegate indicating the end of a USD change
- [func onRedoRequest()](usdpreviewsession/changelistdelegate/onredorequest.md)
  An redo has been requested in the session
- [func onUndoRequest()](usdpreviewsession/changelistdelegate/onundorequest.md)
  An undo has been requested in the session
- [func willApplyChanges(USDPreviewSession.Event)](usdpreviewsession/changelistdelegate/willapplychanges(_:).md)
- [func willApplyChanges(instanceIdentifier: String, operationIdentifier: UInt64)](usdpreviewsession/changelistdelegate/willapplychanges(instanceidentifier:operationidentifier:).md)
  Event emitted to the ChangelistDelegate indicating the start of a USD change


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatialpreview/usdpreviewsession/changelistdelegate)*