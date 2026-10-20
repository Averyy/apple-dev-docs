# navigateBack(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Navigates backwards in the page controller’s arranged objects array.

**Availability**:
- macOS 10.8+

## Declaration

```swift
@IBAction
func navigateBack(_ sender: Any?)
```

```objc
- (void) navigateBack:(id) sender;
```

#### Discussion

This method is typically invoked in response to a user interacting with a control, the `sender`.

This method is animated and invokes the delegate’s [`pageControllerWillStartLiveTransition(_:)`](../nspagecontrollerdelegate/pagecontrollerwillstartlivetransition%28_%29.md) and [`pageControllerDidEndLiveTransition(_:)`](../nspagecontrollerdelegate/pagecontrollerdidendlivetransition%28_%29.md) methods.

## Parameters

- `sender`: The sender.

## See Also

### Related Documentation
- [func navigateForward(to: Any)](./navigateforward%28to%29.md)
  Navigates to the specific object.
### Page Controller Navigation
- [func navigateForward(Any?)](./navigateforward%28_%29.md)
  Navigates to the next object in the page controller’s arranged objects array, if appropriate.
- [func takeSelectedIndexFrom(Any?)](./takeselectedindexfrom%28_%29.md)
  Navigates to the selected index, which is taken from the sender.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspagecontroller/navigateback(_:))*