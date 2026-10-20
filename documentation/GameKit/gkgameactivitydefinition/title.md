# title

**Framework**: GameKit  
**Kind**: property  
**Role**: Instance Property

A short title for the game activity.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
var title: String { get }
```

```objc
@property (nonatomic, copy, readonly) NSString * title;
```

## See Also

### Getting the display properties and image
- [var details: String?](./details.md)
  A more detailed description of the game activity.
- [var defaultProperties: [String : String]](./defaultproperties.md)
  Default properties defined by the developer for this type of game activity.
- [func loadImage(completionHandler: (UIImage?, (any Error)?) -> Void)](./loadimage%28completionhandler%29.md)
  Asynchronously load the image. Error will be nil on success.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkgameactivitydefinition/title)*