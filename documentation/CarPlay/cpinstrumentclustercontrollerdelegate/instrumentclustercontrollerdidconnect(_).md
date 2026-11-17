# instrumentClusterControllerDidConnect(_:)

**Framework**: CarPlay  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Tells the delegate that there’s a new window for displaying your content.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 15.4+

## Declaration

```swift
func instrumentClusterControllerDidConnect(_ instrumentClusterWindow: UIWindow)
```

```objc
- (void) instrumentClusterControllerDidConnectWindow:(UIWindow *) instrumentClusterWindow;
```

## Discussion

The system creates the window as part of the initial scene setup. However, when you assign a new delegate object to the [`delegate`](../cpinstrumentclustercontroller/delegate.md) property of the controller, the system calls this method on your delegate object to give it a chance to handle the event.

## Parameters

- `instrumentClusterWindow`: The window object for displaying your content. Install the view controller with your custom content in the window’s [`rootViewController`](../../UIKit/uiwindow/rootviewcontroller.md) property.

## See Also

### Responding to life-cycle events
- [func instrumentClusterControllerDidDisconnectWindow(UIWindow)](./instrumentclustercontrollerdiddisconnectwindow%28_%29.md)
  Tells the delegate that the system removed the window you use to draw your content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpinstrumentclustercontrollerdelegate/instrumentclustercontrollerdidconnect(_:))*