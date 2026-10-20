# applicationDidChangeScreenParameters(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Tells the delegate about changes to the configuration of any attached displays.

**Availability**:
- macOS 10.10+

## Declaration

```swift
@MainActor
optional func applicationDidChangeScreenParameters(_ notification: Notification)
```

```objc
- (void) applicationDidChangeScreenParameters:(NSNotification *) notification;
```

## Parameters

- `notification`: A notification named [`didChangeScreenParametersNotification`](../nsapplication/didchangescreenparametersnotification.md). Calling the [`object`](../../Foundation/nsnotification/object.md) method of this notification returns the `NSApplication` object itself.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplicationdelegate/applicationdidchangescreenparameters(_:))*