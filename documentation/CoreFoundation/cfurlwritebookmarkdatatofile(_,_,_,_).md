# CFURLWriteBookmarkDataToFile(_:_:_:_:)

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Creates an alias file on disk at a specified location with specified bookmark data.

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
func CFURLWriteBookmarkDataToFile(_ bookmarkRef: CFData!, _ fileURL: CFURL!, _ options: CFURLBookmarkFileCreationOptions, _ errorRef: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool
```

```c
extern Boolean CFURLWriteBookmarkDataToFile(CFDataRef bookmarkRef, CFURLRef fileURL, CFURLBookmarkFileCreationOptions options, CFErrorRef*errorRef);
```

## Return Value

`true` if the alias file is successfully created; otherwise, `false`.

## Parameters

- `bookmarkRef`: The bookmark data containing information for the alias file.
- `fileURL`: The desired location of the alias file.
- `options`: Options taken into account when creating the alias file.
- `errorRef`: The error that occurred in the case that the alias file cannot be created.

## See Also

### Working with Bookmark Data
- [func CFURLCreateBookmarkData(CFAllocator!, CFURL!, CFURLBookmarkCreationOptions, CFArray!, CFURL!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Unmanaged<CFData>!](./cfurlcreatebookmarkdata%28_,_,_,_,_,_%29.md)
  Returns bookmark data for a URL, created with specified options and resource values.
- [func CFURLCreateBookmarkDataFromAliasRecord(CFAllocator!, CFData!) -> Unmanaged<CFData>!](./cfurlcreatebookmarkdatafromaliasrecord%28_,_%29.md)
  Initializes and returns bookmark data derived from an alias record.
- [func CFURLCreateBookmarkDataFromFile(CFAllocator!, CFURL!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Unmanaged<CFData>!](./cfurlcreatebookmarkdatafromfile%28_,_,_%29.md)
  Initializes and returns bookmark data derived from a file pointed to by a specified URL.
- [func CFURLStartAccessingSecurityScopedResource(CFURL!) -> Bool](./cfurlstartaccessingsecurityscopedresource%28_%29.md)
  In an app that has adopted App Sandbox, makes the resource pointed to by a security-scoped URL available to the app.
- [func CFURLStopAccessingSecurityScopedResource(CFURL!)](./cfurlstopaccessingsecurityscopedresource%28_%29.md)
  In an app that adopts App Sandbox, revokes access to the resource pointed to by a security-scoped URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfurlwritebookmarkdatatofile(_:_:_:_:))*