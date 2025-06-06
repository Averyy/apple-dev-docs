# setupPanelDeviceSelectionChanged(_:)

**Framework**: Objective-C Runtime  
**Kind**: method

Sent by the default notification center when the device selection in the panel has changed.

**Availability**:
- macOS ?+

## Declaration

```swift
func setupPanelDeviceSelectionChanged(_ aNotification: Notification!)
```

#### Discussion

You can retrieve the `DRSetupPanel` object in question by sending `NSNotification` object to `aNotification`. The userInfo dictionary contains the single key DRSetupPanelSelectedDeviceKey whose value is the `DRDevice` object that is currently selected.

## Parameters

- `aNotification`: Notification object. This is always  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/setuppaneldeviceselectionchanged(_:))*