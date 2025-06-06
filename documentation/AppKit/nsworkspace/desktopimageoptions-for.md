# desktopImageOptions(for:)

**Framework**: AppKit  
**Kind**: method

Returns the desktop image options for the given screen.

**Availability**:
- macOS 10.6+

## Declaration

```swift
func desktopImageOptions(for screen: NSScreen) -> [NSWorkspace.DesktopImageOptionKey : Any]?
```

#### Return Value

A dictionary containing the keys found in [`NSWorkspace.DesktopImageOptionKey`](nsworkspace/desktopimageoptionkey.md).

#### Discussion

You must call this method from your app’s main thread.

## Parameters

- `screen`: The screen for which to get the desktop image options.

## See Also

- [func desktopImageURL(for: NSScreen) -> URL?](nsworkspace/desktopimageurl(for:).md)
  Returns the URL for the desktop image for the given screen.
- [func setDesktopImageURL(URL, for: NSScreen, options: [NSWorkspace.DesktopImageOptionKey : Any]) throws](nsworkspace/setdesktopimageurl(_:for:options:).md)
  Sets the desktop image for the given screen to the image at the specified URL.
- [NSWorkspace.DesktopImageOptionKey](nsworkspace/desktopimageoptionkey.md)
  Keys that indicate how to display a new desktop image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsworkspace/desktopimageoptions(for:))*