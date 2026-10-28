# pageController(_:prepare:with:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Prepare the view controller and it’s view for drawing.

**Availability**:
- macOS 10.8+

## Declaration

```swift
@MainActor
optional func pageController(_ pageController: NSPageController, prepare viewController: NSViewController, with object: Any?)
```

```objc
- (void) pageController:(NSPageController *) pageController prepareViewController:(NSViewController *) viewController withObject:(id) object;
```

## Discussion

If this method is not implemented, then `viewController` object’s `representedObject` is set to the object.

> **Note**:  This method is called on the main thread and should return immediately. The view will be asked to draw on a background thread and must support background drawing.

This method is only useful if [`pageController(_:identifierFor:)`](./pagecontroller%28_,identifierfor%29.md) and [`pageController(_:prepare:with:)`](./pagecontroller%28_,prepare,with%29.md) are implemented.

## Parameters

- `pageController`: The page controller.
- `viewController`: The view controller to prepare for drawing. You should setup the data sources and perform layout.
- `object`: The object to display.

## See Also

### Managing View Controllers
- [func pageController(NSPageController, identifierFor: Any) -> NSPageController.ObjectIdentifier](./pagecontroller%28_,identifierfor%29.md)
  Return the identifier of the view controller that owns a view to display the object.
- [func pageController(NSPageController, viewControllerForIdentifier: NSPageController.ObjectIdentifier) -> NSViewController](./pagecontroller%28_,viewcontrollerforidentifier%29.md)
  Returns a view controller the page controller uses for managing the specified identifier.
- [func pageController(NSPageController, frameFor: Any?) -> NSRect](./pagecontroller%28_,framefor%29.md)
  Returns the frame appropriate for displaying the specified object.
- [NSPageController.ObjectIdentifier](../nspagecontroller/objectidentifier.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspagecontrollerdelegate/pagecontroller(_:prepare:with:))*