# NSEditorRegistration

**Framework**: AppKit  
**Kind**: protocol

A set of methods that controllers can implement to enable an editor view to inform the controller when it has uncommitted changes.

**Availability**:
- macOS ?+

## Declaration

```swift
protocol NSEditorRegistration : NSObjectProtocol
```

#### Overview

An implementor is responsible for tracking which editors have uncommitted changes, and sending those editors [`commitEditing`](https://developer.apple.com/documentation/ObjectiveC/NSObject-swift.class/commitEditing) and [`discardEditing`](https://developer.apple.com/documentation/ObjectiveC/NSObject-swift.class/discardEditing) messages, as appropriate, to force the editor to submit, or discard, their values.

[`NSController`](nscontroller.md) provides an implementation of this informal protocol. You would implement this protocol if you wanted to provide your own controller class without subclassing [`NSController`](nscontroller.md).

## Topics

### Instance Methods
- [func objectDidBeginEditing(any NSEditor)](nseditorregistration/objectdidbeginediting(_:).md)
- [func objectDidEndEditing(any NSEditor)](nseditorregistration/objectdidendediting(_:).md)

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
### Conforming Types
- [NSArrayController](nsarraycontroller.md)
- [NSController](nscontroller.md)
- [NSDictionaryController](nsdictionarycontroller.md)
- [NSDocument](nsdocument.md)
- [NSObjectController](nsobjectcontroller.md)
- [NSPersistentDocument](nspersistentdocument.md)
- [NSTreeController](nstreecontroller.md)
- [NSUserDefaultsController](nsuserdefaultscontroller.md)

## See Also

- [NSAccessibility](nsaccessibility.md)
  A legacy, informal protocol that Apple doesn’t recommend for active use.
- [protocol NSInputServiceProvider](nsinputserviceprovider.md)
- [protocol NSInputServerMouseTracker](nsinputservermousetracker.md)
- [protocol NSDrawerDelegate](nsdrawerdelegate.md)
  A set of methods that drawer delegates implement to open, close, and resize the drawer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nseditorregistration)*