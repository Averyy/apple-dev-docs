# sharingService(_:sourceFrameOnScreenForShareItem:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Invoked when the sharing service is performed and the sharing window is displayed, to present a transition between the original items and the sharing window.

**Availability**:
- macOS 10.8+

## Declaration

```swift
@MainActor
optional func sharingService(_ sharingService: NSSharingService, sourceFrameOnScreenForShareItem item: Any) -> NSRect
```

```objc
- (NSRect) sharingService:(NSSharingService *) sharingService sourceFrameOnScreenForShareItem:(id) item;
```

## Return Value

The rectangle, in screen coordinates, to display the transition.

## Discussion

The following is an example implementation of this method:

```objc
- (NSRect)sharingService:(NSSharingService *)sharingService sourceFrameOnScreenForShareItem:(id <NSPasteboardWriting>)item
{
    if ([item isKindOfClass:[NSImage class]]) {
        NSImage * image = [_imageView image];
        NSRect frame = [_imageView bounds];
        frame = [_imageView convertRect:frame toView:nil];
        frame.origin = [[_imageView window] convertBaseToScreen:frame.origin];
        return frame;
    }
    return NSZeroRect;
}
```

## Parameters

- `sharingService`: The sharing service.
- `item`: The item being shared.

## See Also

### Customizing Transition Animation
- [func sharingService(NSSharingService, transitionImageForShareItem: Any, contentRect: UnsafeMutablePointer<NSRect>) -> NSImage?](./sharingservice%28_,transitionimageforshareitem,contentrect%29.md)
  Invoked to allow returning a custom transition image when sharing an item.
- [func sharingService(NSSharingService, sourceWindowForShareItems: [Any], sharingContentScope: UnsafeMutablePointer<NSSharingService.SharingContentScope>) -> NSWindow?](./sharingservice%28_,sourcewindowforshareitems,sharingcontentscope%29.md)
  Returns the window that contained the share items.
- [NSSharingService.SharingContentScope](../nssharingservice/sharingcontentscope.md)
  The sharing scope constants specify the nature of the things you are sharing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssharingservicedelegate/sharingservice(_:sourceframeonscreenforshareitem:))*