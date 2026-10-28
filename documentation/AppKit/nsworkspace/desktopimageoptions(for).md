# desktopImageOptions(for:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns the desktop image options for the given screen.

**Availability**:
- macOS 10.6+

## Declaration

```swift
func desktopImageOptions(for screen: NSScreen) -> [NSWorkspace.DesktopImageOptionKey : Any]?
```

```objc
- (NSDictionary<NSString *,id> *) desktopImageOptionsForScreen:(NSScreen *) screen;
```

## Return Value

A dictionary containing the keys found in [`NSWorkspace.DesktopImageOptionKey`](./desktopimageoptionkey.md).

## Discussion

You must call this method from your app’s main thread.

## Parameters

- `screen`: The screen for which to get the desktop image options.

## See Also

### Managing the Desktop Image
- [func desktopImageURL(for: NSScreen) -> URL?](./desktopimageurl%28for%29.md)
  Returns the URL for the desktop image for the given screen.
- [func setDesktopImageURL(URL, for: NSScreen, options: [NSWorkspace.DesktopImageOptionKey : Any]) throws](./setdesktopimageurl%28_,for,options%29.md)
  Sets the desktop image for the given screen to the image at the specified URL.
- [NSWorkspace.DesktopImageOptionKey](./desktopimageoptionkey.md)
  Keys that indicate how to display a new desktop image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsworkspace/desktopimageoptions(for:))*