# desktopImageURL(for:)

**Framework**: AppKit  
**Kind**: method

Returns the URL for the desktop image for the given screen.

**Availability**:
- macOS 10.6+

## Declaration

```swift
func desktopImageURL(for screen: NSScreen) -> URL?
```

#### Return Value

The desktop image.

#### Discussion

You must call this method from your app’s main thread.

## Parameters

- `screen`: The screen for which to get the desktop image.

## See Also

- [func setDesktopImageURL(URL, for: NSScreen, options: [NSWorkspace.DesktopImageOptionKey : Any]) throws](nsworkspace/setdesktopimageurl(_:for:options:).md)
  Sets the desktop image for the given screen to the image at the specified URL.
- [func desktopImageOptions(for: NSScreen) -> [NSWorkspace.DesktopImageOptionKey : Any]?](nsworkspace/desktopimageoptions(for:).md)
  Returns the desktop image options for the given screen.
- [NSWorkspace.DesktopImageOptionKey](nsworkspace/desktopimageoptionkey.md)
  Keys that indicate how to display a new desktop image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsworkspace/desktopimageurl(for:))*