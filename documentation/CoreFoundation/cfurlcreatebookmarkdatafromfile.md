# CFURLCreateBookmarkDataFromFile(_:_:_:)

**Framework**: Core Foundation  
**Kind**: func

Initializes and returns bookmark data derived from a file pointed to by a specified URL.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.6+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func CFURLCreateBookmarkDataFromFile(_ allocator: CFAllocator!, _ fileURL: CFURL!, _ errorRef: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Unmanaged<CFData>!
```

#### Return Value

The bookmark data for the file, or `NULL` if an error occurs.

## Parameters

- `allocator`: The allocator to use to allocate memory for the new   object. Pass   or   to use the current default allocator.
- `fileURL`: The file URL.
- `errorRef`: The error that occurred in the case that the bookmark data cannot be created.

## See Also

- [func CFURLCreateBookmarkData(CFAllocator!, CFURL!, CFURLBookmarkCreationOptions, CFArray!, CFURL!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Unmanaged<CFData>!](cfurlcreatebookmarkdata(_:_:_:_:_:_:).md)
  Returns bookmark data for a URL, created with specified options and resource values.
- [func CFURLCreateBookmarkDataFromAliasRecord(CFAllocator!, CFData!) -> Unmanaged<CFData>!](cfurlcreatebookmarkdatafromaliasrecord(_:_:).md)
  Initializes and returns bookmark data derived from an alias record.
- [func CFURLWriteBookmarkDataToFile(CFData!, CFURL!, CFURLBookmarkFileCreationOptions, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](cfurlwritebookmarkdatatofile(_:_:_:_:).md)
  Creates an alias file on disk at a specified location with specified bookmark data.
- [func CFURLStartAccessingSecurityScopedResource(CFURL!) -> Bool](cfurlstartaccessingsecurityscopedresource(_:).md)
  In an app that has adopted App Sandbox, makes the resource pointed to by a security-scoped URL available to the app.
- [func CFURLStopAccessingSecurityScopedResource(CFURL!)](cfurlstopaccessingsecurityscopedresource(_:).md)
  In an app that adopts App Sandbox, revokes access to the resource pointed to by a security-scoped URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfurlcreatebookmarkdatafromfile(_:_:_:))*