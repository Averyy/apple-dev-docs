# openControllerHomeButtonSettingsForActivity:error:

**Framework**: Game Controller  
**Kind**: method  
**Role**: Instance Method

Opens the Settings app to the screen in game controller settings where the user can change the controller shortcut action.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+

## Declaration

```objc
- (BOOL) openControllerHomeButtonSettingsForActivity:(GCControllerHomeButtonSettingsCustomizationActivity) activity error:(NSError **) error;
```

#### Return Value

YES if the Settings app was opened, NO if it could not be opened and \p error contains additional information.  This function returns immediately after attempting to open the Settings app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gccontrollerhomebuttonsettingsmanager-10hl4/opencontrollerhomebuttonsettingsforactivity:error:)*