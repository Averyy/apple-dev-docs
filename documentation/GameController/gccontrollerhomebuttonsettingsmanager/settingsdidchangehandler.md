# settingsDidChangeHandler

**Framework**: Game Controller  
**Kind**: property

A block that is called after shortcut settings change.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
var settingsDidChangeHandler: (() -> Void)? { get set }
```

#### Discussion

This block is called on the queue that the `GCControllerHomeButtonSettingsManager` was initialized with.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gccontrollerhomebuttonsettingsmanager/settingsdidchangehandler)*