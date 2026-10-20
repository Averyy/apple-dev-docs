# defaultProperties

**Framework**: GameKit  
**Kind**: property  
**Role**: Instance Property

Default properties defined by the developer for this type of game activity.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
var defaultProperties: [String : String] { get }
```

```objc
@property (nonatomic, copy, readonly) NSDictionary<NSString *,NSString *> * defaultProperties;
```

## See Also

### Getting the display properties and image
- [var title: String](./title.md)
  A short title for the game activity.
- [var details: String?](./details.md)
  A more detailed description of the game activity.
- [func loadImage(completionHandler: (UIImage?, (any Error)?) -> Void)](./loadimage%28completionhandler%29.md)
  Asynchronously load the image. Error will be nil on success.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkgameactivitydefinition/defaultproperties)*