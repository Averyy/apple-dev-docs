# openControllerHomeButtonSettings(for:)

**Framework**: Game Controller  
**Kind**: method

Opens the Settings app to the screen in game controller settings where the user can change the controller shortcut action.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+

## Declaration

```swift
func openControllerHomeButtonSettings(for activity: GCControllerHomeButtonSettingsManager.SettingsCustomizationActivity) throws
```

#### Discussion

This function returns immediately after attempting to open the Settings app.

> **Note**: An error if the Settings app could not be opened.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gccontrollerhomebuttonsettingsmanager-258mu/opencontrollerhomebuttonsettings(for:))*