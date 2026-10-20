# NSSharingService.SharingContentScope

**Framework**: AppKit  
**Kind**: enum  
**Role**: Enumeration

The sharing scope constants specify the nature of the things you are sharing.

**Availability**:
- macOS 10.8+

## Declaration

```swift
enum SharingContentScope
```

```c
enum NSSharingContentScope : NSInteger;
```

## Topics

### Constants
- [NSSharingService.SharingContentScope.item](./sharingcontentscope/item.md)
  Used when sharing a clearly identified item, for example, a file represented by its icon.
- [NSSharingService.SharingContentScope.partial](./sharingcontentscope/partial.md)
  Used when sharing a portion of a more global content, for example, part of a webpage.
- [NSSharingService.SharingContentScope.full](./sharingcontentscope/full.md)
  Used when sharing the whole content of the current document, for example, the URL of the webpage.
### Initializers
- [init?(rawValue: Int)](./sharingcontentscope/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Customizing Transition Animation
- [func sharingService(NSSharingService, sourceFrameOnScreenForShareItem: Any) -> NSRect](../nssharingservicedelegate/sharingservice%28_,sourceframeonscreenforshareitem%29.md)
  Invoked when the sharing service is performed and the sharing window is displayed, to present a transition between the original items and the sharing window.
- [func sharingService(NSSharingService, transitionImageForShareItem: Any, contentRect: UnsafeMutablePointer<NSRect>) -> NSImage?](../nssharingservicedelegate/sharingservice%28_,transitionimageforshareitem,contentrect%29.md)
  Invoked to allow returning a custom transition image when sharing an item.
- [func sharingService(NSSharingService, sourceWindowForShareItems: [Any], sharingContentScope: UnsafeMutablePointer<NSSharingService.SharingContentScope>) -> NSWindow?](../nssharingservicedelegate/sharingservice%28_,sourcewindowforshareitems,sharingcontentscope%29.md)
  Returns the window that contained the share items.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssharingservice/sharingcontentscope)*