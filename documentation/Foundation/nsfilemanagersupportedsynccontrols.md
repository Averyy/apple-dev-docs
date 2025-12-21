# NSFileManagerSupportedSyncControls

**Framework**: Foundation  
**Kind**: struct

An option set of the sync controls available for an item.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
struct NSFileManagerSupportedSyncControls
```

#### Overview

Get an instance of this type by calling [`resourceValues(forKeys:)`](url/resourcevalues(forkeys:).md) on a [`URL`](url.md) instance (Swift) or [`getResourceValue(_:forKey:)`](nsurl/getresourcevalue(_:forkey:).md) on an [`NSURL`](nsurl.md) (Swift or Objective-C) and passing in the key [`ubiquitousItemSupportedSyncControlsKey`](urlresourcekey/ubiquitousitemsupportedsynccontrolskey.md).

## Topics

### Inspecting supported sync controls
- [static var pauseSync: NSFileManagerSupportedSyncControls](nsfilemanagersupportedsynccontrols/pausesync.md)
  The file provider supports pausing the sync on the item.
- [static var failUploadOnConflict: NSFileManagerSupportedSyncControls](nsfilemanagersupportedsynccontrols/failuploadonconflict.md)
  The file provider supports failing an upload if the local and server versions conflict.
### Working with raw values
- [init(rawValue: UInt)](nsfilemanagersupportedsynccontrols/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [func pauseSyncForUbiquitousItem(at: URL, completionHandler: ((any Error)?) -> Void)](filemanager/pausesyncforubiquitousitem(at:completionhandler:).md)
  Asynchronously pauses sync of an item at the given URL.
- [func resumeSyncForUbiquitousItem(at: URL, with: NSFileManagerResumeSyncBehavior, completionHandler: ((any Error)?) -> Void)](filemanager/resumesyncforubiquitousitem(at:with:completionhandler:).md)
  Asynchronously resumes the sync on a paused item using the given resume behavior.
- [enum NSFileManagerResumeSyncBehavior](nsfilemanagerresumesyncbehavior.md)
  The behaviors the file manager can apply to resolve conflicts when resuming a sync.
- [func fetchLatestRemoteVersionOfItem(at: URL, completionHandler: (NSFileVersion?, (any Error)?) -> Void)](filemanager/fetchlatestremoteversionofitem(at:completionhandler:).md)
  Asynchronously fetches the latest remote version of a given item from the server.
- [class NSFileVersion](nsfileversion.md)
  A snapshot of a file at a specific point in time.
- [func uploadLocalVersionOfUbiquitousItem(at: URL, withConflictResolutionPolicy: NSFileManagerUploadLocalVersionConflictPolicy, completionHandler: (NSFileVersion?, (any Error)?) -> Void)](filemanager/uploadlocalversionofubiquitousitem(at:withconflictresolutionpolicy:completionhandler:).md)
  Asynchronously uploads the local version of the item using the provided conflict resolution policy.
- [enum NSFileManagerUploadLocalVersionConflictPolicy](nsfilemanageruploadlocalversionconflictpolicy.md)
  The policies the file manager can apply to resolve conflicts when uploading a local version of a file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsfilemanagersupportedsynccontrols)*