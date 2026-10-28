# NSEditorRegistration

**Framework**: AppKit  
**Kind**: protocol  
**Role**: Protocol

A set of methods that controllers can implement to enable an editor view to inform the controller when it has uncommitted changes.

**Availability**:
- macOS

## Declaration

```swift
protocol NSEditorRegistration : NSObjectProtocol
```

```objc
@protocol NSEditorRegistration <NSObject>
```

## Overview

An implementor is responsible for tracking which editors have uncommitted changes, and sending those editors [`commitEditing`](../ObjectiveC/nsobject-swift.class/commitediting.md) and [`discardEditing`](../ObjectiveC/nsobject-swift.class/discardediting.md) messages, as appropriate, to force the editor to submit, or discard, their values.

[`NSController`](./nscontroller.md) provides an implementation of this informal protocol. You would implement this protocol if you wanted to provide your own controller class without subclassing [`NSController`](./nscontroller.md).

## Topics

### Instance Methods
- [func objectDidBeginEditing(any NSEditor)](./nseditorregistration/objectdidbeginediting%28_%29.md)
- [func objectDidEndEditing(any NSEditor)](./nseditorregistration/objectdidendediting%28_%29.md)

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
### Conforming Types
- [NSArrayController](./nsarraycontroller.md)
- [NSController](./nscontroller.md)
- [NSDictionaryController](./nsdictionarycontroller.md)
- [NSDocument](./nsdocument.md)
- [NSObjectController](./nsobjectcontroller.md)
- [NSPersistentDocument](./nspersistentdocument.md)
- [NSTreeController](./nstreecontroller.md)
- [NSUserDefaultsController](./nsuserdefaultscontroller.md)

## See Also

### Deprecated protocols
- [NSAccessibility](./nsaccessibility.md)
  A legacy, informal protocol that Apple doesn’t recommend for active use.
- [protocol NSInputServiceProvider](./nsinputserviceprovider.md)
- [protocol NSInputServerMouseTracker](./nsinputservermousetracker.md)
- [protocol NSDrawerDelegate](./nsdrawerdelegate.md)
  A set of methods that drawer delegates implement to open, close, and resize the drawer.
- [NSEditor](./nseditor-deprecated-symbols.md)
  A set of methods that controllers and UI elements can implement to manage editing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nseditorregistration)*