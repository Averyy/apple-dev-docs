# takeSelectedIndexFrom(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Navigates to the selected index, which is taken from the sender.

**Availability**:
- macOS 10.8+

## Declaration

```swift
@IBAction
func takeSelectedIndexFrom(_ sender: Any?)
```

```objc
- (void) takeSelectedIndexFrom:(id) sender;
```

## Discussion

When invoked, this method causes the page controller’s view to display the object specified by the value taken from the `sender` control.

This method is animated and invokes the delegate’s [`pageControllerWillStartLiveTransition(_:)`](../nspagecontrollerdelegate/pagecontrollerwillstartlivetransition%28_%29.md) and [`pageControllerDidEndLiveTransition(_:)`](../nspagecontrollerdelegate/pagecontrollerdidendlivetransition%28_%29.md) methods.

## Parameters

- `sender`: The control that invoked the action.

## See Also

### Related Documentation
- [func navigateForward(to: Any)](./navigateforward%28to%29.md)
  Navigates to the specific object.
### Page Controller Navigation
- [func navigateBack(Any?)](./navigateback%28_%29.md)
  Navigates backwards in the page controller’s arranged objects array.
- [func navigateForward(Any?)](./navigateforward%28_%29.md)
  Navigates to the next object in the page controller’s arranged objects array, if appropriate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspagecontroller/takeselectedindexfrom(_:))*