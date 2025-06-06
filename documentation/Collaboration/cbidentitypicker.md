# CBIdentityPicker

**Framework**: Collaboration  
**Kind**: class

A `CBIdentityPicker` object allows a user to select identities—for example, user or group objects—that it wants one or more services or shared resources to have access to. An identity picker can be displayed either as an application-modal dialog or as a sheet attached to a document window. An identity picker returns the selected records to be added to access control lists using Collaboration. If a selected record is not a user or group identity, then an identity picker prompts the user for additional information—such as a password—to promote that record to a sharing account.

**Availability**:
- macOS 10.5+

## Declaration

```swift
class CBIdentityPicker
```

## Topics

### Running an Identity Picker
- [func runModal(for: NSWindow, modalDelegate: Any?, didEnd: Selector?, contextInfo: UnsafeMutableRawPointer?)](cbidentitypicker/runmodal(for:modaldelegate:didend:contextinfo:).md)
  Runs the receiver modally as a sheet attached to a specified window.
- [func runModal(for: NSWindow, completionHandler: ((NSApplication.ModalResponse) -> Void)?)](cbidentitypicker/runmodal(for:completionhandler:).md)
  Runs the identity picker modally as a sheet attached to a specified window.
- [func runModal() -> Int](cbidentitypicker/runmodal.md)
  Runs the receiver as an application-modal dialog.
### Retrieving Identities
- [var identities: [CBIdentity]](cbidentitypicker/identities.md)
  The array of identities (represented by `CBIdentity` objects) selected using the identity picker.
### Setting and Getting Properties
- [var title: String?](cbidentitypicker/title.md)
  The title of the identity picker.
- [var allowsMultipleSelection: Bool](cbidentitypicker/allowsmultipleselection.md)
  A Boolean value indicating whether the user is allowed to select multiple identities.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/collaboration/cbidentitypicker)*