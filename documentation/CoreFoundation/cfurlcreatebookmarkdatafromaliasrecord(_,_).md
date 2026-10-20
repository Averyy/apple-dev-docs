# CFURLCreateBookmarkDataFromAliasRecord(_:_:)

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Initializes and returns bookmark data derived from an alias record.

**Availability**:
- macOS 10.6+ - Deprecated in 11.0

> **Deprecated**: The Carbon Alias Manager is deprecated. This function should only be used to convert Carbon AliasRecords to bookmark data.

## Declaration

```swift
func CFURLCreateBookmarkDataFromAliasRecord(_ allocatorRef: CFAllocator!, _ aliasRecordDataRef: CFData!) -> Unmanaged<CFData>!
```

```c
extern CFDataRefCFURLCreateBookmarkDataFromAliasRecord(CFAllocatorRef allocatorRef, CFDataRef aliasRecordDataRef);
```

#### Return Value

The bookmark data for the alias record.

## Parameters

- `allocatorRef`: The allocator to use to allocate memory for the new `CFURL` object. Pass `NULL` or [`kCFAllocatorDefault`](./kcfallocatordefault.md) to use the current default allocator.
- `aliasRecordDataRef`: The alias record.

## See Also

### Working with Bookmark Data
- [func CFURLCreateBookmarkData(CFAllocator!, CFURL!, CFURLBookmarkCreationOptions, CFArray!, CFURL!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Unmanaged<CFData>!](./cfurlcreatebookmarkdata%28_,_,_,_,_,_%29.md)
  Returns bookmark data for a URL, created with specified options and resource values.
- [func CFURLCreateBookmarkDataFromFile(CFAllocator!, CFURL!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Unmanaged<CFData>!](./cfurlcreatebookmarkdatafromfile%28_,_,_%29.md)
  Initializes and returns bookmark data derived from a file pointed to by a specified URL.
- [func CFURLWriteBookmarkDataToFile(CFData!, CFURL!, CFURLBookmarkFileCreationOptions, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](./cfurlwritebookmarkdatatofile%28_,_,_,_%29.md)
  Creates an alias file on disk at a specified location with specified bookmark data.
- [func CFURLStartAccessingSecurityScopedResource(CFURL!) -> Bool](./cfurlstartaccessingsecurityscopedresource%28_%29.md)
  In an app that has adopted App Sandbox, makes the resource pointed to by a security-scoped URL available to the app.
- [func CFURLStopAccessingSecurityScopedResource(CFURL!)](./cfurlstopaccessingsecurityscopedresource%28_%29.md)
  In an app that adopts App Sandbox, revokes access to the resource pointed to by a security-scoped URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfurlcreatebookmarkdatafromaliasrecord(_:_:))*