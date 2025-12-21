# URL

**Framework**: Foundation  
**Kind**: struct

A value that identifies the location of a resource, such as an item on a remote server or the path to a local file.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
struct URL
```

## Mentions

- [Using the file system effectively](using-the-file-system-effectively.md)
- [Checking Volume Storage Capacity](checking-volume-storage-capacity.md)
- [Downloading files from websites](downloading-files-from-websites.md)
- [Encoding and Decoding Custom Types](encoding-and-decoding-custom-types.md)
- [Processing URL session data task results with Combine](processing-url-session-data-task-results-with-combine.md)

#### Overview

You can construct URLs and access their parts. For URLs that represent local files, you can also manipulate properties of those files directly, such as changing the file’s last modification date. Finally, you can pass URLs to other APIs to retrieve the contents of those URLs. For example, you can use [`URLSession`](urlsession.md) and its related classes to access the contents of remote resources.

URLs are the preferred way to refer to local files. Most objects that read data from or write data to a file have methods that accept a URL instead of a pathname as the file reference. For example, you can get the contents of a local file URL as [`String`](https://developer.apple.com/documentation/Swift/String) by calling [`init(contentsOf:encoding:)`](https://developer.apple.com/documentation/Swift/String/init(contentsOf:encoding:)), or as a [`Data`](data.md) by calling [`init(contentsOf:options:)`](data/init(contentsof:options:).md).

As a convenience, you can use Swift’s `async`-`await` syntax to asynchronously access the contents of a [`URL`](url.md) through the [`resourceBytes`](url/resourcebytes.md) and [`lines`](url/lines.md) properties. These properties use the shared [`URLSession`](urlsession.md) instance to load the resource.

`URL` defines a set of properties for common directories like [`documentsDirectory`](url/documentsdirectory.md) and [`cachesDirectory`](url/cachesdirectory.md), some of which have distinct behaviors for backup or automatic purging. To make the best use of these directories, see [`Using the file system effectively`](using-the-file-system-effectively.md).

## Topics

### Creating a URL from a string
- [init?(string: String)](url/init(string:).md)
  Creates a URL instance from the provided string.
- [init?(string: String, encodingInvalidCharacters: Bool)](url/init(string:encodinginvalidcharacters:).md)
  Creates a URL instance from the provided string, optionally IDNA- and percent-encoding any invalid characters.
- [init?(string: String, relativeTo: URL?)](url/init(string:relativeto:).md)
  Creates a URL instance from the provided string, relative to another URL.
- [init(resolvingBookmarkData: Data, options: URL.BookmarkResolutionOptions, relativeTo: URL?, bookmarkDataIsStale: inout Bool) throws](url/init(resolvingbookmarkdata:options:relativeto:bookmarkdataisstale:)-3ic6f.md)
  Creates a URL that refers to a location specified by resolving bookmark data.
- [init?(resolvingBookmarkData: Data, options: URL.BookmarkResolutionOptions, relativeTo: URL?, bookmarkDataIsStale: inout Bool) throws](url/init(resolvingbookmarkdata:options:relativeto:bookmarkdataisstale:)-97e6x.md)
  Initializes a URL that refers to a location specified by resolving bookmark data.
### Creating a file URL from a string path
- [init(filePath: String, directoryHint: URL.DirectoryHint, relativeTo: URL?)](url/init(filepath:directoryhint:relativeto:).md)
  Creates a file URL that references a path you specify as a string.
- [enum DirectoryHint](url/directoryhint.md)
  A hint to URL file APIs for handling paths that may reference directories.
- [init(fileURLWithPath: String)](url/init(fileurlwithpath:).md)
  Creates a file URL that references the local file or directory at the given path.
- [init(fileURLWithPath: String, isDirectory: Bool)](url/init(fileurlwithpath:isdirectory:).md)
  Creates a file URL that references the local file or directory at the given path.
- [init(fileURLWithPath: String, relativeTo: URL?)](url/init(fileurlwithpath:relativeto:).md)
  Creates a file URL that references the local file or directory at the given path, relative to a base URL.
- [init(fileURLWithPath: String, isDirectory: Bool, relativeTo: URL?)](url/init(fileurlwithpath:isdirectory:relativeto:).md)
  Creates a file URL that references the local file or directory at the given path, relative to a base URL.
- [init(fileURLWithFileSystemRepresentation: UnsafePointer<Int8>, isDirectory: Bool, relativeTo: URL?)](url/init(fileurlwithfilesystemrepresentation:isdirectory:relativeto:).md)
  Creates a file URL that references the local file or directory for the file system representation of the path.
- [init(fileReferenceLiteralResourceName: String)](url/init(filereferenceliteralresourcename:).md)
  Creates a URL from a playground file literal.
- [init?(filePath: FilePath, directoryHint: URL.DirectoryHint)](url/init(filepath:directoryhint:).md)
  Creates a file URL that references a file path.
### Creating a file URL from a file path
- [init?(FilePath)](url/init(_:).md)
  Creates a file URL that references the local file or directory at the file path you specify.
- [init?(FilePath, isDirectory: Bool)](url/init(_:isdirectory:).md)
  Creates a file URL that references the local file or directory at the file path you specify.
- [struct FilePath](../System/FilePath.md)
  Represents a location in the file system.
### Creating a file URL for a common directory
- [init(for: FileManager.SearchPathDirectory, in: FileManager.SearchPathDomainMask, appropriateFor: URL?, create: Bool) throws](url/init(for:in:appropriatefor:create:).md)
  Creates a file URL for a common directory in a domain.
- [FileManager.SearchPathDirectory](filemanager/searchpathdirectory.md)
  The location of significant directories.
- [FileManager.SearchPathDomainMask](filemanager/searchpathdomainmask.md)
  Domain constants specifying base locations to use when you search for significant directories.
### Creating a URL by resolving a bookmark
- [init(resolvingBookmarkData: Data, options: URL.BookmarkResolutionOptions, relativeTo: URL?, bookmarkDataIsStale: inout Bool) throws](url/init(resolvingbookmarkdata:options:relativeto:bookmarkdataisstale:)-3ic6f.md)
  Creates a URL that refers to a location specified by resolving bookmark data.
- [init(resolvingAliasFileAt: URL, options: URL.BookmarkResolutionOptions) throws](url/init(resolvingaliasfileat:options:).md)
  Creates a URL that refers to the location specified by resolving an alias file.
- [typealias BookmarkResolutionOptions](url/bookmarkresolutionoptions.md)
  An alias for the bookmark resolution options type.
- [struct BookmarkResolutionOptions](nsurl/bookmarkresolutionoptions.md)
  Options used when resolving bookmark data.
### Creating a URL from a resource
- [init?(resource: URLResource)](url/init(resource:).md)
  Creates a URL from a resource.
### Creating a URL by parsing
- [init<T>(T.ParseInput, strategy: T) throws](url/init(_:strategy:).md)
  Creates a URL instance by parsing the provided input in accordance with a parse strategy.
- [struct ParseStrategy](url/parsestrategy.md)
  A parse strategy for creating URLs from formatted strings.
### Accessing the parts of a URL
- [func fragment(percentEncoded: Bool) -> String?](url/fragment(percentencoded:).md)
  Returns the fragment component of the URL, optionally removing any percent-encoding.
- [var fragment: String?](url/fragment.md)
  The fragment component of the URL if the URL conforms to RFC 3986; otherwise, nil.
- [func host(percentEncoded: Bool) -> String?](url/host(percentencoded:).md)
  Returns the host component of the URL, optionally removing any percent-encoding.
- [var host: String?](url/host.md)
  The host component of a URL if the URL conforms to RFC 3986; otherwise, nil.
- [var lastPathComponent: String](url/lastpathcomponent.md)
  The last path component of the URL, or an empty string if the path is an empty string.
- [func path(percentEncoded: Bool) -> String](url/path(percentencoded:).md)
  Returns the path component of the URL, optionally removing any percent-encoding.
- [var path: String](url/path.md)
  The path component of the URL if the URL conforms to RFC 3986; otherwise, an empty string.
- [func password(percentEncoded: Bool) -> String?](url/password(percentencoded:).md)
  Returns the password component of the URL, optionally removing any percent-encoding.
- [var password: String?](url/password.md)
  The password component of the URL if the URL conforms to RFC 3986; otherwise, nil.
- [var pathComponents: [String]](url/pathcomponents.md)
  The path components of the URL, or an empty array if the path is an empty string.
- [var pathExtension: String](url/pathextension.md)
  The path extension of the URL, or an empty string if the path is an empty string.
- [var port: Int?](url/port.md)
  The port component of the URL if the URL conforms to RFC 3986; otherwise, nil.
- [func query(percentEncoded: Bool) -> String?](url/query(percentencoded:).md)
  Returns the query component of the URL, optionally removing any percent-encoding.
- [var query: String?](url/query.md)
  The query of the URL if the URL conforms to RFC 3986; otherwise, nil.
- [var scheme: String?](url/scheme.md)
  The scheme of the URL.
- [func user(percentEncoded: Bool) -> String?](url/user(percentencoded:).md)
  Returns the user component of the URL, optionally removing any percent-encoding.
- [var user: String?](url/user.md)
  The user component of the URL if the URL conforms to RFC 3986; otherwise, nil.
### Accessing URL representations
- [var baseURL: URL?](url/baseurl.md)
  The base URL.
- [var absoluteString: String](url/absolutestring.md)
  The absolute string for the URL.
- [var absoluteURL: URL](url/absoluteurl.md)
  The absolute URL.
- [var relativePath: String](url/relativepath.md)
  The relative path of the URL if the URL conforms to RFC 3986, otherwise nil.
- [var relativeString: String](url/relativestring.md)
  The relative portion of a URL.
- [var standardized: URL](url/standardized.md)
  A version of the URL with any instances of “..” or “.” resolved in its path.
- [var standardizedFileURL: URL](url/standardizedfileurl.md)
  A standardized version of the path of a file URL.
### Accessing resource values
- [func resourceValues(forKeys: Set<URLResourceKey>) throws -> URLResourceValues](url/resourcevalues(forkeys:).md)
  Returns a collection of resource values identified by the given resource keys.
- [func setResourceValues(URLResourceValues) throws](url/setresourcevalues(_:).md)
  Sets the resource value identified by a given resource key.
- [func removeCachedResourceValue(forKey: URLResourceKey)](url/removecachedresourcevalue(forkey:).md)
  Removes the cached resource value identified by a given resource value key from the URL object.
- [func removeAllCachedResourceValues()](url/removeallcachedresourcevalues.md)
  Removes all cached resource values and all temporary resource values from the URL object.
- [func setTemporaryResourceValue(any Sendable, forKey: URLResourceKey)](url/settemporaryresourcevalue(_:forkey:).md)
  Sets a temporary resource value on the URL object.
- [struct URLResourceKey](urlresourcekey.md)
  Keys that apply to file system URLs.
- [struct URLResourceValues](urlresourcevalues.md)
  The properties that the file system resources support.
### Working with the data representation of a URL
- [init?(dataRepresentation: Data, relativeTo: URL?, isAbsolute: Bool)](url/init(datarepresentation:relativeto:isabsolute:).md)
  Initializes a newly created URL using the contents of the given data, relative to a base URL.
- [var dataRepresentation: Data](url/datarepresentation.md)
  The data representation of the URL’s relativeString.
### Working with file URLs
- [var isFileURL: Bool](url/isfileurl.md)
  A Boolean that is true if the scheme is `file:`.
- [var hasDirectoryPath: Bool](url/hasdirectorypath.md)
  A Boolean that is true if the URL path represents a directory.
- [func withUnsafeFileSystemRepresentation<ResultType>((UnsafePointer<Int8>?) throws -> ResultType) rethrows -> ResultType](url/withunsafefilesystemrepresentation(_:).md)
  Passes the URL’s path in the file system representation to a closure.
- [func resolveSymlinksInPath()](url/resolvesymlinksinpath.md)
  Resolves any symlinks in the path of a file URL.
- [func resolvingSymlinksInPath() -> URL](url/resolvingsymlinksinpath.md)
  Resolves any symlinks in the path of a file URL.
- [func standardize()](url/standardize.md)
  Standardizes the path of a file URL.
### Accessing common directories
- [static var applicationDirectory: URL](url/applicationdirectory.md)
  The standard directory for apps.
- [static var applicationSupportDirectory: URL](url/applicationsupportdirectory.md)
  The standard directory for application support files.
- [static var cachesDirectory: URL](url/cachesdirectory.md)
  The standard directory for discardable cache files.
- [static var desktopDirectory: URL](url/desktopdirectory.md)
  The standard directory for files on the desktop.
- [static var documentsDirectory: URL](url/documentsdirectory.md)
  The standard directory for document files.
- [static var downloadsDirectory: URL](url/downloadsdirectory.md)
  The standard directory for download files.
- [static var libraryDirectory: URL](url/librarydirectory.md)
  The standard directory for documentation, support, and configuration files.
- [static var moviesDirectory: URL](url/moviesdirectory.md)
  The standard directory for movie files.
- [static var musicDirectory: URL](url/musicdirectory.md)
  The standard directory for music files.
- [static var picturesDirectory: URL](url/picturesdirectory.md)
  The standard directory for image files.
- [static var sharedPublicDirectory: URL](url/sharedpublicdirectory.md)
  The standard directory for publicly shared files.
- [static var temporaryDirectory: URL](url/temporarydirectory.md)
  The standard directory for temporary files.
- [static var trashDirectory: URL](url/trashdirectory.md)
  The standard trash directory.
- [static var userDirectory: URL](url/userdirectory.md)
  The container directory of user home directories.
### Accessing home and user directories
- [static func currentDirectory() -> URL](url/currentdirectory.md)
  Returns the working directory of the current process.
- [static var homeDirectory: URL](url/homedirectory.md)
  The home directory for the current user.
- [static func homeDirectory(forUser: String) -> URL?](url/homedirectory(foruser:).md)
  Returns the home directory for the specified user.
### Adding path components
- [func append<S>(path: S, directoryHint: URL.DirectoryHint)](url/append(path:directoryhint:).md)
  Appends a path to the URL, with a hint for handling directory awareness.
- [func append<S>(component: S, directoryHint: URL.DirectoryHint)](url/append(component:directoryhint:).md)
  Appends a path component to the URL, with a hint for handling directory awareness.
- [func appendPathComponent(String)](url/appendpathcomponent(_:).md)
  Appends a path component to the URL.
- [func appendPathComponent(String, isDirectory: Bool)](url/appendpathcomponent(_:isdirectory:).md)
  Appends a path component to the URL, specifying whether the resulting path is a directory.
- [func appending<S>(path: S, directoryHint: URL.DirectoryHint) -> URL](url/appending(path:directoryhint:).md)
  Returns a URL by appending the specified path to the URL, with a hint for handling directory awareness.
- [func appending<S>(component: S, directoryHint: URL.DirectoryHint) -> URL](url/appending(component:directoryhint:).md)
  Returns a URL by appending the specified path component to the URL, with a hint for handling directory awareness.
- [func appendingPathComponent(String) -> URL](url/appendingpathcomponent(_:).md)
  Returns a URL by appending the specified path component to self.
- [func appendingPathComponent(String, isDirectory: Bool) -> URL](url/appendingpathcomponent(_:isdirectory:).md)
  Returns a URL by appending the specified path component to self, specifying whether the resulting path is a directory.
- [func append<S>(components: S..., directoryHint: URL.DirectoryHint)](url/append(components:directoryhint:).md)
  Appends multiple path components to the URL, with a hint for handling directory awareness.
- [func appending<S>(components: S..., directoryHint: URL.DirectoryHint) -> URL](url/appending(components:directoryhint:).md)
  Returns a new URL by appending multiple path components to the URL, with a hint for handling directory awareness.
- [func appendPathComponent(String, conformingTo: UTType)](url/appendpathcomponent(_:conformingto:).md)
  Appends a path component to the URL that conforms to a uniform type identifier.
- [func appendingPathComponent(String, conformingTo: UTType) -> URL](url/appendingpathcomponent(_:conformingto:).md)
  Returns a URL by appending the specified path component that conforms to a uniform type identifier.
### Adding a path extension
- [func appendPathExtension(String)](url/appendpathextension(_:).md)
  Appends the specified path extension to self.
- [func appendingPathExtension(String) -> URL](url/appendingpathextension(_:).md)
  Returns a URL by appending the specified path extension to self.
- [func appendPathExtension(for: UTType)](url/appendpathextension(for:).md)
  Appends the preferred path extension for the type you specify.
- [func appendingPathExtension(for: UTType) -> URL](url/appendingpathextension(for:).md)
  Returns a URL by appending the preferred path extension for the type you specify to the URL’s last path component.
### Adding query items
- [func append(queryItems: [URLQueryItem])](url/append(queryitems:).md)
  Appends a list of query items to the URL.
- [func appending(queryItems: [URLQueryItem]) -> URL](url/appending(queryitems:).md)
  Returns a new URL formed by appending a list of query items to the URL.
- [struct URLQueryItem](urlqueryitem.md)
  A single name-value pair from the query portion of a URL.
### Removing path components
- [func deleteLastPathComponent()](url/deletelastpathcomponent.md)
  Returns a URL constructed by removing the last path component of self.
- [func deletingLastPathComponent() -> URL](url/deletinglastpathcomponent.md)
  Returns a URL constructed by removing the last path component of self.
### Removing a path extension
- [func deletePathExtension()](url/deletepathextension.md)
  Returns a URL constructed by removing any path extension.
- [func deletingPathExtension() -> URL](url/deletingpathextension.md)
  Returns a URL constructed by removing any path extension.
### Creating bookmarks
- [func bookmarkData(options: URL.BookmarkCreationOptions, includingResourceValuesForKeys: Set<URLResourceKey>?, relativeTo: URL?) throws -> Data](url/bookmarkdata(options:includingresourcevaluesforkeys:relativeto:).md)
  Returns bookmark data for the URL, created with specified options and resource values.
- [static func bookmarkData(withContentsOf: URL) throws -> Data](url/bookmarkdata(withcontentsof:).md)
  Initializes and returns bookmark data derived from an alias file pointed to by a specified URL.
- [static func writeBookmarkData(Data, to: URL) throws](url/writebookmarkdata(_:to:).md)
  Creates an alias file on disk at a specified location with specified bookmark data.
- [static func resourceValues(forKeys: Set<URLResourceKey>, fromBookmarkData: Data) -> URLResourceValues?](url/resourcevalues(forkeys:frombookmarkdata:).md)
  Returns the resource values for properties identified by a specified array of keys contained in specified bookmark data.
- [typealias BookmarkCreationOptions](url/bookmarkcreationoptions.md)
  An alias for bookmark creation options.
- [struct BookmarkCreationOptions](nsurl/bookmarkcreationoptions.md)
  Options used when creating bookmark data.
### Checking reachability
- [func checkResourceIsReachable() throws -> Bool](url/checkresourceisreachable.md)
  Returns whether the URL’s resource exists and is reachable.
### Loading URL contents asynchronously
- [var resourceBytes: URL.AsyncBytes](url/resourcebytes.md)
  The URL’s resource data, as an asynchronous sequence of bytes.
- [var lines: AsyncLineSequence<URL.AsyncBytes>](url/lines.md)
  The URL’s resource data, as an asynchronous sequence of lines of text.
- [struct AsyncBytes](url/asyncbytes.md)
  An asynchronous sequence of bytes loaded from the URL.
### Working with promised items
- [func checkPromisedItemIsReachable() throws -> Bool](url/checkpromiseditemisreachable.md)
  Returns whether the promised item URL’s resource exists and is reachable.
- [func promisedItemResourceValues(forKeys: Set<URLResourceKey>) throws -> URLResourceValues](url/promiseditemresourcevalues(forkeys:).md)
  Gets resource values from URLs of ‘promised’ items.
### Working with security scoped resources
- [func startAccessingSecurityScopedResource() -> Bool](url/startaccessingsecurityscopedresource.md)
  Given a url created by resolving a bookmark data created with security scope, make the resource referenced by the url accessible to the process.
- [func stopAccessingSecurityScopedResource()](url/stopaccessingsecurityscopedresource.md)
  Revokes the access granted to the url by a prior successful call to the complementary start function.
### Describing a URL
- [var customPlaygroundQuickLook: PlaygroundQuickLook](url/customplaygroundquicklook.md)
  A playground quicklook for the URL.
### Formatting a URL
- [func formatted() -> String](url/formatted.md)
  Formats the URL using a default format style.
- [func formatted<F>(F) -> F.FormatOutput](url/formatted(_:).md)
  Formats the URL, using the provided format style.
- [struct FormatStyle](url/formatstyle.md)
  A structure that converts between URL instances and their textual representations.
### Using reference types
- [class NSURL](nsurl.md)
  An object that represents the location of a resource, such as an item on a remote server or the path to a local file.
### App Intents support
- [static var defaultResolverSpecification: some ResolverSpecification](url/defaultresolverspecification.md)
  The default resolver specification that the App Intents framework uses.
- [typealias Specification](url/specification.md)
  The specification type for conforming with App Intents.
- [typealias UnwrappedType](url/unwrappedtype.md)
  The core type for conforming with App Intents.
- [typealias ValueType](url/valuetype.md)
  The value type for conforming with App Intents.
### Structures
- [struct Template](url/template.md)
  A template for constructing a URL from variable expansions.
### Initializers
- [init?(template: URL.Template, variables: [URL.Template.VariableName : URL.Template.Value])](url/init(template:variables:).md)
  Creates a new `URL` by expanding the RFC 6570 template and variables.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [CustomURLRepresentationParameterConvertible](../AppIntents/CustomURLRepresentationParameterConvertible.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [ReferenceConvertible](referenceconvertible.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [Transferable](../CoreTransferable/Transferable.md)

## See Also

- [struct URLComponents](urlcomponents.md)
  A structure that parses URLs into and constructs URLs from their constituent parts.
- [struct URLQueryItem](urlqueryitem.md)
  A single name-value pair from the query portion of a URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/url)*