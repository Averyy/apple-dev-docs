# NSStoryboardControllerCreator

**Framework**: AppKit  
**Kind**: typealias  
**Role**: Type Alias

A block that you use to handle the custom creation of controller objects from your storyboard file.

**Availability**:
- macOS

## Declaration

```c
typedef id (^)(NSCoder *) NSStoryboardControllerCreator;
```

## Discussion

Use your block to construct a window or view controller using a custom initialization method. Your custom method must accept an [`NSCoder`](../Foundation/nscoder.md) object as one of its parameters, and it may include other parameters that you need to initialize the contents of the object. The implementation of your method must call the inherited [`init(coder:)`](./nsresponder/init%28coder%29.md) method at some point during its execution. Not doing so is a programmer error.

## Parameters

- `coder`: The coder object containing the storyboard data to use when configuring the window controller.

## See Also

### Instantiating Storyboard Controllers
- [func instantiateController(withIdentifier: NSStoryboard.SceneIdentifier) -> Any](./nsstoryboard/instantiatecontroller%28withidentifier%29.md)
  Instantiates a specified view controller or window controller from a storyboard.
- [NSStoryboard.SceneIdentifier](./nsstoryboard/sceneidentifier.md)
  A string that uniquely identifies a view controller or window controller in your storyboard file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsstoryboardcontrollercreator)*