# panelDidShow(_:)

**Framework**: CarPlay  
**Kind**: method

Tells the delegate that the system displayed the specified map panel.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+

## Declaration

```swift
optional func panelDidShow(_ panel: CPMapPanel)
```

#### Discussion

Shortly after a panel appears in your CarPlay interface, the system calls this method to give you a chance to respond. Use this method to perform any additional tasks that require the panel to be visible. The system calls this method on your app’s main thread after any animations to display the panel.

## Parameters

- `panel`: The panel that appeared in your map interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpmappanel/delegate-swift.protocol/paneldidshow(_:))*