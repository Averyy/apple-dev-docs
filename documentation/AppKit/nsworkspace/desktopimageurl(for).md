# desktopImageURL(for:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns the URL for the desktop image for the given screen.

**Availability**:
- macOS 10.6+

## Declaration

```swift
func desktopImageURL(for screen: NSScreen) -> URL?
```

```objc
- (NSURL *) desktopImageURLForScreen:(NSScreen *) screen;
```

#### Return Value

The desktop image.

#### Discussion

You must call this method from your app’s main thread.

## Parameters

- `screen`: The screen for which to get the desktop image.

## See Also

### Managing the Desktop Image
- [func setDesktopImageURL(URL, for: NSScreen, options: [NSWorkspace.DesktopImageOptionKey : Any]) throws](./setdesktopimageurl%28_,for,options%29.md)
  Sets the desktop image for the given screen to the image at the specified URL.
- [func desktopImageOptions(for: NSScreen) -> [NSWorkspace.DesktopImageOptionKey : Any]?](./desktopimageoptions%28for%29.md)
  Returns the desktop image options for the given screen.
- [NSWorkspace.DesktopImageOptionKey](./desktopimageoptionkey.md)
  Keys that indicate how to display a new desktop image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsworkspace/desktopimageurl(for:))*