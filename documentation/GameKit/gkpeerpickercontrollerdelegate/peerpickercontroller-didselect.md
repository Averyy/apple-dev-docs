# peerPickerController(_:didSelect:)

**Framework**: GameKit  
**Kind**: method

Tells the delegate that the user selected a connection type.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
optional func peerPickerController(_ picker: GKPeerPickerController, didSelect type: GKPeerPickerConnectionType)
```

#### Discussion

If the peer picker is configured to allow users to choose between multiple connection types, this method is called when users select the connection type they want to use. Your delegate implements this method if you want to override the behavior for a particular connection type.

> ❗ **Important**:  In iOS 3.0, the peer picker can configure Bluetooth connections ([`GKPeerPickerConnectionType.nearby`](gkpeerpickerconnectiontype/nearby.md)). If the user chooses an Internet connection ([`GKPeerPickerConnectionType.online`](gkpeerpickerconnectiontype/online.md)), your delegate should dismiss the dialog and present its own user interface to configure the Internet connection:

 In iOS 3.0, the peer picker can configure Bluetooth connections ([`GKPeerPickerConnectionType.nearby`](gkpeerpickerconnectiontype/nearby.md)). If the user chooses an Internet connection ([`GKPeerPickerConnectionType.online`](gkpeerpickerconnectiontype/online.md)), your delegate should dismiss the dialog and present its own user interface to configure the Internet connection:

```objc
- (void)peerPickerController:(GKPeerPickerController *)picker didSelectConnectionType:(GKPeerPickerConnectionType)type {
    if(type == GKPeerPickerConnectionTypeOnline) {
        [picker dismiss];
        [picker autorelease];
// Display your own user interface here.
}
```

## Parameters

- `picker`: The controller for the peer picker dialog.
- `type`: The type of network connection chosen by the user.

## See Also

- [func peerPickerController(GKPeerPickerController, sessionFor: GKPeerPickerConnectionType) -> GKSession](gkpeerpickercontrollerdelegate/peerpickercontroller(_:sessionfor:).md)
  Asks the delegate to return a session for the specified connection type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkpeerpickercontrollerdelegate/peerpickercontroller(_:didselect:))*