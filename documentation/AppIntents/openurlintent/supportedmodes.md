# supportedModes

**Framework**: App Intents  
**Kind**: property

Defines the supported modes that describe the behavior of your app intent.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
static var supportedModes: IntentModes { get }
```

#### Discussion

The suppprted modes determine whether the intent performs its action in the background, the foreground, or a combination of both. Available modes include:

Additionally, you can set `supportedModes` to a combination of background and foreground modes:

When handling both background and foreground modes you can consult `SystemContext`’s `SystemContext/currentMode` property within your [`perform()`](appintent/perform().md) implementation to determine the active mode and decide whether foregrounding your app is appropriate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/openurlintent/supportedmodes)*