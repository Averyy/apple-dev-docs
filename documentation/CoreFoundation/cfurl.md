# CFURL

**Framework**: Core Foundation  
**Kind**: class

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
class CFURL
```

#### Overview

The `CFURL` opaque type provides facilities for creating, parsing, and dereferencing URL strings. `CFURL` is useful to applications that need to use URLs to access resources, including local files.

A `CFURL` object is composed of two parts—a base URL, which can be `NULL`, and a string that is resolved relative to the base URL. A `CFURL` object whose string is fully resolved without a base URL is considered absolute; all others are considered relative.

`CFURL` is “toll-free bridged” with its Cocoa Foundation counterpart, [`NSURL`](https://developer.apple.com/documentation/Foundation/NSURL). This means that the Core Foundation type is interchangeable in function or method calls with the bridged Foundation object. In other words, in a method where you see an `NSURL *` parameter, you can pass in a `CFURLRef`, and in a function where you see a `CFURLRef` parameter, you can pass in an `NSURL` instance. This also applies to concrete subclasses of `NSURL`. See [`Toll-Free Bridged Types`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFDesignConcepts/Articles/tollFreeBridgedTypes.html#//apple_ref/doc/uid/TP40010677) for more information on toll-free bridging.

Starting in OS X v10.6, the `CFURL` opaque type provides a facility for creating and using bookmarks. A  provides a persistent reference to a file-system resource. When you resolve a bookmark, you obtain a URL to the resource’s current location. A bookmark’s association with a file-system resource (typically a file or folder) usually continues to work if the user moves or renames the resource, or if the user relaunches your app or restarts the system.

In a macOS app that adopts App Sandbox, to gain persistent access to a file-system resource you must use a . Such a bookmark preserves, across app launches, a user’s intent to give your app access to a resource. For details on how this works, including information on the entitlements you need in your Xcode project, read [`Security-Scoped Bookmarks and Persistent Resource Access`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Security/Conceptual/AppSandboxDesignGuide/AppSandboxInDepth/AppSandboxInDepth.html#//apple_ref/doc/uid/TP40011183-CH3-SW16) in [`App Sandbox Design Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Security/Conceptual/AppSandboxDesignGuide/AboutAppSandbox/AboutAppSandbox.html#//apple_ref/doc/uid/TP40011183).

