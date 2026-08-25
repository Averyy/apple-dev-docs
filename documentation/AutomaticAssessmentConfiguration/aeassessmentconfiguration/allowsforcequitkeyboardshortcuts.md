# allowsForceQuitKeyboardShortcuts

**Framework**: Automatic Assessment Configuration  
**Kind**: property

A Boolean value that indicates whether to allow force quitting apps during an assessment.

**Availability**:
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)

## Declaration

```swift
var allowsForceQuitKeyboardShortcuts: Bool { get set }
```

#### Discussion

Users can force quit apps by pressing Shift-Option-Command-Escape to force quit the frontmost app. An assessment session disables force quit by default, but you can allow it by setting [`allowsForceQuitKeyboardShortcuts`](aeassessmentconfiguration/allowsforcequitkeyboardshortcuts.md) to `true` in the [`AEAssessmentConfiguration`](aeassessmentconfiguration.md) instance that you use to initialize a session.

> **Note**: This property controls only the force quit keyboard shortcuts. Setting it to `false` does not remove the Force Quit item from the Apple menu. Use [`allowedAppleMenuItems`](aeassessmentconfiguration/allowedapplemenuitems.md) to configure the allowed Apple menu items.


---

*[View on Apple Developer](https://developer.apple.com/documentation/automaticassessmentconfiguration/aeassessmentconfiguration/allowsforcequitkeyboardshortcuts)*