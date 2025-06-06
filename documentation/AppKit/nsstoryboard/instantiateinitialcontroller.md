# instantiateInitialController()

**Framework**: AppKit  
**Kind**: method

Creates the initial view controller or window controller from a storyboard.

**Availability**:
- macOS 10.10+

## Declaration

```swift
func instantiateInitialController() -> Any?
```

#### Return Value

The initial view controller or window controller for the storyboard.

#### Discussion

Every storyboard has an initial view controller or window controller that represents its starting point. For the main storyboard, this is usually the first controller presented to the user at launch time. Designate the initial view controller in Interface Builder when configuring the storyboard file.

Typically, you call this method only when transitioning to the initial view controller in a different storyboard file. For your app’s main storyboard file—that is, the storyboard file specified in the app’s `Info.plist` file using the `UIMainStoryboardFile` key—the initial view controller is loaded into memory and presented automatically.

Each time you call this method, it creates a new instance of the initial controller.

## See Also

- [func instantiateInitialController<Controller>(creator: ((NSCoder) -> Controller?)?) -> Controller?](nsstoryboard/instantiateinitialcontroller(creator:)-pi04.md)
  Creates the initial view controller from the storyboard and initializes it using your custom code.
- [func instantiateInitialController<Controller>(creator: ((NSCoder) -> Controller?)?) -> Controller?](nsstoryboard/instantiateinitialcontroller(creator:)-529r1.md)
  Creates the initial window controller from the storyboard and initializes it using your custom code.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsstoryboard/instantiateinitialcontroller())*