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

> **Note**: Performing operations on `GCControllerHomeButtonSettingsManager` is only permitted while a game controller is connected.

## Topics

### Initializers
- [init?()](gccontrollerhomebuttonsettingsmanager/init.md)
- [init?(queue: dispatch_queue_t?)](gccontrollerhomebuttonsettingsmanager/init(queue:).md)
### Instance Properties
- [var settingsDidChangeHandler: (() -> Void)?](gccontrollerhomebuttonsettingsmanager/settingsdidchangehandler.md)
  A block that is called after shortcut settings change.
### Instance Methods
- [func openControllerHomeButtonSettings(for: GCControllerHomeButtonSettingsManager.Activity) throws](gccontrollerhomebuttonsettingsmanager/opencontrollerhomebuttonsettings(for:).md)
  Opens the Settings app to the screen in game controller settings where the user can change the controller shortcut action.
- [func readControllerHomeButtonAction() throws -> GCControllerHomeButtonSettingsManager.Action](gccontrollerhomebuttonsettingsmanager/readcontrollerhomebuttonaction.md)
  Get the current controller Home button action.
### Enumerations
- [GCControllerHomeButtonSettingsManager.Action](gccontrollerhomebuttonsettingsmanager/action.md)
- [GCControllerHomeButtonSettingsManager.Activity](gccontrollerhomebuttonsettingsmanager/activity.md)
  A hint passed to `-openControllerHomeButtonSettingsForActivity:` that indicates the reason the app is requesting to open the Home button settings.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gccontrollerhomebuttonsettingsmanager)*