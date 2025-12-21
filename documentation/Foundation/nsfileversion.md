# NSFileVersion

**Framework**: Foundation  
**Kind**: class

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

#### Overview

Use the methods of this class to access, create, and manage file revisions in your app.

Each file version instance contains metadata about a single revision, including the location of the associated file, the modification date of the revision, and whether the revision is discardable.

In Mac apps, you can use file version objects to track changes to a local file over time and to prevent the loss of data during editing. When managing local versions, the document architecture creates versions at specific points in the lifetime of your application. Your application can also create versions explicitly at times that your application designates as appropriate.

In addition to managing local files, the system also uses this class to manage cloud-based files. For files in the cloud, there is usually only one version of the file at any given time. However, additional file versions may be created in cases where two different computers attempt to save the file to the cloud at the same time. In that case, one file is chosen as the current version and any other versions are tagged as being in conflict with the original. Conflict versions are reported to the appropriate file presenter objects and should be resolved as soon as possible so that the corresponding files can be removed from the cloud.

## Topics

### Getting the Version of a File
- [class func currentVersionOfItem(at: URL) -> NSFileVersion?](nsfileversion/currentversionofitem(at:).md)
  Returns the most recent version object for the file at the specified URL.
- [class func otherVersionsOfItem(at: URL) -> [NSFileVersion]?](nsfileversion/otherversionsofitem(at:).md)
  Returns all versions of the specified file except the current version.
- [class func version(itemAt: URL, forPersistentIdentifier: Any) -> NSFileVersion?](nsfileversion/version(itemat:forpersistentidentifier:).md)
  Returns the version of the file that has the specified persistent ID.
- [class func temporaryDirectoryURLForNewVersionOfItem(at: URL) -> URL](nsfileversion/temporarydirectoryurlfornewversionofitem(at:).md)
  Creates and returns a temporary directory to use for saving the contents of the file.
### Creating a New Version
- [class func addOfItem(at: URL, withContentsOf: URL, options: NSFileVersion.AddingOptions) throws -> NSFileVersion](nsfileversion/addofitem(at:withcontentsof:options:).md)
  Creates a version of the file at the specified location.
### Accessing the Version Information
- [var url: URL](nsfileversion/url.md)
  The URL identifying the location of the file associated with the file version object.
- [var localizedName: String?](nsfileversion/localizedname.md)
  The string containing the user-presentable name of the file version.
- [var localizedNameOfSavingComputer: String?](nsfileversion/localizednameofsavingcomputer.md)
  The user-presentable name of the computer on which the revision was saved.
- [var modificationDate: Date?](nsfileversion/modificationdate.md)
  The modification date of the version.
- [var persistentIdentifier: any NSCoding](nsfileversion/persistentidentifier.md)
  The identifier for this version of the file.
- [var isDiscardable: Bool](nsfileversion/isdiscardable.md)
  A Boolean value that specifies whether the system can delete the associated file at some future time.
### Handling Version Conflicts
- [var isConflict: Bool](nsfileversion/isconflict.md)
  A Boolean value indicating whether the contents of the version are in conflict with the contents of another version.
- [var isResolved: Bool](nsfileversion/isresolved.md)
  A Boolean value that indicates if the version object is in conflict or not.
- [class func unresolvedConflictVersionsOfItem(at: URL) -> [NSFileVersion]?](nsfileversion/unresolvedconflictversionsofitem(at:).md)
  Returns an array of version objects that are currently in conflict for the specified URL.
### Replacing and Deleting Versions
- [func replaceItem(at: URL, options: NSFileVersion.ReplacingOptions) throws -> URL](nsfileversion/replaceitem(at:options:).md)
  Replace the contents of the specified file with the contents of the current version’s file.
- [func remove() throws](nsfileversion/remove.md)
  Remove this version object and its associated file from the version store.
- [class func removeOtherVersionsOfItem(at: URL) throws](nsfileversion/removeotherversionsofitem(at:).md)
  Removes all versions of a file, except the current one, from the version store.
### Constants
- [NSFileVersion.AddingOptions](nsfileversion/addingoptions.md)
  Options for adding a new file version.
- [NSFileVersion.ReplacingOptions](nsfileversion/replacingoptions.md)
  Options for replacing a file version.
### Instance Properties
- [var hasLocalContents: Bool](nsfileversion/haslocalcontents.md)
- [var hasThumbnail: Bool](nsfileversion/hasthumbnail.md)
- [var originatorNameComponents: PersonNameComponents?](nsfileversion/originatornamecomponents.md)
### Type Methods
- [class func getNonlocalVersionsOfItem(at: URL, completionHandler: ([NSFileVersion]?, (any Error)?) -> Void)](nsfileversion/getnonlocalversionsofitem(at:completionhandler:).md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class FileHandle](filehandle.md)
  An object-oriented wrapper for a file descriptor.
- [class NSFileSecurity](nsfilesecurity.md)
  A stub class that encapsulates security information about a file.
- [class FileWrapper](filewrapper.md)
  A representation of a node (a file, directory, or symbolic link) in the file system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsfileversion)*