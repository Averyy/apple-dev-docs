# peerPickerController(_:didSelect:)

**Framework**: GameKit  
**Kind**: method  
**Role**: Instance Method

Tells the delegate that the user selected a connection type.

**Availability**:
- iOS 3.0+ - Deprecated in 7.0
- iPadOS 3.0+ - Deprecated in 7.0
- Mac Catalyst 3.0+ - Deprecated in 7.0
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: Use MCBrowserViewController along with MCBrowserViewControllerDelegate from the MultipeerConnectivity framework.

## Declaration

```swift
optional func peerPickerController(_ picker: GKPeerPickerController, didSelect type: GKPeerPickerConnectionType)
```

```objc
- (void) peerPickerController:(GKPeerPickerController *) picker didSelectConnectionType:(GKPeerPickerConnectionType) type;
```

#### Discussion

If the peer picker is configured to allow users to choose between multiple connection types, this method is called when users select the connection type they want to use. Your delegate implements this method if you want to override the behavior for a particular connection type.

> ❗ **Important**:  In iOS 3.0, the peer picker can configure Bluetooth connections ([`GKPeerPickerConnectionType.nearby`](../gkpeerpickerconnectiontype/nearby.md)). If the user chooses an Internet connection ([`GKPeerPickerConnectionType.online`](../gkpeerpickerconnectiontype/online.md)), your delegate should dismiss the dialog and present its own user interface to configure the Internet connection:

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

### Creating a Session for the Peer Picker
- [func peerPickerController(GKPeerPickerController, sessionFor: GKPeerPickerConnectionType) -> GKSession](./peerpickercontroller%28_,sessionfor%29.md)
  Asks the delegate to return a session for the specified connection type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkpeerpickercontrollerdelegate/peerpickercontroller(_:didselect:))*