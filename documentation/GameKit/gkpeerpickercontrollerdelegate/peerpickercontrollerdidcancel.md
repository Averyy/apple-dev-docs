# peerPickerControllerDidCancel(_:)

**Framework**: GameKit  
**Kind**: method

Tells the delegate that the user canceled the connection attempt.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
optional func peerPickerControllerDidCancel(_ picker: GKPeerPickerController)
```

#### Discussion

After this method returns, the controller dismisses the picker interface.

> ❗ **Important**:  Although optional in the protocol, Game Kit expects your application to implement this method.

 Although optional in the protocol, Game Kit expects your application to implement this method.

## Parameters

- `picker`: The controller for the peer picker dialog.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkpeerpickercontrollerdelegate/peerpickercontrollerdidcancel(_:))*