# UIRequiresFullScreen

**Framework**: Bundle Resources  
**Kind**: typealias

A Boolean value that indicates whether the system puts an iPad app into a compatibility mode that opts the app out of multitasking and dynamic resizing.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+

#### Discussion

iPad multitasking lets multiple apps appear on screen at the same time. Dragging the resize controls causes the system to change the size of each app’s window. Each app must then adjust its content to fit the newly available space.

`UIRequiresFullScreen` allows apps to opt out of this multitasking and dynamic resizing in iOS 9 and later. You include this key in your app’s information property list and set the value to [`true`](https://developer.apple.com/documentation/Swift/true) to request the system to place your app in a compatibility mode that opts out of iPad multitasking and dynamic resizing. In this compatibility mode, the following occurs:

- In iPadOS 26 and later on an iPad that supports the Windowed Apps multitasking mode, or in iPadOS 16 or later on an iPad that supports Stage Manager, the system: - Maintains a consistent scene size for your app, but doesn’t present your app’s scene full screen
- Allows your app’s scene to be on screen with other apps’ scenes
- Scales your app’s presentation when the user resizes it, rather than changing the size of your app’s scene
- Consults the supported interface orientations of your app and adjusts the interface orientation of your scene accordingly, but doesn’t visually rotate your scene
- In iPadOS 18 and earlier on an iPad with Split View & Slide Over multitasking enabled, the system: - Presents your app’s scene full screen
- Prevents your app’s scene from sharing the screen with other app’s scenes in Split View
- Prevents your app’s scene from being resized by the user
- Consults the supported interface orientations of your app, adjusts the interface orientation of your scene accordingly, and visually rotates your scene

In iPadOS 26 and later, support multitasking and dynamic resizing to make your iPad app flexible. For more information, see [`Make your UIKit app more flexible`](https://developer.apple.comhttps://developer.apple.com/videos/play/wwdc2025/282).

For more information about expressing preferred sizing limits for your scene, see [`UISceneSizeRestrictions`](https://developer.apple.com/documentation/UIKit/UISceneSizeRestrictions). For more information about locking your scene to your preferred interface orientation and preventing rotation, see [`prefersInterfaceOrientationLocked`](https://developer.apple.com/documentation/UIKit/UIViewController/prefersInterfaceOrientationLocked).

## See Also

- [Multitasking on iPad, Mac, and Apple Vision Pro](../UIKit/multitasking-on-ipad-mac-and-apple-vision-pro.md)
  Implement multitasking APIs to seamlessly integrate your app with iPadOS, macOS, and visionOS.
- [Presenting content on a connected display](../UIKit/presenting-content-on-a-connected-display.md)
  Fill connected displays with additional content from your app.
- [UILaunchImages](information-property-list/uilaunchimages.md)
  A dictionary containing information about launch images.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list/uirequiresfullscreen)*