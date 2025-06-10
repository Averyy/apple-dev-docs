# NSEditor

**Framework**: AppKit  
**Kind**: protocol

**Availability**:
- macOS ?+

## Declaration

```swift
protocol NSEditor : NSObjectProtocol
```

## Topics

### Instance Methods
- [func commitEditing() -> Bool](nseditor/commitediting.md)
- [func commitEditing(withDelegate: Any?, didCommit: Selector?, contextInfo: UnsafeMutableRawPointer?)](nseditor/commitediting(withdelegate:didcommit:contextinfo:).md)
- [func commitEditingWithoutPresentingError() throws](nseditor/commiteditingwithoutpresentingerror.md)
- [func discardEditing()](nseditor/discardediting.md)

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
### Conforming Types
- [NSArrayController](nsarraycontroller.md)
- [NSCollectionViewItem](nscollectionviewitem.md)
- [NSController](nscontroller.md)
- [NSDictionaryController](nsdictionarycontroller.md)
- [NSObjectController](nsobjectcontroller.md)
- [NSPageController](nspagecontroller.md)
- [NSSplitViewController](nssplitviewcontroller.md)
- [NSSplitViewItemAccessoryViewController](nssplitviewitemaccessoryviewcontroller.md)
- [NSTabViewController](nstabviewcontroller.md)
- [NSTitlebarAccessoryViewController](nstitlebaraccessoryviewcontroller.md)
- [NSTreeController](nstreecontroller.md)
- [NSUserDefaultsController](nsuserdefaultscontroller.md)
- [NSViewController](nsviewcontroller.md)

## See Also

- [protocol NSEditorRegistration](nseditorregistration.md)
  A set of methods that controllers can implement to enable an editor view to inform the controller when it has uncommitted changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nseditor)*