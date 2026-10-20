# NSController

**Framework**: AppKit  
**Kind**: class  
**Role**: Class

An abstract class that implements the [`NSEditor`](./nseditor.md) and [`NSEditorRegistration`](./nseditorregistration.md) informal protocols required for controller classes.

**Availability**:
- macOS

## Declaration

```swift
class NSController
```

```objc
@interface NSController : NSObject
```

## Topics

### Managing editing
- [func objectDidBeginEditing(any NSEditor)](./nscontroller/objectdidbeginediting%28_%29.md)
  Invoked to inform the receiver that `editor` has uncommitted changes that can affect the receiver.
- [func objectDidEndEditing(any NSEditor)](./nscontroller/objectdidendediting%28_%29.md)
  Invoked to inform the receiver that `editor` has committed or discarded its changes.
- [func commitEditing() -> Bool](./nscontroller/commitediting%28%29.md)
  Attempts to commit any pending edits.
- [func commitEditing(withDelegate: Any?, didCommit: Selector?, contextInfo: UnsafeMutableRawPointer?)](./nscontroller/commitediting%28withdelegate,didcommit,contextinfo%29.md)
  Attempts to commit any pending changes in known editors of the receiver.
- [func discardEditing()](./nscontroller/discardediting%28%29.md)
  Discards any pending changes by registered editors.
- [var isEditing: Bool](./nscontroller/isediting.md)
  A Boolean value indicating if any editors are registered with the controller.
### Initializers
- [init()](./nscontroller/init%28%29.md)
- [init?(coder: NSCoder)](./nscontroller/init%28coder%29.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Inherited By
- [NSObjectController](./nsobjectcontroller.md)
- [NSUserDefaultsController](./nsuserdefaultscontroller.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSEditor](./nseditor.md)
- [NSEditorRegistration](./nseditorregistration.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Core Controllers
- [class NSObjectController](./nsobjectcontroller.md)
  A controller that can manage an object’s properties referenced by key-value paths.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscontroller)*