# NSWindow.SharingType.none

**Framework**: AppKit  
**Kind**: case

A legacy constant that macOS no longer uses.

**Availability**:
- macOS 10.5+

## Declaration

```swift
case none
```

#### Discussion

`NSWindowSharingNone` can cause content to not be available in certain sharing situations. Don’t use this value to hide or omit content from being captured. Instead, use FairPlay Streaming (FPS). For more information, read [`FairPlay Streaming`](https://developer.apple.comhttps://developer.apple.com/streaming/fps/).

## See Also

- [NSWindow.SharingType.readOnly](nswindow/sharingtype-swift.enum/readonly.md)
- [static let readWrite: NSWindow.SharingType](nswindow/sharingtype-swift.enum/readwrite.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/sharingtype-swift.enum/none)*