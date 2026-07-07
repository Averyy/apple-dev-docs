# USDPreviewSession.ChangeListDelegate

**Framework**: Spatial Preview  
**Kind**: protocol

A protocol to provide shared undo/redo tracking in a USDPreviewSession.

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
- [func didApplyChanges(instanceIdentifier: String, operationIdentifier: UInt)](usdpreviewsession/changelistdelegate/didapplychanges(instanceidentifier:operationidentifier:).md)
  An event emitted to the ChangelistDelegate indicating the end of a USD change.
- [func onRedoRequest()](usdpreviewsession/changelistdelegate/onredorequest.md)
  An redo has been requested in the session
- [func onUndoRequest()](usdpreviewsession/changelistdelegate/onundorequest.md)
  An undo has been requested in the session
- [func willApplyChanges(instanceIdentifier: String, operationIdentifier: UInt)](usdpreviewsession/changelistdelegate/willapplychanges(instanceidentifier:operationidentifier:).md)
  An event emitted to the ChangeListDelegate indicating the start of a USD change.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatialpreview/usdpreviewsession/changelistdelegate)*