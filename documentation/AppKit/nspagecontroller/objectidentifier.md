# NSPageController.ObjectIdentifier

**Framework**: AppKit  
**Kind**: typealias

**Availability**:
- macOS ?+

## Declaration

```swift
typealias ObjectIdentifier = String
```

## See Also

- [func pageController(NSPageController, identifierFor: Any) -> NSPageController.ObjectIdentifier](nspagecontrollerdelegate/pagecontroller(_:identifierfor:).md)
  Return the identifier of the view controller that owns a view to display the object.
- [func pageController(NSPageController, viewControllerForIdentifier: NSPageController.ObjectIdentifier) -> NSViewController](nspagecontrollerdelegate/pagecontroller(_:viewcontrollerforidentifier:).md)
  Returns a view controller the page controller uses for managing the specified identifier.
- [func pageController(NSPageController, prepare: NSViewController, with: Any?)](nspagecontrollerdelegate/pagecontroller(_:prepare:with:).md)
  Prepare the view controller and it’s view for drawing.
- [func pageController(NSPageController, frameFor: Any?) -> NSRect](nspagecontrollerdelegate/pagecontroller(_:framefor:).md)
  Returns the frame appropriate for displaying the specified object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspagecontroller/objectidentifier)*