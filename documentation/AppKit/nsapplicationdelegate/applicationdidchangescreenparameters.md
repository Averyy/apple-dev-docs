# applicationDidChangeScreenParameters(_:)

**Framework**: AppKit  
**Kind**: method

Tells the delegate about changes to the configuration of any attached displays.

**Availability**:
- macOS 10.10+

## Declaration

```swift
@MainActor
optional func applicationDidChangeScreenParameters(_ notification: Notification)
```

## Parameters

- `notification`: A notification named [`didChangeScreenParametersNotification`](nsapplication/didchangescreenparametersnotification.md). Calling the [`object`](https://developer.apple.com/documentation/foundation/nsnotification/object) method of this notification returns the `NSApplication` object itself.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplicationdelegate/applicationdidchangescreenparameters(_:))*