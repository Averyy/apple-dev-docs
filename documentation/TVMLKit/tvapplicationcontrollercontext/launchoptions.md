# launchOptions

**Framework**: TVMLKit  
**Kind**: property  
**Role**: Instance Property

Data passed to the JavaScript launch callback method.

**Availability**:
- tvOS 9.0+ - Deprecated in 18.0

> **Deprecated**: Please use SwiftUI or UIKit

## Declaration

```swift
var launchOptions: [String : Any] { get set }
```

```objc
@property (nonatomic, copy) NSDictionary<NSString *,id> * launchOptions;
```

#### Discussion

The system will pass this data to the JavaScript [`onLaunch`](../../tvmljs/app/api-1627407-onlaunch.md) method. The values contained in this property must be serializable. You must include [`url`](../../UIKit/uiapplication/launchoptionskey/url.md) and [`sourceApplication`](../../UIKit/uiapplication/launchoptionskey/sourceapplication.md) in the launch options if the JavaScript implements the [`openURL(_:)`](../../UIKit/uiapplication/openurl%28_%29.md) method.

## See Also

### Providing Launch Information
- [var javaScriptApplicationURL: URL](./javascriptapplicationurl.md)
  URL pointing to the controlling JavaScript file for the application.
- [var storageIdentifier: String?](./storageidentifier.md)
  Optional identifier for a local storage file.
- [var supportsPictureInPicturePlayback: Bool](./supportspictureinpictureplayback.md)
  A Boolean value that indicates whether your app can display content in a picture-in-picture format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvmlkit/tvapplicationcontrollercontext/launchoptions)*