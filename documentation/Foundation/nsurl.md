# NSURL

**Framework**: Foundation  
**Kind**: class

An object that represents the location of a resource, such as an item on a remote server or the path to a local file.

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
class NSURL
```

## Mentions

- [Implementing Handoff in Your App](implementing-handoff-in-your-app.md)

#### Overview

In Swift, this object bridges to [`URL`](url.md); use [`NSURL`](nsurl.md) when you need reference semantics or other Foundation-specific behavior.

You can use URL objects to construct URLs and access their parts. For URLs that represent local files, you can also manipulate properties of those files directly, such as changing the file’s last modification date. Finally, you can pass URL objects to other APIs to retrieve the contents of those URLs. For example, you can use the [`URLSession`](urlsession.md), [`NSURLConnection`](nsurlconnection.md), and [`NSURLDownload`](nsurldownload.md) classes to access the contents of remote resources, as described in [`URL Loading System`](url-loading-system.md).

URL objects are the preferred way to refer to local files. Most objects that read data from or write data to a file have methods that accept an [`NSURL`](nsurl.md) object instead of a pathname as the file reference. For example, you can get the contents of a local file URL as an `NSString` object using the [`init(contentsOfURL:encoding:)`](nsstring/init(contentsofurl:encoding:)-715fw.md) initializer, or as an `NSData` object using the [`init(contentsOfURL:options:)`](nsdata/init(contentsofurl:options:)-5abi3.md) initializer.

You can also use URLs for interapplication communication. In macOS, the [`NSWorkspace`](https://developer.apple.com/documentation/AppKit/NSWorkspace) class provides the [`open(_:)`](https://developer.apple.com/documentation/AppKit/NSWorkspace/open(_:)) method to open a location specified by a URL. Similarly, in iOS, the [`UIApplication`](https://developer.apple.com/documentation/UIKit/UIApplication) class provides the [`open(_:options:completionHandler:)`](https://developer.apple.com/documentation/UIKit/UIApplication/open(_:options:completionHandler:)) method.

Additionally, you can use URLs when working with pasteboards, as described in NSURL Additions Reference (part of the AppKit framework).

The [`NSURL`](nsurl.md) class is “toll-free bridged” with its Core Foundation counterpart, [`CFURL`](https://developer.apple.com/documentation/CoreFoundation/CFURL). See [`Toll-Free Bridging`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/General/Conceptual/CocoaEncyclopedia/Toll-FreeBridgin/Toll-FreeBridgin.html#//apple_ref/doc/uid/TP40010810-CH2) for more information on toll-free bridging.

> ❗ **Important**:  The Swift overlay to the Foundation framework provides the [`URL`](url.md) structure, which bridges to the [`NSURL`](nsurl.md) class. For more information about value types, see [`Classes and Structures`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Swift/Conceptual/Swift_Programming_Language/ClassesAndStructures.html#//apple_ref/doc/uid/TP40014097-CH13) in [`The Swift Programming Language (Swift 4.1)`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Swift/Conceptual/Swift_Programming_Language/index.html#//apple_ref/doc/uid/TP40014097) and [`Working with Cocoa Frameworks`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Swift/Conceptual/BuildingCocoaApps/WorkingWithCocoaDataTypes.html#//apple_ref/doc/uid/TP40014216-CH6) in [`Using Swift with Cocoa and Objective-C (Swift 4.1)`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Swift/Conceptual/BuildingCocoaApps/index.html#//apple_ref/doc/uid/TP40014216).

##### Structure of a Url

An [`NSURL`](nsurl.md) object is composed of two parts—a potentially `nil` base URL and a string that is resolved relative to the base URL. An [`NSURL`](nsurl.md) object is considered absolute if its string part is fully resolved without a base; all other URLs are considered relative.

For example, when constructing an `NSURL` object, you might specify `file:///path/to/user/` as the base URL and `folder/file.html` as the string part, as follows:

```objc
NSURL *baseURL = [NSURL fileURLWithPath:@"file:///path/to/user/"];
NSURL *URL = [NSURL URLWithString:@"folder/file.html" relativeToURL:baseURL];
NSLog(@"absoluteURL = %@", [URL absoluteURL]);
```

When fully resolved, the absolute URL is `file:///path/to/user/folder/file.html`.

A URL can be also be divided into pieces based on its structure. For example, the URL `https://johnny:p4ssw0rd@www.example.com:443/script.ext;param=value?query=value#ref` contains the following URL components:

