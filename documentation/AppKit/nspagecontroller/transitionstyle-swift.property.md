# transitionStyle

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The transition style the page controller uses when changing pages.

**Availability**:
- macOS 10.8+

## Declaration

```swift
var transitionStyle: NSPageController.TransitionStyle { get set }
```

```objc
@property NSPageControllerTransitionStyle transitionStyle;
```

## Discussion

The possible values for the transition style are discussed in [`NSPageController.TransitionStyle`](./transitionstyle-swift.enum.md).

The default value is [`NSPageController.TransitionStyle.stackHistory`](./transitionstyle-swift.enum/stackhistory.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspagecontroller/transitionstyle-swift.property)*