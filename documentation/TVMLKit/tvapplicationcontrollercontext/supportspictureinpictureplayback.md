# supportsPictureInPicturePlayback

**Framework**: TVMLKit  
**Kind**: property

A Boolean value that indicates whether your app can display content in a picture-in-picture format.

**Availability**:
- tvOS 9.0+

## Declaration

```swift
var supportsPictureInPicturePlayback: Bool { get set }
```

#### Discussion

When this property is set to [`true`](https://developer.apple.com/documentation/swift/true), the system allows the user to continue watching your app’s video content while using other apps. If you customize playback with [`AVPlayerViewController`](https://developer.apple.com/documentation/AVKit/AVPlayerViewController), set the controller’s [`delegate`](https://developer.apple.com/documentation/AVKit/AVPlayerViewController/delegate) property to an object that implements the [`AVPlayerViewControllerDelegate`](https://developer.apple.com/documentation/AVKit/AVPlayerViewControllerDelegate) protocol and the system will notify that object about picture-in-picture playback events.

The default value is [`true`](https://developer.apple.com/documentation/swift/true).

## See Also

- [var javaScriptApplicationURL: URL](tvapplicationcontrollercontext/javascriptapplicationurl.md)
  URL pointing to the controlling JavaScript file for the application.
- [var launchOptions: [String : Any]](tvapplicationcontrollercontext/launchoptions.md)
  Data passed to the JavaScript launch callback method.
- [var storageIdentifier: String?](tvapplicationcontrollercontext/storageidentifier.md)
  Optional identifier for a local storage file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvmlkit/tvapplicationcontrollercontext/supportspictureinpictureplayback)*