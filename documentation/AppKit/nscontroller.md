# NSController

**Framework**: AppKit  
**Kind**: class

An abstract class that implements the [`NSEditor`](nseditor.md) and [`NSEditorRegistration`](nseditorregistration.md) informal protocols required for controller classes.

**Availability**:
- macOS ?+

## Declaration

```swift
class NSController
```

## Topics

### Managing editing
- [func objectDidBeginEditing(any NSEditor)](nscontroller/objectdidbeginediting(_:).md)
  Invoked to inform the receiver that `editor` has uncommitted changes that can affect the receiver.
- [func objectDidEndEditing(any NSEditor)](nscontroller/objectdidendediting(_:).md)
  Invoked to inform the receiver that `editor` has committed or discarded its changes.
- [func commitEditing() -> Bool](nscontroller/commitediting.md)
  Attempts to commit any pending edits.
- [func commitEditing(withDelegate: Any?, didCommit: Selector?, contextInfo: UnsafeMutableRawPointer?)](nscontroller/commitediting(withdelegate:didcommit:contextinfo:).md)
  Attempts to commit any pending changes in known editors of the receiver.
- [func discardEditing()](nscontroller/discardediting.md)
  Discards any pending changes by registered editors.
- [var isEditing: Bool](nscontroller/isediting.md)
  A Boolean value indicating if any editors are registered with the controller.
### Initializers
- [init()](nscontroller/init.md)
- [init?(coder: NSCoder)](nscontroller/init(coder:).md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [NSObjectController](nsobjectcontroller.md)
- [NSUserDefaultsController](nsuserdefaultscontroller.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSEditor](nseditor.md)
- [NSEditorRegistration](nseditorregistration.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class NSObjectController](nsobjectcontroller.md)
  A controller that can manage an object’s properties referenced by key-value paths.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscontroller)*