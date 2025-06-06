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

- `notification`: A notification named  . Calling the   method of this notification returns the   object itself.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplicationdelegate/applicationdidchangescreenparameters(_:))*