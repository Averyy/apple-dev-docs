# CancelPreviewGeneration

**Framework**: Quick Look  
**Kind**: property  
**Role**: Instance Property

**Availability**:
- macOS 10.5+

## Declaration

```swift
var CancelPreviewGeneration: ((UnsafeMutableRawPointer?, QLPreviewRequest?) -> Void)!
```

```c
void (*)(void *, struct __QLPreviewRequest *) CancelPreviewGeneration;
```

## See Also

### Creating a Quick Look Plug-In
- [init()](./init%28%29.md)
  Creates the interface structure that the platform uses to interface with a Quick Look plug-in.
- [var QueryInterface: ((UnsafeMutableRawPointer?, REFIID, UnsafeMutablePointer<LPVOID?>?) -> HRESULT)!](./queryinterface.md)
- [var AddRef: ((UnsafeMutableRawPointer?) -> ULONG)!](./addref.md)
- [var Release: ((UnsafeMutableRawPointer?) -> ULONG)!](./release.md)
- [var GenerateThumbnailForURL: ((UnsafeMutableRawPointer?, QLThumbnailRequest?, CFURL?, CFString?, CFDictionary?, CGSize) -> OSStatus)!](./generatethumbnailforurl.md)
- [var CancelThumbnailGeneration: ((UnsafeMutableRawPointer?, QLThumbnailRequest?) -> Void)!](./cancelthumbnailgeneration.md)
- [var GeneratePreviewForURL: ((UnsafeMutableRawPointer?, QLPreviewRequest?, CFURL?, CFString?, CFDictionary?) -> OSStatus)!](./generatepreviewforurl.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicklook/qlgeneratorinterfacestruct/cancelpreviewgeneration)*