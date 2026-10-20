# NSEditor

**Framework**: AppKit  
**Kind**: protocol  
**Role**: Protocol

**Availability**:
- macOS

## Declaration

```swift
protocol NSEditor : NSObjectProtocol
```

```objc
@protocol NSEditor <NSObject>
```

## Topics

### Instance Methods
- [func commitEditing() -> Bool](./nseditor/commitediting%28%29.md)
- [func commitEditing(withDelegate: Any?, didCommit: Selector?, contextInfo: UnsafeMutableRawPointer?)](./nseditor/commitediting%28withdelegate,didcommit,contextinfo%29.md)
- [func commitEditingWithoutPresentingError() throws](./nseditor/commiteditingwithoutpresentingerror%28%29.md)
- [func discardEditing()](./nseditor/discardediting%28%29.md)

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
### Conforming Types
- [NSArrayController](./nsarraycontroller.md)
- [NSCollectionViewItem](./nscollectionviewitem.md)
- [NSController](./nscontroller.md)
- [NSDictionaryController](./nsdictionarycontroller.md)
- [NSObjectController](./nsobjectcontroller.md)
- [NSPageController](./nspagecontroller.md)
- [NSSplitViewController](./nssplitviewcontroller.md)
- [NSSplitViewItemAccessoryViewController](./nssplitviewitemaccessoryviewcontroller.md)
- [NSTabViewController](./nstabviewcontroller.md)
- [NSTitlebarAccessoryViewController](./nstitlebaraccessoryviewcontroller.md)
- [NSTreeController](./nstreecontroller.md)
- [NSUserDefaultsController](./nsuserdefaultscontroller.md)
- [NSViewController](./nsviewcontroller.md)

## See Also

### Object Editing
- [protocol NSEditorRegistration](./nseditorregistration.md)
  A set of methods that controllers can implement to enable an editor view to inform the controller when it has uncommitted changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nseditor)*