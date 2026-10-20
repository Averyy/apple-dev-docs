# viewIfLoaded

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

**Availability**:
- macOS 14.0+

## Declaration

```swift
var viewIfLoaded: NSView? { get }
```

```objc
@property (strong, readonly, nullable) NSView * viewIfLoaded;
```

## See Also

### Responding to View Events
- [func viewDidLoad()](./viewdidload%28%29.md)
  Called after the view controller’s view has been loaded into memory.
- [func loadViewIfNeeded()](./loadviewifneeded%28%29.md)
- [var isViewLoaded: Bool](./isviewloaded.md)
  A Boolean value indicating whether the view controller’s view is loaded into memory.
- [func viewWillAppear()](./viewwillappear%28%29.md)
  Called after the view controller’s view has been loaded into memory is about to be added to the view hierarchy in the window.
- [func viewDidAppear()](./viewdidappear%28%29.md)
  Called when the view controller’s view is fully transitioned onto the screen.
- [func viewWillDisappear()](./viewwilldisappear%28%29.md)
  Called when the view controller’s view is about to be removed from the view hierarchy in the window.
- [func viewDidDisappear()](./viewdiddisappear%28%29.md)
  Called after the view controller’s view is removed from the view hierarchy in a window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsviewcontroller/viewifloaded)*