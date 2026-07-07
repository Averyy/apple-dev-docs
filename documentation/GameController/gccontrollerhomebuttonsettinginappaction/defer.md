# GCControllerHomeButtonSettingInAppAction.defer

**Framework**: Game Controller  
**Kind**: case

The system defers its handling to your app’s preference.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
case `defer`
```

#### Discussion

The system reponse to the game controller Home button press is disabled when the app indicates that it wants to handle the Home button press.  The app indicates that it wants to handle the Home button press by setting:

```None
controller.physicalInputProfile.buttons[GCInputButtonHome].preferredSystemGestureState = GCSystemGestureStateDisabled;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gccontrollerhomebuttonsettinginappaction/defer)*