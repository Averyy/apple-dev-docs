# transitionStyle

**Framework**: AppKit  
**Kind**: property

The transition style the page controller uses when changing pages.

**Availability**:
- macOS 10.8+

## Declaration

```swift
@MainActor
var transitionStyle: NSPageController.TransitionStyle { get set }
```

#### Discussion

The possible values for the transition style are discussed in [`NSPageController.TransitionStyle`](nspagecontroller/transitionstyle-swift.enum.md).

The default value is [`NSPageController.TransitionStyle.stackHistory`](nspagecontroller/transitionstyle-swift.enum/stackhistory.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspagecontroller/transitionstyle-swift.property)*