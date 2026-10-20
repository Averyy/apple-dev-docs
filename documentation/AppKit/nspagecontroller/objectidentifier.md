# NSPageController.ObjectIdentifier

**Framework**: AppKit  
**Kind**: typealias  
**Role**: Type Alias

**Availability**:
- macOS

## Declaration

```swift
typealias ObjectIdentifier = String
```

```c
typedef NSString * NSPageControllerObjectIdentifier;
```

## See Also

### Managing View Controllers
- [func pageController(NSPageController, identifierFor: Any) -> NSPageController.ObjectIdentifier](../nspagecontrollerdelegate/pagecontroller%28_,identifierfor%29.md)
  Return the identifier of the view controller that owns a view to display the object.
- [func pageController(NSPageController, viewControllerForIdentifier: NSPageController.ObjectIdentifier) -> NSViewController](../nspagecontrollerdelegate/pagecontroller%28_,viewcontrollerforidentifier%29.md)
  Returns a view controller the page controller uses for managing the specified identifier.
- [func pageController(NSPageController, prepare: NSViewController, with: Any?)](../nspagecontrollerdelegate/pagecontroller%28_,prepare,with%29.md)
  Prepare the view controller and it’s view for drawing.
- [func pageController(NSPageController, frameFor: Any?) -> NSRect](../nspagecontrollerdelegate/pagecontroller%28_,framefor%29.md)
  Returns the frame appropriate for displaying the specified object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspagecontroller/objectidentifier)*