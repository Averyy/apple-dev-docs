# GCControllerHomeButtonSettingsManager

**Framework**: Game Controller  
**Kind**: class

Access the game controller system Home button settings.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
class GCControllerHomeButtonSettingsManager
```

#### Overview

macOS, iOS, and visionOS allow the user to assign an action that launches a chosen application to a long press of the Home button (the logo button on PlayStation and Xbox controllers).  The \c GCControllerHomeButtonSettingsManager class allows your application to partially inspect the user’s currently configured action, and to open the system game controller settings screen where the user can modify the action.

Performing operations on `GCControllerHomeButtonSettingsManager` is only permitted while a game controller is connected.

## Topics

### Initializers
- [init()](gccontrollerhomebuttonsettingsmanager-258mu/init.md)
- [init(isolated any Actor)](gccontrollerhomebuttonsettingsmanager-258mu/init(_:).md)
### Instance Properties
- [var controllerHomeButtonInAppAction: (action: GCControllerHomeButtonSettingsManager.InAppAction, customized: GCControllerHomeButtonSettingsManager.SettingCustomizationStatus)](gccontrollerhomebuttonsettingsmanager-258mu/controllerhomebuttoninappaction.md)
  Get the current controller Home button in-app action setting.
- [var controllerHomeButtonSystemAction: (action: GCControllerHomeButtonSettingsManager.SystemAction, customized: GCControllerHomeButtonSettingsManager.SettingCustomizationStatus)](gccontrollerhomebuttonsettingsmanager-258mu/controllerhomebuttonsystemaction.md)
  Get the current controller Home button system action setting.
- [var settingsUpdates: some AsyncSequence<(), Never>](gccontrollerhomebuttonsettingsmanager-258mu/settingsupdates.md)
  The asynchronous sequence of update notifications for the Home button settings.
### Instance Methods
- [func openControllerHomeButtonSettings(for: GCControllerHomeButtonSettingsManager.SettingsCustomizationActivity) throws](gccontrollerhomebuttonsettingsmanager-258mu/opencontrollerhomebuttonsettings(for:).md)
  Opens the Settings app to the screen in game controller settings where the user can change the controller shortcut action.
### Type Aliases
- [GCControllerHomeButtonSettingsManager.InAppAction](gccontrollerhomebuttonsettingsmanager-258mu/inappaction.md)
- [GCControllerHomeButtonSettingsManager.SettingCustomizationStatus](gccontrollerhomebuttonsettingsmanager-258mu/settingcustomizationstatus.md)
- [GCControllerHomeButtonSettingsManager.SettingsCustomizationActivity](gccontrollerhomebuttonsettingsmanager-258mu/settingscustomizationactivity.md)
- [GCControllerHomeButtonSettingsManager.SystemAction](gccontrollerhomebuttonsettingsmanager-258mu/systemaction.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gccontrollerhomebuttonsettingsmanager-258mu)*