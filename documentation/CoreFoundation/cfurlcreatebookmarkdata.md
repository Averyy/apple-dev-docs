# CFURLCreateBookmarkData(_:_:_:_:_:_:)

**Framework**: Core Foundation  
**Kind**: func

Returns bookmark data for a URL, created with specified options and resource values.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.6+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func CFURLCreateBookmarkData(_ allocator: CFAllocator!, _ url: CFURL!, _ options: CFURLBookmarkCreationOptions, _ resourcePropertiesToInclude: CFArray!, _ relativeToURL: CFURL!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Unmanaged<CFData>!
```

#### Return Value

The bookmark data for the URL.

#### Discussion

To use this function to create a security-scoped bookmark to support App Sandbox, you must first have enabled the appropriate entitlements for your app, as described in [`Enabling Security-Scoped Bookmark and URL Access`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Miscellaneous/Reference/EntitlementKeyReference/Chapters/EnablingAppSandbox.html#//apple_ref/doc/uid/TP40011195-CH4-SW18). In addition, be sure to understand the behavior of the `options` and `relativeToURL` parameters.

For an app-scoped bookmark, no sandboxed app other than the one that created the bookmark can obtain access to the file-system resource that the URL (obtained from the bookmark) points to. Specifically, a bookmark created with security scope fails to resolve if the caller does not have the same code signing identity as the caller that created the bookmark.

For a document-scoped bookmark, any sandboxed app that has access to the bookmark data itself, and has access to the document that owns the bookmark, can obtain access to the resource.

> **Note**:  Security-scoped bookmarks are not available in versions of macOS prior to OS X v10.7.3.

 Security-scoped bookmarks are not available in versions of macOS prior to OS X v10.7.3.

## Parameters

- `allocator`: The allocator to use to allocate memory for the new   object. Pass   or   to use the current default allocator.
- `url`: The URL that bookmark data is being created for.
- `options`: If you instead want to create a security-scoped bookmark that, when resolved, enables you to obtain read-only access to a file-system resource, bitwise   this parameter’s value with both the   option and the   option.
- `resourcePropertiesToInclude`: In addition, the properties can contain the following collection classes:
- `relativeToURL`: If you are creating a security-scoped bookmark to support App Sandbox, use this parameter as follows:
- `error`: The error that occurred in the case that the bookmark data cannot be created.

## See Also

- [func CFURLCreateByResolvingBookmarkData(CFAllocator!, CFData!, CFURLBookmarkResolutionOptions, CFURL!, CFArray!, UnsafeMutablePointer<DarwinBoolean>!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Unmanaged<CFURL>!](cfurlcreatebyresolvingbookmarkdata(_:_:_:_:_:_:_:).md)
  Returns a new URL made by resolving bookmark data.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfurlcreatebookmarkdata(_:_:_:_:_:_:))*