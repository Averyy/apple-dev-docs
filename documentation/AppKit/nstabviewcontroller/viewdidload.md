# viewDidLoad()

**Framework**: AppKit  
**Kind**: method

Called after the view controller’s view has been loaded into memory.

**Availability**:
- macOS 10.10+

## Declaration

```swift
@MainActor
func viewDidLoad()
```

#### Discussion

The tab view controller overrides this method and uses it to configure and layout the tab view and its contents. You can override it in your own subclasses to perform any custom initialization. For example, to replace the default tab view, override this method and set the value of the [`tabView`](nstabviewcontroller/tabview.md) property before calling `super`.

If you override this method, you must call `super` in your implementation.

## See Also

- [func tabView(NSTabView, shouldSelect: NSTabViewItem?) -> Bool](nstabviewcontroller/tabview(_:shouldselect:).md)
  Asks the tab view controller if the specified tab should be selected.
- [func tabView(NSTabView, willSelect: NSTabViewItem?)](nstabviewcontroller/tabview(_:willselect:).md)
  Informs the tab view controller that the specified tab is about to be selected.
- [func tabView(NSTabView, didSelect: NSTabViewItem?)](nstabviewcontroller/tabview(_:didselect:).md)
  Informs the tab view controller that the specified tab was selected.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstabviewcontroller/viewdidload())*