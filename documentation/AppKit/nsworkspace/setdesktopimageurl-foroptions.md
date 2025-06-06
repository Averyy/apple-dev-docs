# setDesktopImageURL(_:for:options:)

**Framework**: Appkit  
**Kind**: method

Sets the desktop image for the given screen to the image at the specified URL.

**Availability**:
- macOS 10.6+

## Declaration

```swift
func setDesktopImageURL(_ url: URL, for screen: NSScreen, options: [NSWorkspace.DesktopImageOptionKey : Any] = [:]) throws
```

#### Discussion

Instead of presenting a user interface for picking the options, choose appropriate defaults and allow the user to adjust them in the System Preference Pane.

You must call this method from your app’s main thread.

> **Note**:  In Swift, this method returns `Void` and is marked with the `throws` keyword to indicate that it throws an error in cases of failure. You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [`Error Handling`](https://developer.apple.comhttps://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [`The Swift Programming Language`](https://developer.apple.comhttps://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## Parameters

- `url`: A file URL to the image. The URL must not be  .
- `screen`: The screen on which to set the desktop image.
- `options`: The options dictionary may contain any of the keys in  , which control how the image is scaled on the screen.

## See Also

- [func desktopImageURL(for: NSScreen) -> URL?](nsworkspace/desktopimageurl(for:).md)
  Returns the URL for the desktop image for the given screen.
- [func desktopImageOptions(for: NSScreen) -> [NSWorkspace.DesktopImageOptionKey : Any]?](nsworkspace/desktopimageoptions(for:).md)
  Returns the desktop image options for the given screen.
- [NSWorkspace.DesktopImageOptionKey](nsworkspace/desktopimageoptionkey.md)
  Keys that indicate how to display a new desktop image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsworkspace/setdesktopimageurl(_:for:options:))*