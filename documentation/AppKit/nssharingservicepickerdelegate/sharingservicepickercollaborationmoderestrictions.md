# sharingServicePickerCollaborationModeRestrictions(_:)

**Framework**: AppKit  
**Kind**: method

Used to specify the case where the share picker should not support some modes of sharing even if they are supported by the items being shared. Disabling all possible modes at the same time is not supported behavior.

**Availability**:
- macOS 15.0+

## Declaration

```swift
optional func sharingServicePickerCollaborationModeRestrictions(_ sharingServicePicker: NSSharingServicePicker) -> [NSSharingServicePicker.CollaborationModeRestriction]?
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssharingservicepickerdelegate/sharingservicepickercollaborationmoderestrictions(_:))*