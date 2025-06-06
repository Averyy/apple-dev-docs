# connectionTypesMask

**Framework**: GameKit  
**Kind**: property

A mask that determines the types of connections a dialog presents to the user.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
var connectionTypesMask: GKPeerPickerConnectionType { get set }
```

#### Discussion

Your application configures the connection types it allows before showing the peer picker. If your application allows more than one connection type, the peer picker offers the user a choice of which type of connection to use. The default value for the mask is [`GKPeerPickerConnectionType.nearby`](gkpeerpickerconnectiontype/nearby.md).

> ❗ **Important**:  In iOS 3.0, [`GKPeerPickerConnectionType.nearby`](gkpeerpickerconnectiontype/nearby.md) is required to be one of the allowed connection types. An exception is thrown if your application does not include it.

 In iOS 3.0, [`GKPeerPickerConnectionType.nearby`](gkpeerpickerconnectiontype/nearby.md) is required to be one of the allowed connection types. An exception is thrown if your application does not include it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkpeerpickercontroller/connectiontypesmask)*