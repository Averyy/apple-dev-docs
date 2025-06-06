# activateIgnoringOtherApps

**Framework**: AppKit  
**Kind**: property

The application is activated regardless of the currently active app.

**Availability**:
- macOS 10.6+

## Declaration

```swift
static var activateIgnoringOtherApps: NSApplication.ActivationOptions { get }
```

#### Discussion

By default, activation deactivates the calling app (assuming it was active), and then the new app is activated only if there’s no currently active application. This prevents the new app from stealing focus from the user, if the app is slow to activate and the user has switched to a different app in the interim. However, if you specify [`activateIgnoringOtherApps`](nsapplication/activationoptions/activateignoringotherapps.md), the application is activated regardless of the currently active app, potentially stealing focus from the user.

> ❗ **Important**:  You should  because stealing key focus produces a poor user experience.

 You should  because stealing key focus produces a poor user experience.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplication/activationoptions/activateignoringotherapps)*