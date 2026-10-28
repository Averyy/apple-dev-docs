# sharingService(_:sourceWindowForShareItems:sharingContentScope:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns the window that contained the share items.

**Availability**:
- macOS 10.8+

## Declaration

```swift
@MainActor
optional func sharingService(_ sharingService: NSSharingService, sourceWindowForShareItems items: [Any], sharingContentScope: UnsafeMutablePointer<NSSharingService.SharingContentScope>) -> NSWindow?
```

```objc
- (NSWindow *) sharingService:(NSSharingService *) sharingService sourceWindowForShareItems:(NSArray *) items sharingContentScope:(NSSharingContentScope *) sharingContentScope;
```

## Return Value

The window of the shared items.

## Discussion

The following is an example implementation of this method. It changes the item scope, and returns the window the source image view is contained within.

```objc
- (NSWindow *)sharingService:(NSSharingService *)sharingService
              sourceWindowForShareItems:(NSArray *)items
              sharingContentScope:(NSSharingContentScope *)sharingContentScope
{
    *sharingContentScope = NSSharingContentScopeItem;
    return [_imageView window];
}
```

## Parameters

- `sharingService`: The sharing service.
- `items`: The items being shared.
- `sharingContentScope`: The sharing content scope. The sharing scope can be modified from the default value of [`NSSharingService.SharingContentScope.item`](../nssharingservice/sharingcontentscope/item.md) by setting a different value in the out parameter `sharingContentScope`. See [`NSSharingService.SharingContentScope`](../nssharingservice/sharingcontentscope.md) for supported values.

## See Also

### Customizing Transition Animation
- [func sharingService(NSSharingService, sourceFrameOnScreenForShareItem: Any) -> NSRect](./sharingservice%28_,sourceframeonscreenforshareitem%29.md)
  Invoked when the sharing service is performed and the sharing window is displayed, to present a transition between the original items and the sharing window.
- [func sharingService(NSSharingService, transitionImageForShareItem: Any, contentRect: UnsafeMutablePointer<NSRect>) -> NSImage?](./sharingservice%28_,transitionimageforshareitem,contentrect%29.md)
  Invoked to allow returning a custom transition image when sharing an item.
- [NSSharingService.SharingContentScope](../nssharingservice/sharingcontentscope.md)
  The sharing scope constants specify the nature of the things you are sharing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssharingservicedelegate/sharingservice(_:sourcewindowforshareitems:sharingcontentscope:))*