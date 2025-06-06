# sharingService(_:transitionImageForShareItem:contentRect:)

**Framework**: AppKit  
**Kind**: method

Invoked to allow returning a custom transition image when sharing an item.

**Availability**:
- macOS 10.8+

## Declaration

```swift
@MainActor
optional func sharingService(_ sharingService: NSSharingService, transitionImageForShareItem item: Any, contentRect: UnsafeMutablePointer<NSRect>) -> NSImage?
```

#### Return Value

The image to display for the sharing transition. Its size should exactly match that of the original image.

#### Discussion

A sample implementation of this method:

```objc
- (NSImage *)sharingService:(NSSharingService *)sharingService
             transitionImageForShareItem:(id <NSPasteboardWriting>)item
             contentRect:(NSRect *)contentRect
{
    if ([item isKindOfClass:[NSImage class]]) {
        return [_imageView image];
    }
}
```

## Parameters

- `sharingService`: The sharing service.
- `item`: The shared item.
- `contentRect`: The content rectangle is the frame of the actual content inside the transition image, excluding all decorations. For example, if the transition image is a QuickLook thumbnail, the value would be  .

## See Also

- [func sharingService(NSSharingService, sourceFrameOnScreenForShareItem: Any) -> NSRect](nssharingservicedelegate/sharingservice(_:sourceframeonscreenforshareitem:).md)
  Invoked when the sharing service is performed and the sharing window is displayed, to present a transition between the original items and the sharing window.
- [func sharingService(NSSharingService, sourceWindowForShareItems: [Any], sharingContentScope: UnsafeMutablePointer<NSSharingService.SharingContentScope>) -> NSWindow?](nssharingservicedelegate/sharingservice(_:sourcewindowforshareitems:sharingcontentscope:).md)
  Returns the window that contained the share items.
- [NSSharingService.SharingContentScope](nssharingservice/sharingcontentscope.md)
  The sharing scope constants specify the nature of the things you are sharing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssharingservicedelegate/sharingservice(_:transitionimageforshareitem:contentrect:))*