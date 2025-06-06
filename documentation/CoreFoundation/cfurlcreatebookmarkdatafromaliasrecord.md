# CFURLCreateBookmarkDataFromAliasRecord(_:_:)

**Framework**: Core Foundation  
**Kind**: func

Initializes and returns bookmark data derived from an alias record.

**Availability**:
- macOS 10.6+

## Declaration

```swift
func CFURLCreateBookmarkDataFromAliasRecord(_ allocatorRef: CFAllocator!, _ aliasRecordDataRef: CFData!) -> Unmanaged<CFData>!
```

#### Return Value

The bookmark data for the alias record.

## Parameters

- `allocatorRef`: The allocator to use to allocate memory for the new   object. Pass   or   to use the current default allocator.
- `aliasRecordDataRef`: The alias record.

## See Also

- [func CFURLCreateBookmarkData(CFAllocator!, CFURL!, CFURLBookmarkCreationOptions, CFArray!, CFURL!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Unmanaged<CFData>!](cfurlcreatebookmarkdata(_:_:_:_:_:_:).md)
  Returns bookmark data for a URL, created with specified options and resource values.
- [func CFURLCreateBookmarkDataFromFile(CFAllocator!, CFURL!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Unmanaged<CFData>!](cfurlcreatebookmarkdatafromfile(_:_:_:).md)
  Initializes and returns bookmark data derived from a file pointed to by a specified URL.
- [func CFURLWriteBookmarkDataToFile(CFData!, CFURL!, CFURLBookmarkFileCreationOptions, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](cfurlwritebookmarkdatatofile(_:_:_:_:).md)
  Creates an alias file on disk at a specified location with specified bookmark data.
- [func CFURLStartAccessingSecurityScopedResource(CFURL!) -> Bool](cfurlstartaccessingsecurityscopedresource(_:).md)
  In an app that has adopted App Sandbox, makes the resource pointed to by a security-scoped URL available to the app.
- [func CFURLStopAccessingSecurityScopedResource(CFURL!)](cfurlstopaccessingsecurityscopedresource(_:).md)
  In an app that adopts App Sandbox, revokes access to the resource pointed to by a security-scoped URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfurlcreatebookmarkdatafromaliasrecord(_:_:))*