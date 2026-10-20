# screensDidSleepNotification

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

A notification that the workspace posts when the device’s screen goes to sleep.

**Availability**:
- macOS 10.6+

## Declaration

```swift
class let screensDidSleepNotification: NSNotification.Name
```

```c
extern NSNotificationName const NSWorkspaceScreensDidSleepNotification;
```

#### Discussion

The notification object is the shared `NSWorkspace` instance. The notification doesn’t contain a `userInfo` dictionary.

Not many apps use this notification, but it can be useful for certain hardware-based drawing decisions, for example when using OpenGL.

> ❗ **Important**:  To receive this notification, use [`notificationCenter`](./notificationcenter.md) to register for it. If you use a different notification center to register, you won’t receive the notification.

To observe this notification using Swift concurrency, use [`NSWorkspace.ScreensDidSleepMessage`](./screensdidsleepmessage.md).

## See Also

### Responding to Environment Notifications
- [class let willLaunchApplicationNotification: NSNotification.Name](./willlaunchapplicationnotification.md)
  A notification that the workspace posts when the Finder is about to launch an app.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsworkspace/screensdidsleepnotification)*