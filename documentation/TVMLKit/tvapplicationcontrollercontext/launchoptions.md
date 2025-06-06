# launchOptions

**Framework**: TVMLKit  
**Kind**: property

Data passed to the JavaScript launch callback method.

**Availability**:
- tvOS 9.0+

## Declaration

```swift
var launchOptions: [String : Any] { get set }
```

#### Discussion

The system will pass this data to the JavaScript [`onLaunch`](https://developer.apple.com/documentation/tvmljs/app/1627407-onlaunch) method. The values contained in this property must be serializable. You must include [`url`](https://developer.apple.com/documentation/UIKit/UIApplication/LaunchOptionsKey/url) and [`sourceApplication`](https://developer.apple.com/documentation/UIKit/UIApplication/LaunchOptionsKey/sourceApplication) in the launch options if the JavaScript implements the [`openURL(_:)`](https://developer.apple.com/documentation/UIKit/UIApplication/openURL(_:)) method.

## See Also

- [var javaScriptApplicationURL: URL](tvapplicationcontrollercontext/javascriptapplicationurl.md)
  URL pointing to the controlling JavaScript file for the application.
- [var storageIdentifier: String?](tvapplicationcontrollercontext/storageidentifier.md)
  Optional identifier for a local storage file.
- [var supportsPictureInPicturePlayback: Bool](tvapplicationcontrollercontext/supportspictureinpictureplayback.md)
  A Boolean value that indicates whether your app can display content in a picture-in-picture format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvmlkit/tvapplicationcontrollercontext/launchoptions)*