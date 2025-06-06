# instantiateController(identifier:creator:)

**Framework**: AppKit  
**Kind**: method

Creates the specified view controller from the storyboard and initializes it using your custom initialization code.

**Availability**:
- macOS 10.15+

## Declaration

```swift
func instantiateController<Controller>(identifier: NSStoryboard.SceneIdentifier, creator: ((NSCoder) -> Controller?)? = nil) -> Controller where Controller : NSViewController
```

#### Return Value

The view controller that corresponds to the specified identifier string. If no view controller has the given identifier, this method throws an exception.

#### Discussion

Use this method to create a view controller object programmatically. Each time you call this method, it creates a new instance of the view controller using the block you provide.

In your `creator` block, create the view controller using your custom constructor method. Your custom initialization method must accept an [`NSCoder`](https://developer.apple.com/documentation/Foundation/NSCoder) object as a parameter and must call the inherited [`init(coder:)`](https://developer.apple.com/documentation/OSLog/OSLogEntry/init(coder:)) method during its execution. Not doing so is a programmer error. After initializing the storyboard state, initialize your view controller’s custom properties.

## Parameters

- `identifier`: If the specified identifier does not exist in the storyboard file, this method raises an exception.
- `creator`: If you return   from your block, this method creates the view controller using the default   method.

## See Also

- [func instantiateController(withIdentifier: NSStoryboard.SceneIdentifier) -> Any](nsstoryboard/instantiatecontroller(withidentifier:).md)
  Instantiates a specified view controller or window controller from a storyboard.
- [func instantiateController<Controller>(identifier: NSStoryboard.SceneIdentifier, creator: ((NSCoder) -> Controller?)?) -> Controller](nsstoryboard/instantiatecontroller(identifier:creator:)-50rw3.md)
  Creates the specified window controller from the storyboard and initializes it using your custom initialization code.
- [NSStoryboard.SceneIdentifier](nsstoryboard/sceneidentifier.md)
  A string that uniquely identifies a view controller or window controller in your storyboard file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsstoryboard/instantiatecontroller(identifier:creator:)-7ddcf)*