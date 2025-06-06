# viewDidDisappear()

**Framework**: AppKit  
**Kind**: method

Called after the title bar accessory view controller’s view is removed from the window’s view hierarchy.

**Availability**:
- macOS 10.10+

## Declaration

```swift
@MainActor
func viewDidDisappear()
```

#### Discussion

You can override this method to perform tasks associated with removing the title bar accessory view controller’s view from the window’s view hierarchy—such as releasing resources not needed when the view is not visible or no longer part of the window—but you must call `super` in your implementation.

## See Also

- [func viewDidAppear()](nstitlebaraccessoryviewcontroller/viewdidappear.md)
  Called when the title bar accessory view controller’s view is fully transitioned onto the screen.
- [func viewWillAppear()](nstitlebaraccessoryviewcontroller/viewwillappear.md)
  Called after the title bar accessory view controller’s view has been loaded into memory is about to be added to the view hierarchy in the window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstitlebaraccessoryviewcontroller/viewdiddisappear())*