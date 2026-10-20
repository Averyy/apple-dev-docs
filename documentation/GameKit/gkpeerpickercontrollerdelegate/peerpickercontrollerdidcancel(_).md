# peerPickerControllerDidCancel(_:)

**Framework**: GameKit  
**Kind**: method  
**Role**: Instance Method

Tells the delegate that the user canceled the connection attempt.

**Availability**:
- iOS 3.0+ - Deprecated in 7.0
- iPadOS 3.0+ - Deprecated in 7.0
- Mac Catalyst 3.0+ - Deprecated in 7.0
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: Use MCBrowserViewController along with MCBrowserViewControllerDelegate from the MultipeerConnectivity framework.

## Declaration

```swift
optional func peerPickerControllerDidCancel(_ picker: GKPeerPickerController)
```

```objc
- (void) peerPickerControllerDidCancel:(GKPeerPickerController *) picker;
```

#### Discussion

After this method returns, the controller dismisses the picker interface.

> ❗ **Important**:  Although optional in the protocol, Game Kit expects your application to implement this method.

## Parameters

- `picker`: The controller for the peer picker dialog.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkpeerpickercontrollerdelegate/peerpickercontrollerdidcancel(_:))*