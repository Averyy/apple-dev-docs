# NSFileVersion

**Framework**: Foundation  
**Kind**: class  
**Role**: Class

A snapshot of a file at a specific point in time.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class NSFileVersion
```

```objc
@interface NSFileVersion : NSObject
```

#### Overview

Use the methods of this class to access, create, and manage file revisions in your app.

Each file version instance contains metadata about a single revision, including the location of the associated file, the modification date of the revision, and whether the revision is discardable.

In Mac apps, you can use file version objects to track changes to a local file over time and to prevent the loss of data during editing. When managing local versions, the document architecture creates versions at specific points in the lifetime of your application. Your application can also create versions explicitly at times that your application designates as appropriate.

In addition to managing local files, the system also uses this class to manage cloud-based files. For files in the cloud, there is usually only one version of the file at any given time. However, additional file versions may be created in cases where two different computers attempt to save the file to the cloud at the same time. In that case, one file is chosen as the current version and any other versions are tagged as being in conflict with the original. Conflict versions are reported to the appropriate file presenter objects and should be resolved as soon as possible so that the corresponding files can be removed from the cloud.

## Topics

### Getting the Version of a File
- [class func currentVersionOfItem(at: URL) -> NSFileVersion?](./nsfileversion/currentversionofitem%28at%29.md)
  Returns the most recent version object for the file at the specified URL.
- [class func otherVersionsOfItem(at: URL) -> [NSFileVersion]?](./nsfileversion/otherversionsofitem%28at%29.md)
  Returns all versions of the specified file except the current version.
- [class func version(itemAt: URL, forPersistentIdentifier: Any) -> NSFileVersion?](./nsfileversion/version%28itemat,forpersistentidentifier%29.md)
  Returns the version of the file that has the specified persistent ID.
- [class func temporaryDirectoryURLForNewVersionOfItem(at: URL) -> URL](./nsfileversion/temporarydirectoryurlfornewversionofitem%28at%29.md)
  Creates and returns a temporary directory to use for saving the contents of the file.
### Creating a New Version
- [class func addOfItem(at: URL, withContentsOf: URL, options: NSFileVersion.AddingOptions) throws -> NSFileVersion](./nsfileversion/addofitem%28at,withcontentsof,options%29.md)
  Creates a version of the file at the specified location.
### Accessing the Version Information
- [var url: URL](./nsfileversion/url.md)
  The URL identifying the location of the file associated with the file version object.
- [var localizedName: String?](./nsfileversion/localizedname.md)
  The string containing the user-presentable name of the file version.
- [var localizedNameOfSavingComputer: String?](./nsfileversion/localizednameofsavingcomputer.md)
  The user-presentable name of the computer on which the revision was saved.
- [var modificationDate: Date?](./nsfileversion/modificationdate.md)
  The modification date of the version.
- [var persistentIdentifier: any NSCoding](./nsfileversion/persistentidentifier.md)
  The identifier for this version of the file.
- [var isDiscardable: Bool](./nsfileversion/isdiscardable.md)
  A Boolean value that specifies whether the system can delete the associated file at some future time.
### Handling Version Conflicts
- [var isConflict: Bool](./nsfileversion/isconflict.md)
  A Boolean value indicating whether the contents of the version are in conflict with the contents of another version.
- [var isResolved: Bool](./nsfileversion/isresolved.md)
  A Boolean value that indicates if the version object is in conflict or not.
- [class func unresolvedConflictVersionsOfItem(at: URL) -> [NSFileVersion]?](./nsfileversion/unresolvedconflictversionsofitem%28at%29.md)
  Returns an array of version objects that are currently in conflict for the specified URL.
### Replacing and Deleting Versions
- [func replaceItem(at: URL, options: NSFileVersion.ReplacingOptions) throws -> URL](./nsfileversion/replaceitem%28at,options%29.md)
  Replace the contents of the specified file with the contents of the current version’s file.
- [func remove() throws](./nsfileversion/remove%28%29.md)
  Remove this version object and its associated file from the version store.
- [class func removeOtherVersionsOfItem(at: URL) throws](./nsfileversion/removeotherversionsofitem%28at%29.md)
  Removes all versions of a file, except the current one, from the version store.
### Constants
- [NSFileVersion.AddingOptions](./nsfileversion/addingoptions.md)
  Options for adding a new file version.
- [NSFileVersion.ReplacingOptions](./nsfileversion/replacingoptions.md)
  Options for replacing a file version.
### Initializers
- [init?(ofItemAtURL: URL, forPersistentIdentifier: Any)](./nsfileversion/init%28ofitematurl,forpersistentidentifier%29.md)
### Instance Properties
- [var hasLocalContents: Bool](./nsfileversion/haslocalcontents.md)
  Whether the version has local contents. Versions that are returned by +getNonlocalVersionsOfItemAtURL:completionHandler: do not initially have local contents. You can only access their contents, either directly via the URL or by invoking -replaceItemAtURL:options:error:, from within a coordinated read on the NSFileVersion’s URL.
- [var hasThumbnail: Bool](./nsfileversion/hasthumbnail.md)
  Whether the version has a thumbnail image available. Thumbnails for versions from +getNonlocalVersionsOfItemAtURL:completionHandler: may not immediately be available. As soon as it becomes available, this property will change from NO to YES. You can use KVO to be notified of this change. If a thumbnail is available, you can access it using NSURLThumbnailKey or NSURLThumbnailDictionaryKey.
- [var originatorNameComponents: PersonNameComponents?](./nsfileversion/originatornamecomponents.md)
  The name components of the user who created this version of the file. Is nil if the file is not shared or if the current user is the originator.
### Type Methods
- [class func getNonlocalVersionsOfItem(at: URL, completionHandler: ([NSFileVersion]?, (any Error)?) -> Void)](./nsfileversion/getnonlocalversionsofitem%28at,completionhandler%29.md)
  Asynchronously returns an array of NSFileVersions associated with the file located by the given URL, or nil if there is no such file or another error occurs.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Managed file access
- [class FileHandle](./filehandle.md)
  An object-oriented wrapper for a file descriptor.
- [class NSFileSecurity](./nsfilesecurity.md)
  A stub class that encapsulates security information about a file.
- [class FileWrapper](./filewrapper.md)
  A representation of a node (a file, directory, or symbolic link) in the file system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsfileversion)*