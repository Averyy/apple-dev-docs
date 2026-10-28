# miniwindowTitle

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The title displayed in the window’s minimized window.

**Availability**:
- macOS

## Declaration

```swift
var miniwindowTitle: String! { get set }
```

```objc
@property (copy, null_resettable) NSString * miniwindowTitle;
```

## Discussion

A minimized window’s title usually reflects that of its full-size counterpart, abbreviated to fit if necessary. Although this property allows you to set the minimized window’s title explicitly, changing the full-size `NSWindow` object’s title (through [`title`](./title.md) or [`setTitleWithRepresentedFilename(_:)`](./settitlewithrepresentedfilename%28_%29.md)) automatically changes the minimized window’s title as well.

## See Also

### Minimizing Windows
- [var isMiniaturized: Bool](./isminiaturized.md)
  A Boolean value that indicates whether the window is minimized.
- [func performMiniaturize(Any?)](./performminiaturize%28_%29.md)
  Simulates the user clicking the minimize button by momentarily highlighting the button, then minimizing the window.
- [func miniaturize(Any?)](./miniaturize%28_%29.md)
  Removes the window from the screen list and displays the minimized window in the Dock.
- [func deminiaturize(Any?)](./deminiaturize%28_%29.md)
  De-minimizes the window.
- [var miniwindowImage: NSImage?](./miniwindowimage.md)
  The custom miniaturized window image of the window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/miniwindowtitle)*