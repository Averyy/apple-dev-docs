# NSFileManagerSupportedSyncControls

**Framework**: Foundation  
**Kind**: struct  
**Role**: Structure

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

```c
enum NSFileManagerSupportedSyncControls : NSUInteger;
```

#### Overview

Get an instance of this type by calling [`resourceValues(forKeys:)`](./url/resourcevalues%28forkeys%29.md) on a [`URL`](./url.md) instance (Swift) or [`getResourceValue(_:forKey:)`](./nsurl/getresourcevalue%28_,forkey%29.md) on an [`NSURL`](./nsurl.md) (Swift or Objective-C) and passing in the key [`ubiquitousItemSupportedSyncControlsKey`](./urlresourcekey/ubiquitousitemsupportedsynccontrolskey.md).

## Topics

### Inspecting supported sync controls
- [static var pauseSync: NSFileManagerSupportedSyncControls](./nsfilemanagersupportedsynccontrols/pausesync.md)
  The file provider supports pausing the sync on the item.
- [static var failUploadOnConflict: NSFileManagerSupportedSyncControls](./nsfilemanagersupportedsynccontrols/failuploadonconflict.md)
  The file provider supports failing an upload if the local and server versions conflict.
### Working with raw values
- [init(rawValue: UInt)](./nsfilemanagersupportedsynccontrols/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../Swift/optionset.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [SetAlgebra](../Swift/setalgebra.md)

## See Also

### Controlling file provider synchronization
- [func pauseSyncForUbiquitousItem(at: URL, completionHandler: ((any Error)?) -> Void)](./filemanager/pausesyncforubiquitousitem%28at,completionhandler%29.md)
  Asynchronously pauses sync of an item at the given URL.
- [func resumeSyncForUbiquitousItem(at: URL, with: NSFileManagerResumeSyncBehavior, completionHandler: ((any Error)?) -> Void)](./filemanager/resumesyncforubiquitousitem%28at,with,completionhandler%29.md)
  Asynchronously resumes the sync on a paused item using the given resume behavior.
- [enum NSFileManagerResumeSyncBehavior](./nsfilemanagerresumesyncbehavior.md)
  The behaviors the file manager can apply to resolve conflicts when resuming a sync.
- [func fetchLatestRemoteVersionOfItem(at: URL, completionHandler: (NSFileVersion?, (any Error)?) -> Void)](./filemanager/fetchlatestremoteversionofitem%28at,completionhandler%29.md)
  Asynchronously fetches the latest remote version of a given item from the server.
- [class NSFileVersion](./nsfileversion.md)
  A snapshot of a file at a specific point in time.
- [func uploadLocalVersionOfUbiquitousItem(at: URL, withConflictResolutionPolicy: NSFileManagerUploadLocalVersionConflictPolicy, completionHandler: (NSFileVersion?, (any Error)?) -> Void)](./filemanager/uploadlocalversionofubiquitousitem%28at,withconflictresolutionpolicy,completionhandler%29.md)
  Asynchronously uploads the local version of the item using the provided conflict resolution policy.
- [enum NSFileManagerUploadLocalVersionConflictPolicy](./nsfilemanageruploadlocalversionconflictpolicy.md)
  The policies the file manager can apply to resolve conflicts when uploading a local version of a file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsfilemanagersupportedsynccontrols)*