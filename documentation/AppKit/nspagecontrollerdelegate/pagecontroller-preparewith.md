# pageController(_:prepare:with:)

**Framework**: Appkit  
**Kind**: method

Prepare the view controller and it’s view for drawing.

**Availability**:
- macOS 10.8+

## Declaration

```swift
@MainActor
optional func pageController(_ pageController: NSPageController, prepare viewController: NSViewController, with object: Any?)
```

#### Discussion

If this method is not implemented, then `viewController` object’s `representedObject` is set to the object.

> **Note**:  This method is called on the main thread and should return immediately. The view will be asked to draw on a background thread and must support background drawing.

This method is only useful if [`pageController(_:identifierFor:)`](nspagecontrollerdelegate/pagecontroller(_:identifierfor:).md) and [`pageController(_:prepare:with:)`](nspagecontrollerdelegate/pagecontroller(_:prepare:with:).md) are implemented.

## Parameters

- `pageController`: The page controller.
- `viewController`: The view controller to prepare for drawing. You should setup the data sources and perform layout.
- `object`: The object to display.

## See Also

- [func pageController(NSPageController, identifierFor: Any) -> NSPageController.ObjectIdentifier](nspagecontrollerdelegate/pagecontroller(_:identifierfor:).md)
  Return the identifier of the view controller that owns a view to display the object.
- [func pageController(NSPageController, viewControllerForIdentifier: NSPageController.ObjectIdentifier) -> NSViewController](nspagecontrollerdelegate/pagecontroller(_:viewcontrollerforidentifier:).md)
  Returns a view controller the page controller uses for managing the specified identifier.
- [func pageController(NSPageController, frameFor: Any?) -> NSRect](nspagecontrollerdelegate/pagecontroller(_:framefor:).md)
  Returns the frame appropriate for displaying the specified object.
- [NSPageController.ObjectIdentifier](nspagecontroller/objectidentifier.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspagecontrollerdelegate/pagecontroller(_:prepare:with:))*