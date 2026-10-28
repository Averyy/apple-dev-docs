# CPMapPanel.Delegate

**Framework**: CarPlay  
**Kind**: protocol  
**Role**: Protocol

The interface you use to respond to the appearance and disappearance of the panel.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+

## Declaration

```swift
protocol Delegate : NSObjectProtocol
```

```objc
@protocol CPMapPanelDelegate <NSObject>
```

## Overview

If you need to know when the system shows or hides the map panel, implement this protocol in a custom object and assign it to the [`delegate`](./delegate-swift.property.md) property of your [`CPMapPanel`](../cpmappanel.md) object. The system calls the methods of your object after it shows or hides the panel.

## Topics

### Instance Methods
- [func panelDidHide(CPMapPanel)](./delegate-swift.protocol/paneldidhide%28_%29.md)
  Tells the delegate that the system hid the specified map panel.
- [func panelDidShow(CPMapPanel)](./delegate-swift.protocol/paneldidshow%28_%29.md)
  Tells the delegate that the system displayed the specified map panel.

## Relationships

### Inherits From
- [NSObjectProtocol](../../ObjectiveC/nsobjectprotocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpmappanel/delegate-swift.protocol)*