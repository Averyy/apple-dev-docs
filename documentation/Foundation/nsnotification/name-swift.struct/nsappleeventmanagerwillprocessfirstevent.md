# NSAppleEventManagerWillProcessFirstEvent

**Framework**: Foundation  
**Kind**: property

Posted by `NSAppleEventManager` before it first dispatches an Apple event. Your application can use this notification to avoid registering any Apple event handlers until the first time at which they may be needed.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
static let NSAppleEventManagerWillProcessFirstEvent: NSNotification.Name
```

#### Discussion

The notification object is the `NSAppleEventManager`. This notification does not contain a `userInfo` dictionary.

## See Also

- [static let NSUbiquityIdentityDidChange: NSNotification.Name](nsnotification/name-swift.struct/nsubiquityidentitydidchange.md)
  Sent after the iCloud (“ubiquity”) identity has changed.
- [static let NSUndoManagerCheckpoint: NSNotification.Name](nsnotification/name-swift.struct/nsundomanagercheckpoint.md)
  Posted whenever an undo manager opens or closes an undo group (except when it opens a top-level group) and when checking the redo stack.
- [static let NSUndoManagerDidCloseUndoGroup: NSNotification.Name](nsnotification/name-swift.struct/nsundomanagerdidcloseundogroup.md)
  Posted after an undo manager closes an undo group.
- [static let NSUndoManagerDidOpenUndoGroup: NSNotification.Name](nsnotification/name-swift.struct/nsundomanagerdidopenundogroup.md)
  Posted whenever an undo manager opens an undo group.
- [static let NSUndoManagerDidRedoChange: NSNotification.Name](nsnotification/name-swift.struct/nsundomanagerdidredochange.md)
  Posted just after an undo manager performs a redo operation.
- [static let NSUndoManagerDidUndoChange: NSNotification.Name](nsnotification/name-swift.struct/nsundomanagerdidundochange.md)
  Posted just after an undo manager performs an undo operation.
- [static let NSUndoManagerWillCloseUndoGroup: NSNotification.Name](nsnotification/name-swift.struct/nsundomanagerwillcloseundogroup.md)
  Posted before an undo manager closes an undo group.
- [static let NSUndoManagerWillRedoChange: NSNotification.Name](nsnotification/name-swift.struct/nsundomanagerwillredochange.md)
  Posted just before an undo manager performs a redo operation.
- [static let NSUndoManagerWillUndoChange: NSNotification.Name](nsnotification/name-swift.struct/nsundomanagerwillundochange.md)
  Posted just before an undo manager performs an undo operation.
- [static let NSWillBecomeMultiThreaded: NSNotification.Name](nsnotification/name-swift.struct/nswillbecomemultithreaded.md)
  Posted when the first thread is detached from the current thread. The `NSThread` class posts this notification at most once—the first time a thread is detached using [`detachNewThreadSelector(_:toTarget:with:)`](thread/detachnewthreadselector(_:totarget:with:).md) or the [`start()`](thread/start().md) method. Subsequent invocations of those methods do not post this notification. Observers of this notification have their notification method invoked in the main thread, not the new thread. The observer notification methods always execute before the new thread begins executing.
- [static let NSBundleResourceRequestLowDiskSpace: NSNotification.Name](nsnotification/name-swift.struct/nsbundleresourcerequestlowdiskspace.md)
  Posted after the system detects that the amount of available disk space is getting low. The notification is posted to the default notification center.
- [static let NSCalendarDayChanged: NSNotification.Name](nsnotification/name-swift.struct/nscalendardaychanged.md)
  A notification that is posted whenever the calendar day of the system changes, as determined by the system calendar, locale, and time zone.
- [static let NSDidBecomeSingleThreaded: NSNotification.Name](nsnotification/name-swift.struct/nsdidbecomesinglethreaded.md)
  Not implemented.
- [static let NSExtensionHostDidBecomeActive: NSNotification.Name](nsnotification/name-swift.struct/nsextensionhostdidbecomeactive.md)
  Posted when the extension’s host app moves from the inactive to the active state.
- [static let NSExtensionHostDidEnterBackground: NSNotification.Name](nsnotification/name-swift.struct/nsextensionhostdidenterbackground.md)
  Posted when the extension’s host app begins running in the background.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsnotification/name-swift.struct/nsappleeventmanagerwillprocessfirstevent)*