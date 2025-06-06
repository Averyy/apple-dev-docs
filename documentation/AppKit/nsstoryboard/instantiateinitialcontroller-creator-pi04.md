# instantiateInitialController(creator:)

**Framework**: AppKit  
**Kind**: method

Creates the initial view controller from the storyboard and initializes it using your custom code.

**Availability**:
- macOS 10.15+

## Declaration

```swift
func instantiateInitialController<Controller>(creator: ((NSCoder) -> Controller?)? = nil) -> Controller? where Controller : NSViewController
```

#### Return Value

The initial view controller in the storyboard.

#### Discussion

Every storyboard file has an initial controller object that represents the default interface to create. Use this method to construct that object using a custom code that you provide. Use this method when the constructor for your object takes parameters in addition to the specified `coder` object.

In your `creator` block, create the view controller using your custom constructor method. Your custom constructor method must accept an [`NSCoder`](https://developer.apple.com/documentation/Foundation/NSCoder) parameter and must call the inherited [`init(coder:)`](https://developer.apple.com/documentation/OSLog/OSLogEntry/init(coder:)) method at some point during its execution. Not doing so is a programmer error.

## Parameters

- `creator`: If you return   from your block, this method creates the view controller using the default   method.

## See Also

- [func instantiateInitialController() -> Any?](nsstoryboard/instantiateinitialcontroller.md)
  Creates the initial view controller or window controller from a storyboard.
- [func instantiateInitialController<Controller>(creator: ((NSCoder) -> Controller?)?) -> Controller?](nsstoryboard/instantiateinitialcontroller(creator:)-529r1.md)
  Creates the initial window controller from the storyboard and initializes it using your custom code.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsstoryboard/instantiateinitialcontroller(creator:)-pi04)*