# Signaling Changes for User-Driven Actions

**Framework**: Fileprovider

Signal the system about any changes created by an action.

#### Overview

You must let the system know about any changes so that it can update the document browser’s interface as needed. For some actions, the browser displays transient items while the action is in progress. The signal tells the browser that the action has completed, letting the system clean up the browser’s interface. The signal also provides updated information for any items that are currently on display.

You may need to signal the item itself, the item’s parent (both the new parent and the old parent for move actions), and the working set.

For any action, follow these steps:

1. Check the item’s parent. If you have an active enumerator for the parent, signal the parent.
2. Check the item itself. If you have an active enumerator for the item, signal the item.
3. If the item is in the working set, signal the working set.
4. If the action adds items to the working set (or removes them), signal the working set.
5. If the item’s parent is in the working set, and the action adds or removes items from the parent, signal the working set.

Signal the change by calling the [`NSFileProviderManager`](nsfileprovidermanager.md) class’s [`signalEnumerator(for:completionHandler:)`](nsfileprovidermanager/signalenumerator(for:completionhandler:).md) method and passing in the proper identifier. For the working set, use the workingSet identifier.

After the system is alerted to the change, it calls [`enumerateChanges(for:from:)`](nsfileproviderenumerator/enumeratechanges(for:from:).md) on any active enumerations that are affected and updates the browser’s user interface as needed.

> **Note**:  You can signal changes for an item even if it doesn’t have an active enumerator. In that case, the system logs a warning but otherwise ignores the signal.

For more information, see [`Tracking Your File Provider’s Changes`](tracking-your-file-provider-s-changes.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/FileProvider/signaling-changes-for-user-driven-actions)*