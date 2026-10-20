# miniwindowImage

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The custom miniaturized window image of the window.

**Availability**:
- macOS

## Declaration

```swift
var miniwindowImage: NSImage? { get set }
```

```objc
@property (strong, nullable) NSImage * miniwindowImage;
```

#### Discussion

The miniaturized window image is the image displayed in the Dock when the window is minimized. If you did not assign a custom image to the window, the value of this property is `nil`.

When the user minimizes the window, the Dock displays [`miniwindowImage`](./miniwindowimage.md) in the corresponding Dock tile, scaling it as needed to fit in the tile. If you do not specify a custom image using this property, the Dock creates one for you automatically.

You can also set this property as needed to change the minimized window image. Typically, you would specify a custom image immediately prior to a window being minimized—when the system posts [`willMiniaturizeNotification`](./willminiaturizenotification.md). You can set this property while the window is minimized to update the current image in the Dock. However, you should not use this property to create complex animations in the Dock.

Support for custom images is disabled by default. To enable support, set the `AppleDockIconEnabled` key to [`true`](../../Swift/true.md) when first registering your application’s user defaults. You must set this key prior to calling the `init` method of [`NSApplication`](../nsapplication.md), which reads the current value of the key.

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
- [var miniwindowTitle: String!](./miniwindowtitle.md)
  The title displayed in the window’s minimized window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/miniwindowimage)*