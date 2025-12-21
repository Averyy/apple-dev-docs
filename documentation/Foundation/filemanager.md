# FileManager

**Framework**: Foundation  
**Kind**: class

A convenient interface to the contents of the file system, and the primary means of interacting with it.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class FileManager
```

## Mentions

- [About Apple File System](about-apple-file-system.md)
- [Using the file system effectively](using-the-file-system-effectively.md)
- [Optimizing Your App’s Data for iCloud Backup](optimizing-your-app-s-data-for-icloud-backup.md)

#### Overview

A file manager object lets you examine the contents of the file system and make changes to it. The [`FileManager`](filemanager.md) class provides convenient access to a shared file manager object that is suitable for most types of file-related manipulations. A file manager object is typically your primary mode of interaction with the file system. You use it to locate, create, copy, and move files and directories. You also use it to get information about a file or directory or change some of its attributes.

When specifying the location of files, you can use either [`NSURL`](nsurl.md) or [`NSString`](nsstring.md) objects. The use of the [`NSURL`](nsurl.md) class is generally preferred for specifying file-system items because URLs can convert path information to a more efficient representation internally. You can also obtain a bookmark from an [`NSURL`](nsurl.md) object, which is similar to an alias and offers a more sure way of locating the file or directory later.

If you are moving, copying, linking, or removing files or directories, you can use a delegate in conjunction with a file manager object to manage those operations. The delegate’s role is to affirm the operation and to decide whether to proceed when errors occur. In macOS 10.7 and later, the delegate must conform to the [`FileManagerDelegate`](filemanagerdelegate.md) protocol.

In iOS 5.0 and later and in macOS 10.7 and later, [`FileManager`](filemanager.md) includes methods for managing items stored in iCloud. Files and directories tagged for cloud storage are synced to iCloud so that they can be made available to the user’s iOS devices and Macintosh computers. Changes to an item in one location are propagated to all other locations to ensure the items stay in sync.

##### Sync Control

A [`package`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFBundles/DocumentPackages/DocumentPackages.html#//apple_ref/doc/uid/10000123i-CH106-SW1) is a directory that the system presents as a single file to the person using the device. Apps with documents that contain multiple files can use packages to manage contents like media assets. In iOS 26 and macOS 26 and later, [`FileManager`](filemanager.md) introduces methods for controlling how a file provider syncs these items. By pausing sync when your app opens a package and resuming when it closes, your app can prevent the file provider from changing the contents of the package in unexpected ways, which potentially leaves the document in an inconsistent state. You can also use this pause and resume API on regular “flat” files.

##### Threading Considerations

The methods of the shared [`FileManager`](filemanager.md) object can be called from multiple threads safely. However, if you use a delegate to receive notifications about the status of move, copy, remove, and link operations, you should create a unique instance of the file manager object, assign your delegate to that object, and use that file manager to initiate your operations.

## Topics

### Creating a file manager
- [convenience init(authorization: NSWorkspace.Authorization)](filemanager/init(authorization:).md)
  Initializes a file manager object that is authorized to perform privileged file system operations.
- [class var `default`: FileManager](filemanager/default.md)
  The shared file manager object for the process.
### Accessing user directories
- [var homeDirectoryForCurrentUser: URL](filemanager/homedirectoryforcurrentuser.md)
  The home directory for the current user.
- [func NSHomeDirectory() -> String](nshomedirectory().md)
  Returns the path to either the user’s or application’s home directory, depending on the platform.
- [func NSUserName() -> String](nsusername().md)
  Returns the logon name of the current user.
- [func NSFullUserName() -> String](nsfullusername().md)
  Returns a string containing the full name of the current user.
- [func homeDirectory(forUser: String) -> URL?](filemanager/homedirectory(foruser:).md)
  Returns the home directory for the specified user.
- [func NSHomeDirectoryForUser(String?) -> String?](nshomedirectoryforuser(_:).md)
  Returns the path to a given user’s home directory.
- [var temporaryDirectory: URL](filemanager/temporarydirectory.md)
  The temporary directory for the current user.
- [func NSTemporaryDirectory() -> String](nstemporarydirectory().md)
  Returns the path of the temporary directory for the current user.
### Locating system directories
- [func url(for: FileManager.SearchPathDirectory, in: FileManager.SearchPathDomainMask, appropriateFor: URL?, create: Bool) throws -> URL](filemanager/url(for:in:appropriatefor:create:).md)
  Locates and optionally creates the specified common directory in a domain.
- [func urls(for: FileManager.SearchPathDirectory, in: FileManager.SearchPathDomainMask) -> [URL]](filemanager/urls(for:in:).md)
  Returns an array of URLs for the specified common directory in the requested domains.
- [func NSSearchPathForDirectoriesInDomains(FileManager.SearchPathDirectory, FileManager.SearchPathDomainMask, Bool) -> [String]](nssearchpathfordirectoriesindomains(_:_:_:).md)
  Creates a list of directory search paths.
- [func NSOpenStepRootDirectory() -> String](nsopensteprootdirectory().md)
  Returns the root directory of the user’s system.
### Locating application group container directories
- [func containerURL(forSecurityApplicationGroupIdentifier: String) -> URL?](filemanager/containerurl(forsecurityapplicationgroupidentifier:).md)
  Returns the container directory associated with the specified security application group identifier.
- [App Groups Entitlement](../BundleResources/Entitlements/com.apple.security.application-groups.md)
  A list of identifiers specifying the groups your app belongs to.
### Discovering directory contents
- [func contentsOfDirectory(at: URL, includingPropertiesForKeys: [URLResourceKey]?, options: FileManager.DirectoryEnumerationOptions) throws -> [URL]](filemanager/contentsofdirectory(at:includingpropertiesforkeys:options:).md)
  Performs a shallow search of the specified directory and returns URLs for the contained items.
- [func contentsOfDirectory(atPath: String) throws -> [String]](filemanager/contentsofdirectory(atpath:).md)
  Performs a shallow search of the specified directory and returns the paths of any contained items.
- [func enumerator(at: URL, includingPropertiesForKeys: [URLResourceKey]?, options: FileManager.DirectoryEnumerationOptions, errorHandler: ((URL, any Error) -> Bool)?) -> FileManager.DirectoryEnumerator?](filemanager/enumerator(at:includingpropertiesforkeys:options:errorhandler:).md)
  Returns a directory enumerator object that can be used to perform a deep enumeration of the directory at the specified URL.
- [func enumerator(atPath: String) -> FileManager.DirectoryEnumerator?](filemanager/enumerator(atpath:).md)
  Returns a directory enumerator object that can be used to perform a deep enumeration of the directory at the specified path.
- [FileManager.DirectoryEnumerator](filemanager/directoryenumerator.md)
  An object that enumerates the contents of a directory.
- [func mountedVolumeURLs(includingResourceValuesForKeys: [URLResourceKey]?, options: FileManager.VolumeEnumerationOptions) -> [URL]?](filemanager/mountedvolumeurls(includingresourcevaluesforkeys:options:).md)
  Returns an array of URLs that identify the mounted volumes available on the device.
- [FileManager.VolumeEnumerationOptions](filemanager/volumeenumerationoptions.md)
  Options for enumerating mounted volumes with the [`mountedVolumeURLs(includingResourceValuesForKeys:options:)`](filemanager/mountedvolumeurls(includingresourcevaluesforkeys:options:).md) method.
- [func subpathsOfDirectory(atPath: String) throws -> [String]](filemanager/subpathsofdirectory(atpath:).md)
  Performs a deep enumeration of the specified directory and returns the paths of all of the contained subdirectories.
- [func subpaths(atPath: String) -> [String]?](filemanager/subpaths(atpath:).md)
  Returns an array of strings identifying the paths for all items in the specified directory.
### Creating and deleting items
- [func createDirectory(at: URL, withIntermediateDirectories: Bool, attributes: [FileAttributeKey : Any]?) throws](filemanager/createdirectory(at:withintermediatedirectories:attributes:).md)
  Creates a directory with the given attributes at the specified URL.
- [func createDirectory(atPath: String, withIntermediateDirectories: Bool, attributes: [FileAttributeKey : Any]?) throws](filemanager/createdirectory(atpath:withintermediatedirectories:attributes:).md)
  Creates a directory with given attributes at the specified path.
- [func createFile(atPath: String, contents: Data?, attributes: [FileAttributeKey : Any]?) -> Bool](filemanager/createfile(atpath:contents:attributes:).md)
  Creates a file with the specified content and attributes at the given location.
- [func removeItem(at: URL) throws](filemanager/removeitem(at:).md)
  Removes the file or directory at the specified URL.
- [func removeItem(atPath: String) throws](filemanager/removeitem(atpath:).md)
  Removes the file or directory at the specified path.
- [func trashItem(at: URL, resultingItemURL: AutoreleasingUnsafeMutablePointer<NSURL?>?) throws](filemanager/trashitem(at:resultingitemurl:).md)
  Moves an item to the trash.
### Replacing items
- [func replaceItemAt(URL, withItemAt: URL, backupItemName: String?, options: FileManager.ItemReplacementOptions) throws -> URL?](filemanager/replaceitemat(_:withitemat:backupitemname:options:)-4210g.md)
  Replaces the contents of the item at the specified URL in a manner that ensures no data loss occurs.
- [func replaceItem(at: URL, withItemAt: URL, backupItemName: String?, options: FileManager.ItemReplacementOptions, resultingItemURL: AutoreleasingUnsafeMutablePointer<NSURL?>?) throws](filemanager/replaceitem(at:withitemat:backupitemname:options:resultingitemurl:).md)
  Replaces the contents of the item at the specified URL in a manner that ensures no data loss occurs.
- [FileManager.ItemReplacementOptions](filemanager/itemreplacementoptions.md)
  Options for specifying the behavior of file replacement operations.
### Moving and copying items
- [func copyItem(at: URL, to: URL) throws](filemanager/copyitem(at:to:).md)
  Copies the file at the specified URL to a new location synchronously.
- [func copyItem(atPath: String, toPath: String) throws](filemanager/copyitem(atpath:topath:).md)
  Copies the item at the specified path to a new location synchronously.
- [func moveItem(at: URL, to: URL) throws](filemanager/moveitem(at:to:).md)
  Moves the file or directory at the specified URL to a new location synchronously.
- [func moveItem(atPath: String, toPath: String) throws](filemanager/moveitem(atpath:topath:).md)
  Moves the file or directory at the specified path to a new location synchronously.
### Managing iCloud-based items
- [var ubiquityIdentityToken: (any NSCoding & NSCopying & NSObjectProtocol)?](filemanager/ubiquityidentitytoken.md)
  An opaque token that represents the current user’s iCloud Drive Documents identity.
- [func url(forUbiquityContainerIdentifier: String?) -> URL?](filemanager/url(forubiquitycontaineridentifier:).md)
  Returns the URL for the iCloud container associated with the specified identifier and establishes access to that container.
- [func isUbiquitousItem(at: URL) -> Bool](filemanager/isubiquitousitem(at:).md)
  Returns a Boolean indicating whether the item is targeted for storage in iCloud.
- [func setUbiquitous(Bool, itemAt: URL, destinationURL: URL) throws](filemanager/setubiquitous(_:itemat:destinationurl:).md)
  Indicates whether the item at the specified URL should be stored in iCloud.
- [func startDownloadingUbiquitousItem(at: URL) throws](filemanager/startdownloadingubiquitousitem(at:).md)
  Starts downloading (if necessary) the specified item to the local system.
- [func evictUbiquitousItem(at: URL) throws](filemanager/evictubiquitousitem(at:).md)
  Removes the local copy of the specified item that’s stored in iCloud.
- [func url(forPublishingUbiquitousItemAt: URL, expiration: AutoreleasingUnsafeMutablePointer<NSDate?>?) throws -> URL](filemanager/url(forpublishingubiquitousitemat:expiration:).md)
  Returns a URL that can be emailed to users to allow them to download a copy of a flat file item from iCloud.
### Accessing file provider services
- [func getFileProviderServicesForItem(at: URL, completionHandler: ([NSFileProviderServiceName : NSFileProviderService]?, (any Error)?) -> Void)](filemanager/getfileproviderservicesforitem(at:completionhandler:).md)
  Returns the services provided by the File Provider extension that manages the item at the given URL.
- [class NSFileProviderService](nsfileproviderservice.md)
  A service that provides a custom communication channel between your app and a File Provider extension.
- [struct NSFileProviderServiceName](nsfileproviderservicename.md)
  The name used to identify a File Provider service.
### Controlling file provider synchronization
- [struct NSFileManagerSupportedSyncControls](nsfilemanagersupportedsynccontrols.md)
  An option set of the sync controls available for an item.
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
### Creating symbolic and hard links
- [func createSymbolicLink(at: URL, withDestinationURL: URL) throws](filemanager/createsymboliclink(at:withdestinationurl:).md)
  Creates a symbolic link at the specified URL that points to an item at the given URL.
- [func createSymbolicLink(atPath: String, withDestinationPath: String) throws](filemanager/createsymboliclink(atpath:withdestinationpath:).md)
  Creates a symbolic link that points to the specified destination.
- [func linkItem(at: URL, to: URL) throws](filemanager/linkitem(at:to:).md)
  Creates a hard link between the items at the specified URLs.
- [func linkItem(atPath: String, toPath: String) throws](filemanager/linkitem(atpath:topath:).md)
  Creates a hard link between the items at the specified paths.
- [func destinationOfSymbolicLink(atPath: String) throws -> String](filemanager/destinationofsymboliclink(atpath:).md)
  Returns the path of the item pointed to by a symbolic link.
### Determining access to files
- [func fileExists(atPath: String) -> Bool](filemanager/fileexists(atpath:).md)
  Returns a Boolean value that indicates whether a file or directory exists at a specified path.
- [func fileExists(atPath: String, isDirectory: UnsafeMutablePointer<ObjCBool>?) -> Bool](filemanager/fileexists(atpath:isdirectory:).md)
  Returns a Boolean value that indicates whether a file or directory exists at a specified path.
- [func isReadableFile(atPath: String) -> Bool](filemanager/isreadablefile(atpath:).md)
  Returns a Boolean value that indicates whether the invoking object appears able to read a specified file.
- [func isWritableFile(atPath: String) -> Bool](filemanager/iswritablefile(atpath:).md)
  Returns a Boolean value that indicates whether the invoking object appears able to write to a specified file.
- [func isExecutableFile(atPath: String) -> Bool](filemanager/isexecutablefile(atpath:).md)
  Returns a Boolean value that indicates whether the operating system appears able to execute a specified file.
- [func isDeletableFile(atPath: String) -> Bool](filemanager/isdeletablefile(atpath:).md)
  Returns a Boolean value that indicates whether the invoking object appears able to delete a specified file.
### Getting and setting attributes
- [func componentsToDisplay(forPath: String) -> [String]?](filemanager/componentstodisplay(forpath:).md)
  Returns an array of strings representing the user-visible components of a given path.
- [func displayName(atPath: String) -> String](filemanager/displayname(atpath:).md)
  Returns the display name of the file or directory at a specified path.
- [func attributesOfItem(atPath: String) throws -> [FileAttributeKey : Any]](filemanager/attributesofitem(atpath:).md)
  Returns the attributes of the item at a given path.
- [func attributesOfFileSystem(forPath: String) throws -> [FileAttributeKey : Any]](filemanager/attributesoffilesystem(forpath:).md)
  Returns a dictionary that describes the attributes of the mounted file system on which a given path resides.
- [func setAttributes([FileAttributeKey : Any], ofItemAtPath: String) throws](filemanager/setattributes(_:ofitematpath:).md)
  Sets the attributes of the specified file or directory.
### Getting and comparing file contents
- [func contents(atPath: String) -> Data?](filemanager/contents(atpath:).md)
  Returns the contents of the file at the specified path.
- [func contentsEqual(atPath: String, andPath: String) -> Bool](filemanager/contentsequal(atpath:andpath:).md)
  Returns a Boolean value that indicates whether the files or directories in specified paths have the same contents.
### Getting the relationship between items
- [func getRelationship(UnsafeMutablePointer<FileManager.URLRelationship>, ofDirectoryAt: URL, toItemAt: URL) throws](filemanager/getrelationship(_:ofdirectoryat:toitemat:).md)
  Determines the type of relationship that exists between a directory and an item.
- [func getRelationship(UnsafeMutablePointer<FileManager.URLRelationship>, of: FileManager.SearchPathDirectory, in: FileManager.SearchPathDomainMask, toItemAt: URL) throws](filemanager/getrelationship(_:of:in:toitemat:).md)
  Determines the type of relationship that exists between a system directory and the specified item.
- [FileManager.URLRelationship](filemanager/urlrelationship.md)
  Constants indicating the relationship between a directory and an item.
### Converting file paths to strings
- [func fileSystemRepresentation(withPath: String) -> UnsafePointer<CChar>](filemanager/filesystemrepresentation(withpath:).md)
  Returns a C-string representation of a given path that properly encodes Unicode strings for use by the file system.
- [func string(withFileSystemRepresentation: UnsafePointer<CChar>, length: Int) -> String](filemanager/string(withfilesystemrepresentation:length:).md)
  Returns an [`NSString`](nsstring.md) object whose contents are derived from the specified C-string path.
### Managing the delegate
- [var delegate: (any FileManagerDelegate)?](filemanager/delegate.md)
  The delegate of the file manager object.
### Managing the current directory
- [func changeCurrentDirectoryPath(String) -> Bool](filemanager/changecurrentdirectorypath(_:).md)
  Changes the path of the current working directory to the specified path.
- [var currentDirectoryPath: String](filemanager/currentdirectorypath.md)
  The path to the program’s current directory.
### Unmounting volumes
- [func unmountVolume(at: URL, options: FileManager.UnmountOptions, completionHandler: ((any Error)?) -> Void)](filemanager/unmountvolume(at:options:completionhandler:).md)
  Starts the process of unmounting the specified volume.
- [FileManager.UnmountOptions](filemanager/unmountoptions.md)
  Options that specify the behavior of an unmount operation.
- [let NSFileManagerUnmountDissentingProcessIdentifierErrorKey: String](nsfilemanagerunmountdissentingprocessidentifiererrorkey.md)
  The process identifier of the process that prevented a volume from unmounting.
### Working with HFS file types
- [func NSFileTypeForHFSTypeCode(OSType) -> String!](nsfiletypeforhfstypecode(_:).md)
  Returns a string encoding a file type code.
- [func NSHFSTypeCodeFromFileType(String!) -> OSType](nshfstypecodefromfiletype(_:).md)
  Returns a file type code.
- [func NSHFSTypeOfFile(String!) -> String!](nshfstypeoffile(_:).md)
  Returns a string encoding a file type.
### Determining resource fork support
- [var NSFoundationVersionWithFileManagerResourceForkSupport: Int32](nsfoundationversionwithfilemanagerresourceforksupport.md)
  The version of the Foundation framework in which `NSFileManager` first supported resource forks.
### Supporting Types
- [FileManager.DirectoryEnumerationOptions](filemanager/directoryenumerationoptions.md)
  Options for enumerating the contents of directories.
- [FileManager.SearchPathDirectory](filemanager/searchpathdirectory.md)
  The location of significant directories.
- [FileManager.SearchPathDomainMask](filemanager/searchpathdomainmask.md)
  Domain constants specifying base locations to use when you search for significant directories.
- [struct FileAttributeKey](fileattributekey.md)
  Keys in dictionaries used to get and set file attributes.
- [struct FileAttributeType](fileattributetype.md)
  Values representing a file’s type attribute.
- [struct FileProtectionType](fileprotectiontype.md)
  Protection level values that can be associated with a file attribute key.
- [struct URLFileProtection](urlfileprotection.md)
  Protection-level values for a URL resource key.
### Notifications
- [static let NSUbiquityIdentityDidChange: NSNotification.Name](nsnotification/name-swift.struct/nsubiquityidentitydidchange.md)
  Sent after the iCloud (“ubiquity”) identity has changed.
### Deprecated Methods
- [func changeFileAttributes([AnyHashable : Any], atPath: String) -> Bool](filemanager/changefileattributes(_:atpath:).md)
  Changes the attributes of a given file or directory.
- [func fileAttributes(atPath: String, traverseLink: Bool) -> [AnyHashable : Any]?](filemanager/fileattributes(atpath:traverselink:).md)
  Returns a dictionary that describes the POSIX attributes of the file specified at a given.
- [func fileSystemAttributes(atPath: String) -> [AnyHashable : Any]?](filemanager/filesystemattributes(atpath:).md)
  Returns a dictionary that describes the attributes of the mounted file system on which a given path resides.
- [func directoryContents(atPath: String) -> [Any]?](filemanager/directorycontents(atpath:).md)
  Returns the directories and files (including symbolic links) contained in a given directory.
- [func createDirectory(atPath: String, attributes: [AnyHashable : Any]) -> Bool](filemanager/createdirectory(atpath:attributes:).md)
  Creates a directory (without contents) at a given path with given attributes.
- [func createSymbolicLink(atPath: String, pathContent: String) -> Bool](filemanager/createsymboliclink(atpath:pathcontent:).md)
  Creates a symbolic link identified by a given path that refers to a given location.
- [func pathContentOfSymbolicLink(atPath: String) -> String?](filemanager/pathcontentofsymboliclink(atpath:).md)
  Returns the path of the directory or file that a symbolic link at a given path refers to.
- [func fileManager(FileManager, shouldProceedAfterError: [AnyHashable : Any]) -> Bool](../ObjectiveC/NSObject-swift.class/fileManager(_:shouldProceedAfterError:).md)
  An `NSFileManager` object sends this message to its handler for each error it encounters when copying, moving, removing, or linking files or directories.
- [func fileManager(FileManager, willProcessPath: String)](../ObjectiveC/NSObject-swift.class/fileManager(_:willProcessPath:).md)
  An `NSFileManager` object sends this message to a handler immediately before attempting to move, copy, rename, or delete, or before attempting to link to a given path.
- [func replaceItemAtURL(originalItemURL: NSURL, withItemAtURL: NSURL, backupItemName: String?, options: FileManager.ItemReplacementOptions) throws -> NSURL?](filemanager/replaceitematurl(originalitemurl:withitematurl:backupitemname:options:).md)
  Replaces the contents of the item at the specified URL in a manner that ensures no data loss occurs.
### Structures
- [FileManager.UbiquityIdentityDidChangeMessage](filemanager/ubiquityidentitydidchangemessage.md)
### Instance Methods
- [func replaceItemAt(URL, withItemAt: URL, backupItemName: String?, options: FileManager.ItemReplacementOptions) throws -> NSURL?](filemanager/replaceitemat(_:withitemat:backupitemname:options:)-9qjo1.md)

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

- [Improving performance and stability when accessing the file system](improving-performance-and-stability-when-accessing-the-file-system.md)
  Prevent data loss and app crashes by interacting with the file system in a coordinated, asynchronous manner and by avoiding unnecessary disk I/O.
- [Using the file system effectively](using-the-file-system-effectively.md)
  Gain access to benefits like automatic backup or purging by using purpose-built directories provided by the system.
- [protocol FileManagerDelegate](filemanagerdelegate.md)
  The interface a file manager’s delegate uses to intervene during operations or if an error occurs.
- [About Apple File System](about-apple-file-system.md)
  Use high-level APIs to get the most out of Apple File System.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/filemanager)*