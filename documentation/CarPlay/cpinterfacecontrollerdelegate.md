# CPInterfaceControllerDelegate

**Framework**: CarPlay  
**Kind**: protocol  
**Role**: Protocol

The methods you implement to observe the addition and removal of templates in your app’s interface.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
@MainActor
protocol CPInterfaceControllerDelegate : NSObjectProtocol
```

```objc
@protocol CPInterfaceControllerDelegate <NSObject>
```

## Overview

Adopt the `CPInterfaceControllerDelegate` protocol in an custom type when you want to respond to changes in your app’s visible content. When a transition causes a new template to appear, the [`CPInterfaceController`](./cpinterfacecontroller.md) object calls the methods of this protocol on its delegate before and after the transition. Use the methods to perform additional tasks related to the appearance of the content.

## Topics

### Handling display-related events
- [func templateWillAppear(CPTemplate, animated: Bool)](./cpinterfacecontrollerdelegate/templatewillappear%28_,animated%29.md)
  Tells the delegate that the controller is about to show the specified template in your interface.
- [func templateDidAppear(CPTemplate, animated: Bool)](./cpinterfacecontrollerdelegate/templatedidappear%28_,animated%29.md)
  Tells the delegate that the controller showed the specified template in your interface.
- [func templateWillDisappear(CPTemplate, animated: Bool)](./cpinterfacecontrollerdelegate/templatewilldisappear%28_,animated%29.md)
  Tells the delegate that the controller is about to remove the specified template in your interface.
- [func templateDidDisappear(CPTemplate, animated: Bool)](./cpinterfacecontrollerdelegate/templatediddisappear%28_,animated%29.md)
  Tells the delegate that the controller removed the specified template from your interface.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Responding to interface changes
- [var delegate: (any CPInterfaceControllerDelegate)?](./cpinterfacecontroller/delegate.md)
  A custom object you use to respond when templates appear and disappear.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpinterfacecontrollerdelegate)*