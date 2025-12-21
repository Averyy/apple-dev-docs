# unmountAndEjectDevice(atPath:)

**Framework**: AppKit  
**Kind**: method

Unmounts and ejects the device at the specified path.

**Availability**:
- macOS ?+

## Declaration

```swift
func unmountAndEjectDevice(atPath path: String) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if the system unmounted the device; otherwise, [`false`](https://developer.apple.com/documentation/Swift/false).

#### Discussion

When this method begins, it posts an [`willUnmountNotification`](nsworkspace/willunmountnotification.md) to the `NSWorkspace` object’s notification center. When it is finished, it posts an [`didUnmountNotification`](nsworkspace/didunmountnotification.md).

Prefer the [`unmountAndEjectDevice(at:)`](nsworkspace/unmountandejectdevice(at:).md) method because it provides more detailed error information.

You can safely call this method from any thread of your app.

## Parameters

- `path`: The path to the device.

## See Also

- [func unmountAndEjectDevice(at: URL) throws](nsworkspace/unmountandejectdevice(at:).md)
  Attempts to eject the volume mounted at the given path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsworkspace/unmountandejectdevice(atpath:))*