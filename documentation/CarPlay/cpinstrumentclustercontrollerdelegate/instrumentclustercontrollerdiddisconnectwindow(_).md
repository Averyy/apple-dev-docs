# instrumentClusterControllerDidDisconnectWindow(_:)

**Framework**: CarPlay  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Tells the delegate that the system removed the window you use to draw your content.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 15.4+

## Declaration

```swift
func instrumentClusterControllerDidDisconnectWindow(_ instrumentClusterWindow: UIWindow)
```

```objc
- (void) instrumentClusterControllerDidDisconnectWindow:(UIWindow *) instrumentClusterWindow;
```

## Discussion

When CarPlay stops displaying your content in the instrument cluster, it removes the window and calls this method. In your implementation, perform any needed cleanup of your app-specific content.

## Parameters

- `instrumentClusterWindow`: The window that the system removed. This parameter can be `nil`.

## See Also

### Responding to life-cycle events
- [func instrumentClusterControllerDidConnect(UIWindow)](./instrumentclustercontrollerdidconnect%28_%29.md)
  Tells the delegate that there’s a new window for displaying your content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpinstrumentclustercontrollerdelegate/instrumentclustercontrollerdiddisconnectwindow(_:))*