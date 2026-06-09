# viewWillAppear()

**Framework**: Image Playground  
**Kind**: method

Notifies the view controller that its view is about to be added to a view hierarchy.

**Availability**:
- macOS 15.1+

## Declaration

```swift
@MainActor
@preconcurrency override dynamic func viewWillAppear()
```

#### Discussion

The view controller uses this method to configure its interface.

## See Also

- [func viewDidLoad()](imageplaygroundviewcontroller/viewdidload.md)
  Called after the controller’s view is loaded into memory.
- [func viewDidDisappear()](imageplaygroundviewcontroller/viewdiddisappear.md)
  Notifies the view controller that its view is about to be removed from a view hierarchy.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imageplayground/imageplaygroundviewcontroller/viewwillappear())*