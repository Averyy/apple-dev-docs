# viewWillAppear()

**Framework**: Image Playground  
**Kind**: method  
**Role**: Instance Method

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

### Managing the view
- [func viewDidLoad()](./viewdidload%28%29.md)
  Called after the controller’s view is loaded into memory.
- [func viewDidDisappear()](./viewdiddisappear%28%29.md)
  Notifies the view controller that its view is about to be removed from a view hierarchy.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imageplayground/imageplaygroundviewcontroller/viewwillappear())*