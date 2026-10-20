# supportsPictureInPicturePlayback

**Framework**: TVMLKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether your app can display content in a picture-in-picture format.

**Availability**:
- tvOS 9.0+ - Deprecated in 18.0

> **Deprecated**: Please use SwiftUI or UIKit

## Declaration

```swift
var supportsPictureInPicturePlayback: Bool { get set }
```

```objc
@property (nonatomic, readwrite) BOOL supportsPictureInPicturePlayback;
```

#### Discussion

When this property is set to [`true`](../../Swift/true.md), the system allows the user to continue watching your app’s video content while using other apps. If you customize playback with [`AVPlayerViewController`](../../AVKit/avplayerviewcontroller.md), set the controller’s [`delegate`](../../AVKit/avplayerviewcontroller/delegate.md) property to an object that implements the [`AVPlayerViewControllerDelegate`](../../AVKit/avplayerviewcontrollerdelegate.md) protocol and the system will notify that object about picture-in-picture playback events.

The default value is [`true`](../../Swift/true.md).

## See Also

### Providing Launch Information
- [var javaScriptApplicationURL: URL](./javascriptapplicationurl.md)
  URL pointing to the controlling JavaScript file for the application.
- [var launchOptions: [String : Any]](./launchoptions.md)
  Data passed to the JavaScript launch callback method.
- [var storageIdentifier: String?](./storageidentifier.md)
  Optional identifier for a local storage file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvmlkit/tvapplicationcontrollercontext/supportspictureinpictureplayback)*