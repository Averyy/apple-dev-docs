# viewDidLoad()

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Called after the view controller’s view has been loaded into memory.

**Availability**:
- macOS 10.10+

## Declaration

```swift
func viewDidLoad()
```

```objc
- (void) viewDidLoad;
```

#### Discussion

The tab view controller overrides this method and uses it to configure and layout the tab view and its contents. You can override it in your own subclasses to perform any custom initialization. For example, to replace the default tab view, override this method and set the value of the [`tabView`](./tabview.md) property before calling `super`.

If you override this method, you must call `super` in your implementation.

## See Also

### Responding to Tab View Events
- [func tabView(NSTabView, shouldSelect: NSTabViewItem?) -> Bool](./tabview%28_,shouldselect%29.md)
  Asks the tab view controller if the specified tab should be selected.
- [func tabView(NSTabView, willSelect: NSTabViewItem?)](./tabview%28_,willselect%29.md)
  Informs the tab view controller that the specified tab is about to be selected.
- [func tabView(NSTabView, didSelect: NSTabViewItem?)](./tabview%28_,didselect%29.md)
  Informs the tab view controller that the specified tab was selected.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstabviewcontroller/viewdidload())*