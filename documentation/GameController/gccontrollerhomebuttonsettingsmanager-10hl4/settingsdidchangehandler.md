# settingsDidChangeHandler

**Framework**: Game Controller  
**Kind**: property  
**Role**: Instance Property

A block that is scheduled after Home button settings change.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+

## Declaration

```objc
@property (atomic, copy, nullable) GCControllerHomeButtonSettingsDidChangeHandler settingsDidChangeHandler;
```

#### Discussion

This block is scheduled on the `queue` the `GCControllerHomeButtonSettingsManager` was initialized with.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gccontrollerhomebuttonsettingsmanager-10hl4/settingsdidchangehandler)*