# SetWantsControlsRestored

**Framework**: AudioDriverKit  
**Kind**: method

**Availability**:
- DriverKit 21.0+

## Declaration

```swift
void SetWantsControlsRestored(bool in_wants_controls_restored);
```

#### Discussion

Setter on the device object that tells the host that the controls for the device should or should not be saved/restored when the device is first published. If the device doesn’t implement this property, it is assumed that the settings should be saved and restored. Note that this should be set before the device is published to the host

## Parameters

- `in_wants_controls_restored`: Bool value indicating if the host should or should not restore control settings for the device   A value of false indicates that the controls for the device should NOT be saved/restored   A value of true indicated that the controls for the device should be saved/restored


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiodriverkit/iouseraudioclockdevice/setwantscontrolsrestored)*