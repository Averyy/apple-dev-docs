# TVApplicationControllerContext

**Framework**: TVMLKit  
**Kind**: class

Launch information provided to the TV application controller.

**Availability**:
- tvOS 9.0+

## Declaration

```swift
class TVApplicationControllerContext
```

## Topics

### Providing Launch Information
- [var javaScriptApplicationURL: URL](tvapplicationcontrollercontext/javascriptapplicationurl.md)
  URL pointing to the controlling JavaScript file for the application.
- [var launchOptions: [String : Any]](tvapplicationcontrollercontext/launchoptions.md)
  Data passed to the JavaScript launch callback method.
- [var storageIdentifier: String?](tvapplicationcontrollercontext/storageidentifier.md)
  Optional identifier for a local storage file.
- [var supportsPictureInPicturePlayback: Bool](tvapplicationcontrollercontext/supportspictureinpictureplayback.md)
  A Boolean value that indicates whether your app can display content in a picture-in-picture format.

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSCopying](../foundation/nscopying.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## See Also

- [Implementing a Hybrid TV App with TVMLKit](implementing-a-hybrid-tv-app-with-tvmlkit.md)
  Display content options with document view controllers and fetch and populate content with TVMLKit JS.
- [class TVApplicationController](tvapplicationcontroller.md)
  An object that bridges the UI, navigation stack, storage, and event handling from JavaScript.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvmlkit/tvapplicationcontrollercontext)*