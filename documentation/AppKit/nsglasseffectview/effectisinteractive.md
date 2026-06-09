# effectIsInteractive

**Framework**: AppKit  
**Kind**: property

Enables interactive glass behavior, which adds a visual response to user interactions.

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
var effectIsInteractive: Bool { get set }
```

#### Discussion

This should be enabled for glass that is used as the background for interactive controls or when used as the container of interactive controls.

When `YES`, the glass effect will provide visual feedback when it is interacted with. When `NO`, the glass effect remains static. The default value is `NO`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsglasseffectview/effectisinteractive)*