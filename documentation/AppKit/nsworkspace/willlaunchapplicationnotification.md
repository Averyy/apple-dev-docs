# willLaunchApplicationNotification

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

A notification that the workspace posts when the Finder is about to launch an app.

**Availability**:
- macOS

## Declaration

```swift
class let willLaunchApplicationNotification: NSNotification.Name
```

```c
extern NSNotificationName NSWorkspaceWillLaunchApplicationNotification;
```

## Discussion

The notification object is the shared `NSWorkspace` instance. The `userInfo` dictionary contains the [`applicationUserInfoKey`](./applicationuserinfokey.md) key with a corresponding instance of [`NSRunningApplication`](../nsrunningapplication.md) that represents the affected app.

The system doesn’t post this notification for background apps or for apps that have the `LSUIElement` key in their `Info.plist` file. If you want to know when all apps (including background apps) launch or terminate, use key-value observing to monitor the value that returns from the [`runningApplications`](./runningapplications.md) method.

> ❗ **Important**:  To receive this notification, use [`notificationCenter`](./notificationcenter.md) to register for it. If you use a different notification center to register, you won’t receive the notification.

To observe this notification using Swift concurrency, use [`NSWorkspace.WillLaunchApplicationMessage`](./willlaunchapplicationmessage.md).

## See Also

### Responding to Environment Notifications
- [class let didLaunchApplicationNotification: NSNotification.Name](./didlaunchapplicationnotification.md)
  A notification that the workspace posts when a new app starts up.
- [class let didTerminateApplicationNotification: NSNotification.Name](./didterminateapplicationnotification.md)
  A notification that the workspace posts when an app finishes executing.
- [class let sessionDidBecomeActiveNotification: NSNotification.Name](./sessiondidbecomeactivenotification.md)
  A notification that the workspace posts after a user session switches in.
- [class let sessionDidResignActiveNotification: NSNotification.Name](./sessiondidresignactivenotification.md)
  A notification that the workspace posts before a user session switches out.
- [class let didHideApplicationNotification: NSNotification.Name](./didhideapplicationnotification.md)
  A notification that the workspace posts when the Finder hides an app.
- [class let didUnhideApplicationNotification: NSNotification.Name](./didunhideapplicationnotification.md)
  A notification that the workspace posts when the Finder unhides an app.
- [class let didActivateApplicationNotification: NSNotification.Name](./didactivateapplicationnotification.md)
  A notification that the workspace posts when the Finder is about to activate an app.
- [class let didDeactivateApplicationNotification: NSNotification.Name](./diddeactivateapplicationnotification.md)
  A notification that the workspace posts when the Finder deactivates an app.
- [class let didRenameVolumeNotification: NSNotification.Name](./didrenamevolumenotification.md)
  A notification that the workspace posts when a volume changes its name or mount path.
- [class let didMountNotification: NSNotification.Name](./didmountnotification.md)
  A notification that the workspace posts when a new device mounts.
- [class let willUnmountNotification: NSNotification.Name](./willunmountnotification.md)
  A notification that the workspace posts when the Finder is about to unmount a device.
- [class let didUnmountNotification: NSNotification.Name](./didunmountnotification.md)
  A notification that the workspace posts when the Finder unmounts a device.
- [class let didChangeFileLabelsNotification: NSNotification.Name](./didchangefilelabelsnotification.md)
  A notification that the workspace posts when the Finder file labels or colors change.
- [class let activeSpaceDidChangeNotification: NSNotification.Name](./activespacedidchangenotification.md)
  A notification that the workspace posts when a Spaces change occurs.
- [class let didWakeNotification: NSNotification.Name](./didwakenotification.md)
  A notification that the workspace posts when the device wakes from sleep.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsworkspace/willlaunchapplicationnotification)*