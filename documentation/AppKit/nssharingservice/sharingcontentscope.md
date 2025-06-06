# NSSharingService.SharingContentScope

**Framework**: AppKit  
**Kind**: enum

The sharing scope constants specify the nature of the things you are sharing.

**Availability**:
- macOS 10.8+

## Declaration

```swift
enum SharingContentScope
```

## Topics

### Constants
- [NSSharingService.SharingContentScope.item](nssharingservice/sharingcontentscope/item.md)
  Used when sharing a clearly identified item, for example, a file represented by its icon.
- [NSSharingService.SharingContentScope.partial](nssharingservice/sharingcontentscope/partial.md)
  Used when sharing a portion of a more global content, for example, part of a webpage.
- [NSSharingService.SharingContentScope.full](nssharingservice/sharingcontentscope/full.md)
  Used when sharing the whole content of the current document, for example, the URL of the webpage.
### Initializers
- [init?(rawValue: Int)](nssharingservice/sharingcontentscope/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [func sharingService(NSSharingService, sourceFrameOnScreenForShareItem: Any) -> NSRect](nssharingservicedelegate/sharingservice(_:sourceframeonscreenforshareitem:).md)
  Invoked when the sharing service is performed and the sharing window is displayed, to present a transition between the original items and the sharing window.
- [func sharingService(NSSharingService, transitionImageForShareItem: Any, contentRect: UnsafeMutablePointer<NSRect>) -> NSImage?](nssharingservicedelegate/sharingservice(_:transitionimageforshareitem:contentrect:).md)
  Invoked to allow returning a custom transition image when sharing an item.
- [func sharingService(NSSharingService, sourceWindowForShareItems: [Any], sharingContentScope: UnsafeMutablePointer<NSSharingService.SharingContentScope>) -> NSWindow?](nssharingservicedelegate/sharingservice(_:sourcewindowforshareitems:sharingcontentscope:).md)
  Returns the window that contained the share items.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssharingservice/sharingcontentscope)*