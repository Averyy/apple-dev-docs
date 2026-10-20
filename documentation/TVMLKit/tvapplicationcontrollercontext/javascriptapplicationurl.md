# javaScriptApplicationURL

**Framework**: TVMLKit  
**Kind**: property  
**Role**: Instance Property

URL pointing to the controlling JavaScript file for the application.

**Availability**:
- tvOS 9.0+ - Deprecated in 18.0

> **Deprecated**: Please use SwiftUI or UIKit

## Declaration

```swift
var javaScriptApplicationURL: URL { get set }
```

```objc
@property (nonatomic, copy) NSURL * javaScriptApplicationURL;
```

## See Also

### Providing Launch Information
- [var launchOptions: [String : Any]](./launchoptions.md)
  Data passed to the JavaScript launch callback method.
- [var storageIdentifier: String?](./storageidentifier.md)
  Optional identifier for a local storage file.
- [var supportsPictureInPicturePlayback: Bool](./supportspictureinpictureplayback.md)
  A Boolean value that indicates whether your app can display content in a picture-in-picture format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvmlkit/tvapplicationcontrollercontext/javascriptapplicationurl)*