| Component | Value |
| --- | --- |
| [`scheme`](nsurl/scheme.md) | `https` |
| [`user`](nsurl/user.md) | `johnny` |
| [`password`](nsurl/password.md) | `p4ssw0rd` |
| [`host`](nsurl/host.md) | `www.example.com` |
| [`port`](nsurl/port.md) | `443` |
| [`path`](nsurl/path.md) | `/script.ext` |
| [`pathExtension`](nsurl/pathextension.md) | `ext` |
| [`pathComponents`](nsurl/pathcomponents.md) | `["/", "script.ext"]` |
| [`parameterString`](nsurl/parameterstring.md) | `param=value` |
| [`query`](nsurl/query.md) | `query=value` |
| [`fragment`](nsurl/fragment.md) | `ref` |

The [`NSURL`](nsurl.md) class provides properties that let you examine each of these components.

> ❗ **Important**:  For apps linked on or after iOS 17 and aligned OS versions, [`NSURL`](nsurl.md) parsing has updated from the obsolete RFC 1738/1808 parsing to the same [`RFC 3986`](https://developer.apple.comhttps://www.ietf.org/rfc/rfc3986.txt) parsing as [`NSURLComponents`](nsurlcomponents.md). This unifies the parsing behaviors of the `NSURL` and `NSURLComponents` APIs. Now, `NSURL` automatically percent- and IDNA-encodes invalid characters to help create a valid URL. To check if a `URLString` is strictly valid according to the RFC, use the new `[NSURL URLWithString:URLString encodingInvalidCharacters:NO]` method. This method leaves all characters as they are and returns `nil` if `URLString` is explicitly invalid.

For apps linked before iOS 17, the [`NSURL`](nsurl.md) class parses URLs according to [`RFC 1808`](https://developer.apple.comhttps://tools.ietf.org/html/rfc1808), [`RFC 1738`](https://developer.apple.comhttps://tools.ietf.org/html/rfc1738), and [`RFC 2732`](https://developer.apple.comhttps://tools.ietf.org/html/rfc2732).

##### Bookmarks and Security Scope

Starting with OS X v10.6 and iOS 4.0, the [`NSURL`](nsurl.md) class provides a facility for creating and using bookmark objects. A  provides a persistent reference to a file-system resource. When you resolve a bookmark, you obtain a URL to the resource’s current location. A bookmark’s association with a file-system resource (typically a file or folder) usually continues to work if the user moves or renames the resource, or if the user relaunches your app or restarts the system.

For a general introduction to using bookmarks, read [`Locating Files Using Bookmarks`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/FileManagement/Conceptual/FileSystemProgrammingGuide/AccessingFilesandDirectories/AccessingFilesandDirectories.html#//apple_ref/doc/uid/TP40010672-CH3-SW10) in [`File System Programming Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/FileManagement/Conceptual/FileSystemProgrammingGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40010672).

In a macOS app that adopts App Sandbox, you can use  to gain access to file-system resources outside your app’s sandbox. These bookmarks preserve the user’s intent to give your app access to a resource across app launches. For details on how this works, including information on the entitlements you need in your Xcode project, read [`Security-Scoped Bookmarks and Persistent Resource Access`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Security/Conceptual/AppSandboxDesignGuide/AppSandboxInDepth/AppSandboxInDepth.html#//apple_ref/doc/uid/TP40011183-CH3-SW16) in [`App Sandbox Design Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Security/Conceptual/AppSandboxDesignGuide/AboutAppSandbox/AboutAppSandbox.html#//apple_ref/doc/uid/TP40011183). The methods for using security-scoped bookmarks are described in this document in Working with Bookmark Data.

When you resolve a security-scoped bookmark, you get a security-scoped URL.

##### Security Scoped Urls

Security-scoped URLs provide access to resources outside an app’s sandbox. In macOS, you get access to security-scoped URLs when you resolve a security-scoped bookmark. In iOS, apps that  or  documents using a [`UIDocumentPickerViewController`](https://developer.apple.com/documentation/UIKit/UIDocumentPickerViewController) also receive security-scoped URLs.

To gain access to a security-scoped URL, you must call the [`startAccessingSecurityScopedResource()`](nsurl/startaccessingsecurityscopedresource().md) method (or its Core Foundation equivalent, the [`CFURLStartAccessingSecurityScopedResource(_:)`](https://developer.apple.com/documentation/CoreFoundation/CFURLStartAccessingSecurityScopedResource(_:)) function). For iOS apps, if you use a [`UIDocument`](https://developer.apple.com/documentation/UIKit/UIDocument) to access the URL, it automatically manages the security-scoped URL for you.

If `startAccessingSecurityScopedResource` (or `CFUrLStartAccessingSecurityScopedResource`) returns [`true`](https://developer.apple.com/documentation/swift/true), you must relinquish your access by calling the [`stopAccessingSecurityScopedResource()`](nsurl/stopaccessingsecurityscopedresource().md) method (or its Core Foundation equivalent, the [`CFURLStopAccessingSecurityScopedResource(_:)`](https://developer.apple.com/documentation/CoreFoundation/CFURLStopAccessingSecurityScopedResource(_:)) function). You should relinquish your access as soon as you have finished using the file. After you call these methods, you immediately lose access to the resource in question.

> ⚠️ **Warning**:  If you fail to relinquish your access when you no longer need a file-system resource, your app leaks kernel resources. If sufficient kernel resources are leaked, your app loses its ability to add file-system locations to its sandbox, using Powerbox, security-scoped bookmarks, or similar APIs, until relaunched.

###### Security Scoped Urls and String Paths

In a macOS app, when you copy a security-scoped URL, the copy has the security scope of the original. You gain access to the file-system resource (that the URL points to) just as you would with the original URL: by calling the [`startAccessingSecurityScopedResource()`](nsurl/startaccessingsecurityscopedresource().md) method (or its Core Foundation equivalent).

If you need a security-scoped URL’s path as a string value (as provided by the [`path`](nsurl/path.md) method), such as to provide to an API that requires a string value, obtain the path from the URL as needed. Note, however, that a string-based path obtained from a security-scoped URL  have security scope and you cannot use that string to obtain access to a security-scoped resource.

##### Icloud Document Thumbnails

With OS X v10.10 and iOS 8.0, the NSURL class includes the ability to get and set document thumbnails as a resource property for iCloud documents. You can get a dictionary of [`NSImage`](https://developer.apple.com/documentation/AppKit/NSImage) objects in macOS or [`UIImage`](https://developer.apple.com/documentation/UIKit/UIImage) objects in iOS using the [`getResourceValue(_:forKey:)`](nsurl/getresourcevalue(_:forkey:).md) or [`getPromisedItemResourceValue(_:forKey:)`](nsurl/getpromiseditemresourcevalue(_:forkey:).md) methods.

In macOS, you can set a dictionary of thumbnails using the [`setResourceValue(_:forKey:)`](nsurl/setresourcevalue(_:forkey:).md) method. You can also get or set all the thumbnails as an `NSImage` object with multiple representations by using the [`thumbnailKey`](urlresourcekey/thumbnailkey.md).

> **Note**:  Do not set the [`thumbnailDictionaryKey`](urlresourcekey/thumbnaildictionarykey.md) key directly. Modifying this key interferes with document tracking and can create duplicates of your document, as well as other possible problems. In iOS, use a [`UIDocument`](https://developer.apple.com/documentation/UIKit/UIDocument) subclass to manage your file. Set the thumbnail by overriding the document’s [`fileAttributesToWrite(to:for:)`](https://developer.apple.com/documentation/UIKit/UIDocument/fileAttributesToWrite(to:for:)) method and returning a dictionary that contains the proper thumbnail keys (along with any other file attributes). In macOS, follow the instructions for creating thumbnails given in [`Quick Look Programming Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/Quicklook_Programming_Guide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40005020).

> **Note**:  Although the thumbnail API is designed to support multiple image resolutions, currently it only supports 1024 x 1024 pixel thumbnails.

## Topics

### Creating a URL object
- [convenience init?(string: String)](nsurl/init(string:).md)
  Initializes an NSURL object with a provided URL string.
- [convenience init?(string: String, encodingInvalidCharacters: Bool)](nsurl/init(string:encodinginvalidcharacters:).md)
  Creates an instance from the provided string, optionally IDNA- and percent-encoding any invalid characters.
- [init?(string: String, relativeTo: URL?)](nsurl/init(string:relativeto:).md)
  Initializes an NSURL object with a base URL and a relative string.
- [class func fileURL(withPath: String, isDirectory: Bool) -> URL](nsurl/fileurl(withpath:isdirectory:).md)
  Initializes and returns a newly created NSURL object as a file URL with a specified path.
- [init(fileURLWithPath: String, isDirectory: Bool)](nsurl/init(fileurlwithpath:isdirectory:).md)
  Initializes a newly created NSURL referencing the local file or directory at `path`.
- [class func fileURL(withPath: String, relativeTo: URL?) -> URL](nsurl/fileurl(withpath:relativeto:).md)
- [init(fileURLWithPath: String, relativeTo: URL?)](nsurl/init(fileurlwithpath:relativeto:).md)
- [class func fileURL(withPath: String, isDirectory: Bool, relativeTo: URL?) -> URL](nsurl/fileurl(withpath:isdirectory:relativeto:).md)
- [init(fileURLWithPath: String, isDirectory: Bool, relativeTo: URL?)](nsurl/init(fileurlwithpath:isdirectory:relativeto:).md)
- [class func fileURL(withPath: String) -> URL](nsurl/fileurl(withpath:).md)
  Initializes and returns a newly created NSURL object as a file URL with a specified path.
- [init(fileURLWithPath: String)](nsurl/init(fileurlwithpath:).md)
  Initializes a newly created NSURL referencing the local file or directory at `path`.
- [class func fileURL(withPathComponents: [String]) -> URL?](nsurl/fileurl(withpathcomponents:).md)
  Initializes and returns a newly created NSURL object as a file URL with specified path components.
- [convenience init(resolvingAliasFileAt: URL, options: NSURL.BookmarkResolutionOptions) throws](nsurl/init(resolvingaliasfileat:options:).md)
  Returns a new URL made by resolving the alias file at `url`.
- [convenience init(resolvingBookmarkData: Data, options: NSURL.BookmarkResolutionOptions, relativeTo: URL?, bookmarkDataIsStale: UnsafeMutablePointer<ObjCBool>?) throws](nsurl/init(resolvingbookmarkdata:options:relativeto:bookmarkdataisstale:).md)
  Initializes a newly created NSURL that points to a location specified by resolving bookmark data.
- [class func fileURL(withFileSystemRepresentation: UnsafePointer<CChar>, isDirectory: Bool, relativeTo: URL?) -> URL](nsurl/fileurl(withfilesystemrepresentation:isdirectory:relativeto:).md)
  Returns a new URL object initialized with a C string representing a local file system path.
- [func getFileSystemRepresentation(UnsafeMutablePointer<CChar>, maxLength: Int) -> Bool](nsurl/getfilesystemrepresentation(_:maxlength:).md)
  Fills the provided buffer with a C string representing a local file system path.
- [init(fileURLWithFileSystemRepresentation: UnsafePointer<CChar>, isDirectory: Bool, relativeTo: URL?)](nsurl/init(fileurlwithfilesystemrepresentation:isdirectory:relativeto:).md)
  Initializes a URL object with a C string representing a local file system path.
- [class func absoluteURL(withDataRepresentation: Data, relativeTo: URL?) -> URL](nsurl/absoluteurl(withdatarepresentation:relativeto:).md)
- [init(absoluteURLWithDataRepresentation: Data, relativeTo: URL?)](nsurl/init(absoluteurlwithdatarepresentation:relativeto:).md)
- [init(dataRepresentation: Data, relativeTo: URL?)](nsurl/init(datarepresentation:relativeto:).md)
- [var dataRepresentation: Data](nsurl/datarepresentation.md)
### Querying an NSURL
- [func checkResourceIsReachableAndReturnError(NSErrorPointer) -> Bool](nsurl/checkresourceisreachableandreturnerror(_:).md)
  Returns whether the resource pointed to by a file URL can be reached.
- [func isFileReferenceURL() -> Bool](nsurl/isfilereferenceurl.md)
  Returns whether the URL is a file reference URL.
- [var isFileURL: Bool](nsurl/isfileurl.md)
  A boolean value that determines whether the receiver is a file URL.
### Accessing the Parts of the URL
- [var absoluteString: String?](nsurl/absolutestring.md)
  The URL string for the receiver as an absolute URL. (read-only)
- [var absoluteURL: URL?](nsurl/absoluteurl.md)
  An absolute URL that refers to the same resource as the receiver. (read-only)
- [var baseURL: URL?](nsurl/baseurl.md)
  The base URL. (read-only)
- [var fileSystemRepresentation: UnsafePointer<CChar>](nsurl/filesystemrepresentation.md)
  A C string containing the URL’s file system path. (read-only)
- [var fragment: String?](nsurl/fragment.md)
  The fragment identifier, conforming to RFC 1808. (read-only)
- [var host: String?](nsurl/host.md)
  The host, conforming to RFC 1808. (read-only)
- [var lastPathComponent: String?](nsurl/lastpathcomponent.md)
  The last path component. (read-only)
- [var parameterString: String?](nsurl/parameterstring.md)
  The parameter string conforming to RFC 1808. (read-only)
- [var password: String?](nsurl/password.md)
  The password conforming to RFC 1808. (read-only)
- [var path: String?](nsurl/path.md)
  The path, conforming to RFC 1808. (read-only)
- [var pathComponents: [String]?](nsurl/pathcomponents.md)
  An array containing the  path components. (read-only)
- [var pathExtension: String?](nsurl/pathextension.md)
  The path extension. (read-only)
- [var port: NSNumber?](nsurl/port.md)
  The port, conforming to RFC 1808.
- [var query: String?](nsurl/query.md)
  The query string, conforming to RFC 1808.
- [var relativePath: String?](nsurl/relativepath.md)
  The relative path, conforming to RFC 1808. (read-only)
- [var relativeString: String](nsurl/relativestring.md)
  A string representation of the relative portion of the URL. (read-only)
- [var resourceSpecifier: String?](nsurl/resourcespecifier.md)
  The resource specifier. (read-only)
- [var scheme: String?](nsurl/scheme.md)
  The scheme. (read-only)
- [var standardized: URL?](nsurl/standardized.md)
  A copy of the URL with any instances of `".."` or `"."` removed from its path. (read-only)
- [var user: String?](nsurl/user.md)
  The user name, conforming to RFC 1808.
### Accessing Resource Values
- [func resourceValues(forKeys: [URLResourceKey]) throws -> [URLResourceKey : Any]](nsurl/resourcevalues(forkeys:).md)
  Returns the resource values for the properties identified by specified array of keys.
- [func getResourceValue(AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey: URLResourceKey) throws](nsurl/getresourcevalue(_:forkey:).md)
  Returns the value of the resource property for the specified key.
- [func setResourceValue(Any?, forKey: URLResourceKey) throws](nsurl/setresourcevalue(_:forkey:).md)
  Sets the URL’s resource property for a given key to a given value.
- [func setResourceValues([URLResourceKey : Any]) throws](nsurl/setresourcevalues(_:).md)
  Sets the URL’s resource properties for a given set of keys to a given set of values.
- [func removeAllCachedResourceValues()](nsurl/removeallcachedresourcevalues.md)
  Removes all cached resource values and temporary resource values from the URL object.
- [func removeCachedResourceValue(forKey: URLResourceKey)](nsurl/removecachedresourcevalue(forkey:).md)
  Removes the cached resource value identified by a given key from the URL object.
- [func setTemporaryResourceValue((any Sendable)?, forKey: URLResourceKey)](nsurl/settemporaryresourcevalue(_:forkey:).md)
  Sets a temporary resource value on the URL object.
- [struct URLResourceKey](urlresourcekey.md)
  Keys that apply to file system URLs.
### Modifying and Converting a File URL
- [var filePathURL: URL?](nsurl/filepathurl.md)
  A file path URL that points to the same resource as the URL object. (read-only)
- [func fileReferenceURL() -> URL?](nsurl/filereferenceurl.md)
  Returns a new file reference URL that points to the same resource as the receiver.
- [func appendingPathComponent(String) -> URL?](nsurl/appendingpathcomponent(_:).md)
  Returns a new URL by appending a path component to the original URL.
- [func appendingPathComponent(String, isDirectory: Bool) -> URL?](nsurl/appendingpathcomponent(_:isdirectory:).md)
  Returns a new URL by appending a path component to the original URL, along with a trailing slash if the component is a directory.
- [func appendingPathComponent(String, conformingTo: UTType) -> URL](nsurl/appendingpathcomponent(_:conformingto:).md)
  Returns a URL by appending the specified path component with the file extension for a uniform type identifier.
- [func appendingPathExtension(String) -> URL?](nsurl/appendingpathextension(_:).md)
  Returns a new URL by appending a path extension to the original URL.
- [func appendingPathExtension(for: UTType) -> URL](nsurl/appendingpathextension(for:).md)
  Returns a URL by appending the path extension for a uniform type identifier.
- [var deletingLastPathComponent: URL?](nsurl/deletinglastpathcomponent.md)
  A URL you create by removing the last path component from the receiver. (read-only)
- [var deletingPathExtension: URL?](nsurl/deletingpathextension.md)
  A URL you create by removing the path extension from the receiver, if any. (read-only)
- [var resolvingSymlinksInPath: URL?](nsurl/resolvingsymlinksinpath.md)
  A URL that points to the same resource as the receiver and includes no symbolic links. (read-only)
- [var standardizingPath: URL?](nsurl/standardizingpath.md)
  A URL that points to the same resource as the original URL using an absolute path. (read-only)
- [var hasDirectoryPath: Bool](nsurl/hasdirectorypath.md)
  A Boolean value that indicates whether the URL string’s path represents a directory.
### Working with Bookmark Data
- [class func bookmarkData(withContentsOf: URL) throws -> Data](nsurl/bookmarkdata(withcontentsof:).md)
  Initializes and returns bookmark data derived from an alias file pointed to by a specified URL.
- [func bookmarkData(options: NSURL.BookmarkCreationOptions, includingResourceValuesForKeys: [URLResourceKey]?, relativeTo: URL?) throws -> Data](nsurl/bookmarkdata(options:includingresourcevaluesforkeys:relativeto:).md)
  Returns a bookmark for the URL, created with specified options and resource values.
- [class func resourceValues(forKeys: [URLResourceKey], fromBookmarkData: Data) -> [URLResourceKey : Any]?](nsurl/resourcevalues(forkeys:frombookmarkdata:).md)
  Returns the resource values for properties identified by a specified array of keys contained in specified bookmark data.
- [class func writeBookmarkData(Data, to: URL, options: NSURL.BookmarkFileCreationOptions) throws](nsurl/writebookmarkdata(_:to:options:).md)
  Creates an alias file on disk at a specified location with specified bookmark data.
- [func startAccessingSecurityScopedResource() -> Bool](nsurl/startaccessingsecurityscopedresource.md)
  In an app that has adopted App Sandbox, makes the resource pointed to by a security-scoped URL available to the app.
- [func stopAccessingSecurityScopedResource()](nsurl/stopaccessingsecurityscopedresource.md)
  In an app that adopts App Sandbox, revokes access to the resource pointed to by a security-scoped URL.
- [typealias BookmarkFileCreationOptions](nsurl/bookmarkfilecreationoptions.md)
  Options used when creating file bookmark data
- [struct BookmarkCreationOptions](nsurl/bookmarkcreationoptions.md)
  Options used when creating bookmark data.
- [struct BookmarkResolutionOptions](nsurl/bookmarkresolutionoptions.md)
  Options used when resolving bookmark data.
### Working with Promised Items
- [func checkPromisedItemIsReachableAndReturnError(NSErrorPointer) -> Bool](nsurl/checkpromiseditemisreachableandreturnerror(_:).md)
  Returns whether the promised item can be reached.
- [func getPromisedItemResourceValue(AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey: URLResourceKey) throws](nsurl/getpromiseditemresourcevalue(_:forkey:).md)
  Returns the value of the resource property for the specified key.
- [func promisedItemResourceValues(forKeys: [URLResourceKey]) throws -> [URLResourceKey : Any]](nsurl/promiseditemresourcevalues(forkeys:).md)
  Returns the resource values for the properties identified by specified array of keys.
### Working with Pasteboards
- [init?(fromPasteboard: NSPasteboard)](nsurl/init(frompasteboard:).md)
  Reads an NSURL object off of the specified pasteboard.
- [func write(to: NSPasteboard)](nsurl/write(to:).md)
  Writes the URL to the specified pasteboard.
### Using Quick Looks
- [var customPlaygroundQuickLook: PlaygroundQuickLook](nsurl/customplaygroundquicklook.md)
### Constants
- [NSURL Schemes](nsurl-schemes.md)
  The schemes that the `NSURL` class is able to parse.
- [NSError userInfo Dictionary Keys](nserror-userinfo-dictionary-keys.md)
  Keys in the userInfo dictionary of an `NSError` object when certain NSURL methods return an error.
### Deprecated
- [convenience init?(scheme: String, host: String?, path: String)](nsurl/init(scheme:host:path:).md)
  Initializes a newly created NSURL with a specified scheme, host, and path.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](nscoding.md)
- [NSCopying](nscopying.md)
- [NSItemProviderReading](nsitemproviderreading.md)
- [NSItemProviderWriting](nsitemproviderwriting.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSPasteboardReading](../AppKit/NSPasteboardReading.md)
- [NSPasteboardWriting](../AppKit/NSPasteboardWriting.md)
- [NSSecureCoding](nssecurecoding.md)
- [QLPreviewItem](../QuickLookUI/QLPreviewItem.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsurl)*