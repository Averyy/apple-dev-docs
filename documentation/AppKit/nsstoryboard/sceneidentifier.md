# NSStoryboard.SceneIdentifier

**Framework**: AppKit  
**Kind**: typealias  
**Role**: Type Alias

A string that uniquely identifies a view controller or window controller in your storyboard file.

**Availability**:
- macOS

## Declaration

```swift
typealias SceneIdentifier = String
```

```c
typedef NSString * NSStoryboardSceneIdentifier;
```

#### Discussion

Set scene identifiers in your storyboard by assigning a value to the Storyboard ID attribute.

## See Also

### Instantiating Storyboard Controllers
- [func instantiateController(withIdentifier: NSStoryboard.SceneIdentifier) -> Any](./instantiatecontroller%28withidentifier%29.md)
  Instantiates a specified view controller or window controller from a storyboard.
- [func instantiateController<Controller>(identifier: NSStoryboard.SceneIdentifier, creator: ((NSCoder) -> Controller?)?) -> Controller](./instantiatecontroller%28identifier,creator%29-7ddcf.md)
  Creates the specified view controller from the storyboard and initializes it using your custom initialization code.
- [func instantiateController<Controller>(identifier: NSStoryboard.SceneIdentifier, creator: ((NSCoder) -> Controller?)?) -> Controller](./instantiatecontroller%28identifier,creator%29-50rw3.md)
  Creates the specified window controller from the storyboard and initializes it using your custom initialization code.
- [NSStoryboardControllerCreator](../nsstoryboardcontrollercreator.md)
  A block that you use to handle the custom creation of controller objects from your storyboard file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsstoryboard/sceneidentifier)*