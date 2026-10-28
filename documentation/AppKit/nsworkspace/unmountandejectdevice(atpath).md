# unmountAndEjectDevice(atPath:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Unmounts and ejects the device at the specified path.

**Availability**:
- macOS

## Declaration

```swift
func unmountAndEjectDevice(atPath path: String) -> Bool
```

```objc
- (BOOL) unmountAndEjectDeviceAtPath:(NSString *) path;
```

## Return Value

[`true`](../../Swift/true.md) if the system unmounted the device; otherwise, [`false`](../../Swift/false.md).

## Discussion

When this method begins, it posts an [`willUnmountNotification`](./willunmountnotification.md) to the `NSWorkspace` object’s notification center. When it is finished, it posts an [`didUnmountNotification`](./didunmountnotification.md).

Prefer the [`unmountAndEjectDevice(at:)`](./unmountandejectdevice%28at%29.md) method because it provides more detailed error information.

You can safely call this method from any thread of your app.

## Parameters

- `path`: The path to the device.

## See Also

### Unmounting a Device
- [func unmountAndEjectDevice(at: URL) throws](./unmountandejectdevice%28at%29.md)
  Attempts to eject the volume mounted at the given path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsworkspace/unmountandejectdevice(atpath:))*