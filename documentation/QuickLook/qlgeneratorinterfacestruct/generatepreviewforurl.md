# GeneratePreviewForURL

**Framework**: Quick Look  
**Kind**: property

**Availability**:
- macOS 10.5+

## Declaration

```swift
var GeneratePreviewForURL: ((UnsafeMutableRawPointer?, QLPreviewRequest?, CFURL?, CFString?, CFDictionary?) -> OSStatus)!
```

## See Also

- [init()](qlgeneratorinterfacestruct/init.md)
  Creates the interface structure that the platform uses to interface with a Quick Look plug-in.
- [var QueryInterface: ((UnsafeMutableRawPointer?, REFIID, UnsafeMutablePointer<LPVOID?>?) -> HRESULT)!](qlgeneratorinterfacestruct/queryinterface.md)
- [var AddRef: ((UnsafeMutableRawPointer?) -> ULONG)!](qlgeneratorinterfacestruct/addref.md)
- [var Release: ((UnsafeMutableRawPointer?) -> ULONG)!](qlgeneratorinterfacestruct/release.md)
- [var GenerateThumbnailForURL: ((UnsafeMutableRawPointer?, QLThumbnailRequest?, CFURL?, CFString?, CFDictionary?, CGSize) -> OSStatus)!](qlgeneratorinterfacestruct/generatethumbnailforurl.md)
- [var CancelThumbnailGeneration: ((UnsafeMutableRawPointer?, QLThumbnailRequest?) -> Void)!](qlgeneratorinterfacestruct/cancelthumbnailgeneration.md)
- [var CancelPreviewGeneration: ((UnsafeMutableRawPointer?, QLPreviewRequest?) -> Void)!](qlgeneratorinterfacestruct/cancelpreviewgeneration.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicklook/qlgeneratorinterfacestruct/generatepreviewforurl)*