# init()

**Framework**: Quick Look  
**Kind**: init  
**Role**: Initializer

Creates the interface structure that the platform uses to interface with a Quick Look plug-in.

**Availability**:
- macOS 10.5+

## Declaration

```swift
init()
```

## See Also

### Creating a Quick Look Plug-In
- [var QueryInterface: ((UnsafeMutableRawPointer?, REFIID, UnsafeMutablePointer<LPVOID?>?) -> HRESULT)!](./queryinterface.md)
- [var AddRef: ((UnsafeMutableRawPointer?) -> ULONG)!](./addref.md)
- [var Release: ((UnsafeMutableRawPointer?) -> ULONG)!](./release.md)
- [var GenerateThumbnailForURL: ((UnsafeMutableRawPointer?, QLThumbnailRequest?, CFURL?, CFString?, CFDictionary?, CGSize) -> OSStatus)!](./generatethumbnailforurl.md)
- [var CancelThumbnailGeneration: ((UnsafeMutableRawPointer?, QLThumbnailRequest?) -> Void)!](./cancelthumbnailgeneration.md)
- [var GeneratePreviewForURL: ((UnsafeMutableRawPointer?, QLPreviewRequest?, CFURL?, CFString?, CFDictionary?) -> OSStatus)!](./generatepreviewforurl.md)
- [var CancelPreviewGeneration: ((UnsafeMutableRawPointer?, QLPreviewRequest?) -> Void)!](./cancelpreviewgeneration.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicklook/qlgeneratorinterfacestruct/init())*