When you resolve a security-scoped bookmark, you get a security-scoped URL. The file system resource that the URL points to is not available for use inside your app’s sandbox until you call the [`CFURLStartAccessingSecurityScopedResource(_:)`](cfurlstartaccessingsecurityscopedresource(_:).md) function (or its Cocoa equivalent, the [`startAccessingSecurityScopedResource()`](https://developer.apple.com/documentation/foundation/nsurl/1417051-startaccessingsecurityscopedreso) method) on the URL.

When you no longer need access to a resource that you obtained using security scope (typically, after you close the resource) you must call the [`CFURLStopAccessingSecurityScopedResource(_:)`](cfurlstopaccessingsecurityscopedresource(_:).md) method (or its Cocoa equivalent, the [`stopAccessingSecurityScopedResource()`](https://developer.apple.com/documentation/foundation/nsurl/1413736-stopaccessingsecurityscopedresou) method) on the resource’s URL.

> ⚠️ **Warning**:  You must balance every call to the [`CFURLStartAccessingSecurityScopedResource(_:)`](cfurlstartaccessingsecurityscopedresource(_:).md) method with a corresponding call to the [`CFURLStopAccessingSecurityScopedResource(_:)`](cfurlstopaccessingsecurityscopedresource(_:).md) method. If you fail to relinquish your access when you no longer need a file-system resource, your app leaks kernel resources. If sufficient kernel resources are leaked, your app loses its ability to add file-system locations to its sandbox, such as via Powerbox or security-scoped bookmarks, until relaunched.

 You must balance every call to the [`CFURLStartAccessingSecurityScopedResource(_:)`](cfurlstartaccessingsecurityscopedresource(_:).md) method with a corresponding call to the [`CFURLStopAccessingSecurityScopedResource(_:)`](cfurlstopaccessingsecurityscopedresource(_:).md) method. If you fail to relinquish your access when you no longer need a file-system resource, your app leaks kernel resources. If sufficient kernel resources are leaked, your app loses its ability to add file-system locations to its sandbox, such as via Powerbox or security-scoped bookmarks, until relaunched.

The functions for using security-scoped bookmarks are described in this document in Working with Bookmark Data. For a general introduction to using bookmarks in macOS, read [`Locating Files Using Bookmarks`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/FileManagement/Conceptual/FileSystemProgrammingGuide/AccessingFilesandDirectories/AccessingFilesandDirectories.html#//apple_ref/doc/uid/TP40010672-CH3-SW10) in [`File System Programming Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/FileManagement/Conceptual/FileSystemProgrammingGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40010672).

When you copy a security-scoped URL (as obtained from a security-scoped bookmark), the copy has the security scope of the original. You gain access to the file-system resource (that the URL points to) just as you would with the original URL: by calling the [`CFURLStartAccessingSecurityScopedResource(_:)`](cfurlstartaccessingsecurityscopedresource(_:).md) function (or its Cocoa equivalent).

If you need a security-scoped URL’s path as a string value (as provided by the [`CFURLGetString(_:)`](cfurlgetstring(_:).md) function), such as to provide to an API that requires a string value, obtain the path from the URL as needed. Note, however, that a string-based path obtained from a security-scoped URL  have security scope and you cannot use that string to obtain access a security-scoped resource.

`CFURL` fails to create an object if the string passed is not well-formed (that is, if it does not comply with RFC 2396). Examples of cases that will not succeed are strings containing space characters and high-bit characters. If a function fails to create a `CFURL` object, it returns `NULL`, which you must be prepared to handle. If you create `CFURL` objects using file system paths, you should use the [`CFURLCreateFromFileSystemRepresentation(_:_:_:_:)`](cfurlcreatefromfilesystemrepresentation(_:_:_:_:).md) and [`CFURLCreateFromFileSystemRepresentationRelativeToBase(_:_:_:_:_:)`](cfurlcreatefromfilesystemrepresentationrelativetobase(_:_:_:_:_:).md) functions, which handle the subtle differences between URL paths and file system paths.

For functions that read and write data from a URL, see [`Core Foundation URL Access Utilities`](core-foundation-url-access-utilities.md)

## Topics

### Creating a CFURL
- [func CFURLCopyAbsoluteURL(CFURL!) -> CFURL!](cfurlcopyabsoluteurl(_:).md)
  Creates a new `CFURL` object by resolving the relative portion of a URL against its base.
- [func CFURLCreateAbsoluteURLWithBytes(CFAllocator!, UnsafePointer<UInt8>!, CFIndex, CFStringEncoding, CFURL!, Bool) -> CFURL!](cfurlcreateabsoluteurlwithbytes(_:_:_:_:_:_:).md)
  Creates a new `CFURL` object by resolving the relative portion of a URL, specified as bytes, against its given base URL.
- [func CFURLCreateByResolvingBookmarkData(CFAllocator!, CFData!, CFURLBookmarkResolutionOptions, CFURL!, CFArray!, UnsafeMutablePointer<DarwinBoolean>!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Unmanaged<CFURL>!](cfurlcreatebyresolvingbookmarkdata(_:_:_:_:_:_:_:).md)
  Returns a new URL made by resolving bookmark data.
- [func CFURLCreateCopyAppendingPathComponent(CFAllocator!, CFURL!, CFString!, Bool) -> CFURL!](cfurlcreatecopyappendingpathcomponent(_:_:_:_:).md)
  Creates a copy of a given URL and appends a path component.
- [func CFURLCreateCopyAppendingPathExtension(CFAllocator!, CFURL!, CFString!) -> CFURL!](cfurlcreatecopyappendingpathextension(_:_:_:).md)
  Creates a copy of a given URL and appends a path extension.
- [func CFURLCreateCopyDeletingLastPathComponent(CFAllocator!, CFURL!) -> CFURL!](cfurlcreatecopydeletinglastpathcomponent(_:_:).md)
  Creates a copy of a given URL with the last path component deleted.
- [func CFURLCreateCopyDeletingPathExtension(CFAllocator!, CFURL!) -> CFURL!](cfurlcreatecopydeletingpathextension(_:_:).md)
  Creates a copy of a given URL with its last path extension removed.
- [func CFURLCreateFilePathURL(CFAllocator!, CFURL!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Unmanaged<CFURL>!](cfurlcreatefilepathurl(_:_:_:).md)
  Returns a new file path URL that refers to the same resource as a specified URL.
- [func CFURLCreateFileReferenceURL(CFAllocator!, CFURL!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Unmanaged<CFURL>!](cfurlcreatefilereferenceurl(_:_:_:).md)
  Returns a new file reference URL that points to the same resource as a specified URL.
- [func CFURLCreateFromFileSystemRepresentation(CFAllocator!, UnsafePointer<UInt8>!, CFIndex, Bool) -> CFURL!](cfurlcreatefromfilesystemrepresentation(_:_:_:_:).md)
  Creates a new `CFURL` object for a file system entity using the native representation.
- [func CFURLCreateFromFileSystemRepresentationRelativeToBase(CFAllocator!, UnsafePointer<UInt8>!, CFIndex, Bool, CFURL!) -> CFURL!](cfurlcreatefromfilesystemrepresentationrelativetobase(_:_:_:_:_:).md)
  Creates a `CFURL` object from a native character string path relative to a base URL.
- [func CFURLCreateFromFSRef(CFAllocator!, OpaquePointer!) -> CFURL!](cfurlcreatefromfsref(_:_:).md)
  Creates a URL from a given directory or file.
- [func CFURLCreateWithBytes(CFAllocator!, UnsafePointer<UInt8>!, CFIndex, CFStringEncoding, CFURL!) -> CFURL!](cfurlcreatewithbytes(_:_:_:_:_:).md)
  Creates a `CFURL` object using a given character bytes.
- [func CFURLCreateWithFileSystemPath(CFAllocator!, CFString!, CFURLPathStyle, Bool) -> CFURL!](cfurlcreatewithfilesystempath(_:_:_:_:).md)
  Creates a `CFURL` object using a local file system path string.
- [func CFURLCreateWithFileSystemPathRelativeToBase(CFAllocator!, CFString!, CFURLPathStyle, Bool, CFURL!) -> CFURL!](cfurlcreatewithfilesystempathrelativetobase(_:_:_:_:_:).md)
  Creates a `CFURL` object using a local file system path string relative to a base URL.
- [func CFURLCreateWithString(CFAllocator!, CFString!, CFURL!) -> CFURL!](cfurlcreatewithstring(_:_:_:).md)
  Creates a `CFURL` object using a given `CFString` object.
### Accessing the Parts of a URL
- [func CFURLCanBeDecomposed(CFURL!) -> Bool](cfurlcanbedecomposed(_:).md)
  Determines if the given URL conforms to RFC 1808 and therefore can be decomposed.
- [func CFURLCopyFileSystemPath(CFURL!, CFURLPathStyle) -> CFString!](cfurlcopyfilesystempath(_:_:).md)
  Returns the path portion of a given URL.
- [func CFURLCopyFragment(CFURL!, CFString!) -> CFString!](cfurlcopyfragment(_:_:).md)
  Returns the fragment from a given URL.
- [func CFURLCopyHostName(CFURL!) -> CFString!](cfurlcopyhostname(_:).md)
  Returns the host name of a given URL.
- [func CFURLCopyLastPathComponent(CFURL!) -> CFString!](cfurlcopylastpathcomponent(_:).md)
  Returns the last path component of a given URL.
- [func CFURLCopyNetLocation(CFURL!) -> CFString!](cfurlcopynetlocation(_:).md)
  Returns the net location portion of a given URL.
- [func CFURLCopyParameterString(CFURL!, CFString!) -> CFString!](cfurlcopyparameterstring(_:_:).md)
  Returns the parameter string from a given URL.
- [func CFURLCopyPassword(CFURL!) -> CFString!](cfurlcopypassword(_:).md)
  Returns the password of a given URL.
- [func CFURLCopyPath(CFURL!) -> CFString!](cfurlcopypath(_:).md)
  Returns the path portion of a given URL.
- [func CFURLCopyPathExtension(CFURL!) -> CFString!](cfurlcopypathextension(_:).md)
  Returns the path extension of a given URL.
- [func CFURLCopyQueryString(CFURL!, CFString!) -> CFString!](cfurlcopyquerystring(_:_:).md)
  Returns the query string of a given URL.
- [func CFURLCopyResourceSpecifier(CFURL!) -> CFString!](cfurlcopyresourcespecifier(_:).md)
  Returns any additional resource specifiers after the path.
- [func CFURLCopyScheme(CFURL!) -> CFString!](cfurlcopyscheme(_:).md)
  Returns the scheme portion of a given URL.
- [func CFURLCopyStrictPath(CFURL!, UnsafeMutablePointer<DarwinBoolean>!) -> CFString!](cfurlcopystrictpath(_:_:).md)
  Returns the path portion of a given URL.
- [func CFURLCopyUserName(CFURL!) -> CFString!](cfurlcopyusername(_:).md)
  Returns the user name from a given URL.
- [func CFURLGetPortNumber(CFURL!) -> Int32](cfurlgetportnumber(_:).md)
  Returns the port number from a given URL.
- [func CFURLHasDirectoryPath(CFURL!) -> Bool](cfurlhasdirectorypath(_:).md)
  Determines if a given URL’s path represents a directory.
### Converting URLs to Other Representations
- [func CFURLCreateData(CFAllocator!, CFURL!, CFStringEncoding, Bool) -> CFData!](cfurlcreatedata(_:_:_:_:).md)
  Creates a `CFData` object containing the content of a given URL.
- [func CFURLCreateStringByAddingPercentEscapes(CFAllocator!, CFString!, CFString!, CFString!, CFStringEncoding) -> CFString!](cfurlcreatestringbyaddingpercentescapes(_:_:_:_:_:).md)
  Creates a copy of a string, replacing certain characters with the equivalent percent escape sequence based on the specified encoding.
- [func CFURLCreateStringByReplacingPercentEscapes(CFAllocator!, CFString!, CFString!) -> CFString!](cfurlcreatestringbyreplacingpercentescapes(_:_:_:).md)
  Creates a new string by replacing any percent escape sequences with their character equivalent.
- [func CFURLCreateStringByReplacingPercentEscapesUsingEncoding(CFAllocator!, CFString!, CFString!, CFStringEncoding) -> CFString!](cfurlcreatestringbyreplacingpercentescapesusingencoding(_:_:_:_:).md)
  Creates a new string by replacing any percent escape sequences with their character equivalent.
- [func CFURLGetFileSystemRepresentation(CFURL!, Bool, UnsafeMutablePointer<UInt8>!, CFIndex) -> Bool](cfurlgetfilesystemrepresentation(_:_:_:_:).md)
  Fills a buffer with the file system’s native string representation of a given URL’s path.
- [func CFURLGetFSRef(CFURL!, OpaquePointer!) -> Bool](cfurlgetfsref(_:_:).md)
  Converts a given URL to a file or directory object.
- [func CFURLGetString(CFURL!) -> CFString!](cfurlgetstring(_:).md)
  Returns the URL as a `CFString` object.
### Getting URL Properties
- [func CFURLGetBaseURL(CFURL!) -> CFURL!](cfurlgetbaseurl(_:).md)
  Returns the base URL of a given URL if it exists.
- [func CFURLGetBytes(CFURL!, UnsafeMutablePointer<UInt8>!, CFIndex) -> CFIndex](cfurlgetbytes(_:_:_:).md)
  Returns by reference the byte representation of a URL object.
- [func CFURLGetByteRangeForComponent(CFURL!, CFURLComponentType, UnsafeMutablePointer<CFRange>!) -> CFRange](cfurlgetbyterangeforcomponent(_:_:_:).md)
  Returns the range of the specified component in the bytes of a URL.
- [func CFURLGetTypeID() -> CFTypeID](cfurlgettypeid().md)
  Returns the type identifier for the `CFURL` opaque type.
- [func CFURLResourceIsReachable(CFURL!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](cfurlresourceisreachable(_:_:).md)
  Returns whether the resource pointed to by a file URL can be reached.
### Getting and Setting File System Resource Properties
- [func CFURLClearResourcePropertyCache(CFURL!)](cfurlclearresourcepropertycache(_:).md)
  Removes all cached resource values and temporary resource values from the URL object.
- [func CFURLClearResourcePropertyCacheForKey(CFURL!, CFString!)](cfurlclearresourcepropertycacheforkey(_:_:).md)
  Removes the cached resource value identified by a given key from the URL object.
- [func CFURLCopyResourcePropertiesForKeys(CFURL!, CFArray!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Unmanaged<CFDictionary>!](cfurlcopyresourcepropertiesforkeys(_:_:_:).md)
  Returns the resource values for the properties identified by specified array of keys.
- [func CFURLCopyResourcePropertyForKey(CFURL!, CFString!, UnsafeMutableRawPointer!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](cfurlcopyresourcepropertyforkey(_:_:_:_:).md)
  Returns the value of a given resource property of a given URL.
- [func CFURLCreateResourcePropertiesForKeysFromBookmarkData(CFAllocator!, CFArray!, CFData!) -> Unmanaged<CFDictionary>!](cfurlcreateresourcepropertiesforkeysfrombookmarkdata(_:_:_:).md)
  Returns the resource values for properties identified by a specified array of keys contained in specified bookmark data.
- [func CFURLCreateResourcePropertyForKeyFromBookmarkData(CFAllocator!, CFString!, CFData!) -> Unmanaged<CFTypeRef>!](cfurlcreateresourcepropertyforkeyfrombookmarkdata(_:_:_:).md)
  Returns the value of a resource property from specified bookmark data.
- [func CFURLSetResourcePropertiesForKeys(CFURL!, CFDictionary!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](cfurlsetresourcepropertiesforkeys(_:_:_:).md)
  Sets the URL’s resource properties for a given set of keys to a given set of values.
- [func CFURLSetResourcePropertyForKey(CFURL!, CFString!, CFTypeRef!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](cfurlsetresourcepropertyforkey(_:_:_:_:).md)
  Sets the URL’s resource property for a given key to a given value.
- [func CFURLSetTemporaryResourcePropertyForKey(CFURL!, CFString!, CFTypeRef!)](cfurlsettemporaryresourcepropertyforkey(_:_:_:).md)
  Sets a temporary resource value on the URL.
### Working with Bookmark Data
- [func CFURLCreateBookmarkData(CFAllocator!, CFURL!, CFURLBookmarkCreationOptions, CFArray!, CFURL!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Unmanaged<CFData>!](cfurlcreatebookmarkdata(_:_:_:_:_:_:).md)
  Returns bookmark data for a URL, created with specified options and resource values.
- [func CFURLCreateBookmarkDataFromAliasRecord(CFAllocator!, CFData!) -> Unmanaged<CFData>!](cfurlcreatebookmarkdatafromaliasrecord(_:_:).md)
  Initializes and returns bookmark data derived from an alias record.
- [func CFURLCreateBookmarkDataFromFile(CFAllocator!, CFURL!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Unmanaged<CFData>!](cfurlcreatebookmarkdatafromfile(_:_:_:).md)
  Initializes and returns bookmark data derived from a file pointed to by a specified URL.
- [func CFURLWriteBookmarkDataToFile(CFData!, CFURL!, CFURLBookmarkFileCreationOptions, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](cfurlwritebookmarkdatatofile(_:_:_:_:).md)
  Creates an alias file on disk at a specified location with specified bookmark data.
- [func CFURLStartAccessingSecurityScopedResource(CFURL!) -> Bool](cfurlstartaccessingsecurityscopedresource(_:).md)
  In an app that has adopted App Sandbox, makes the resource pointed to by a security-scoped URL available to the app.
- [func CFURLStopAccessingSecurityScopedResource(CFURL!)](cfurlstopaccessingsecurityscopedresource(_:).md)
  In an app that adopts App Sandbox, revokes access to the resource pointed to by a security-scoped URL.
### Bookmark Data Types
- [struct CFURLBookmarkCreationOptions](cfurlbookmarkcreationoptions.md)
  Type for bookmark data creation options.
- [typealias CFURLBookmarkFileCreationOptions](cfurlbookmarkfilecreationoptions.md)
  Type for bookmark file creation options.
- [struct CFURLBookmarkResolutionOptions](cfurlbookmarkresolutionoptions.md)
  Type for bookmark data resolution options.
### Bookmark Data Constants
- [Bookmark Data Creation Options](bookmark-data-creation-options.md)
  Options used when creating bookmark data.
- [Bookmark Data Resolution Options](bookmark-data-resolution-options.md)
  Options used when resolving bookmark data.
### File System Constants
- [Common File System Resource Keys](common-file-system-resource-keys.md)
  Keys that are applicable to file system URLs.
- [File Resource Types](file-resource-types.md)
  Possible values for the [`kCFURLFileResourceTypeKey`](kcfurlfileresourcetypekey.md) key.
- [File Property Keys](file-property-keys.md)
  Keys that apply to properties of files.
- [iCloud Constants](icloud-constants.md)
  These constants can be used to determining whether a file is stored in the cloud and to obtain information about its status.
- [Volume Property Keys](volume-property-keys.md)
  Keys that apply to volumes.
- [CFError userInfo Dictionary Keys](cferror-userinfo-dictionary-keys.md)
  Keys in the userInfo dictionary of a `CFError` object when certain CFURL functions return an error.
### Miscellaneous
- [enum CFURLComponentType](cfurlcomponenttype.md)
  The types of components in a URL.
- [enum CFURLPathStyle](cfurlpathstyle.md)
  Options you can use to determine how CFURL functions parse a file system path name.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)

## See Also

- [class CFAllocator](cfallocator.md)
- [class CFArray](cfarray.md)
- [class CFAttributedString](cfattributedstring.md)
- [class CFBag](cfbag.md)
- [class CFBinaryHeap](cfbinaryheap.md)
- [class CFBitVector](cfbitvector.md)
- [class CFBoolean](cfboolean.md)
- [class CFBundle](cfbundle.md)
- [class CFCalendar](cfcalendar.md)
- [class CFCharacterSet](cfcharacterset.md)
- [class CFData](cfdata.md)
- [class CFDate](cfdate.md)
- [class CFDateFormatter](cfdateformatter.md)
- [class CFDictionary](cfdictionary.md)
- [class CFError](cferror.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfurl)*