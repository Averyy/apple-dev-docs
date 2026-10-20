# deviceBrowserView(_:selectionDidChange:)

**Framework**: Quartz  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Sent to the delegate when the selection changes in the browser view.

**Availability**:
- macOS 10.6+

## Declaration

```swift
func deviceBrowserView(_ deviceBrowserView: IKDeviceBrowserView!, selectionDidChange device: ICDevice!)
```

```objc
- (void) deviceBrowserView:(IKDeviceBrowserView *) deviceBrowserView selectionDidChange:(ICDevice *) device;
```

## Parameters

- `deviceBrowserView`: The object that sent the message.
- `device`: The newly selected device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/ikdevicebrowserviewdelegate/devicebrowserview(_:selectiondidchange:))*