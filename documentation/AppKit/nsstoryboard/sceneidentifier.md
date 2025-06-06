# NSStoryboard.SceneIdentifier

**Framework**: AppKit  
**Kind**: typealias

A string that uniquely identifies a view controller or window controller in your storyboard file.

**Availability**:
- macOS ?+

## Declaration

```swift
typealias SceneIdentifier = String
```

#### Discussion

Set scene identifiers in your storyboard by assigning a value to the Storyboard ID attribute.

## See Also

- [func instantiateController(withIdentifier: NSStoryboard.SceneIdentifier) -> Any](nsstoryboard/instantiatecontroller(withidentifier:).md)
  Instantiates a specified view controller or window controller from a storyboard.
- [func instantiateController<Controller>(identifier: NSStoryboard.SceneIdentifier, creator: ((NSCoder) -> Controller?)?) -> Controller](nsstoryboard/instantiatecontroller(identifier:creator:)-7ddcf.md)
  Creates the specified view controller from the storyboard and initializes it using your custom initialization code.
- [func instantiateController<Controller>(identifier: NSStoryboard.SceneIdentifier, creator: ((NSCoder) -> Controller?)?) -> Controller](nsstoryboard/instantiatecontroller(identifier:creator:)-50rw3.md)
  Creates the specified window controller from the storyboard and initializes it using your custom initialization code.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsstoryboard/sceneidentifier)*