# panelDidHide(_:)

**Framework**: CarPlay  
**Kind**: method

Tells the delegate that the system hid the specified map panel.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+

## Declaration

```swift
optional func panelDidHide(_ panel: CPMapPanel)
```

#### Discussion

Shortly after the system removes a map panel from your CarPlay interface, the system calls this method to give you a chance to respond. Use this method to perform any cleanup tasks associated with the panel’s disappearance. The system calls this method on your app’s main thread.

## Parameters

- `panel`: The panel that disappeared from your map interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpmappanel/delegate-swift.protocol/paneldidhide(_:))*