# pageController(_:frameFor:)

**Framework**: AppKit  
**Kind**: method

Returns the frame appropriate for displaying the specified object.

**Availability**:
- macOS 10.8+

## Declaration

```swift
@MainActor
optional func pageController(_ pageController: NSPageController, frameFor object: Any?) -> NSRect
```

#### Return Value

The frame appropriate for displaying `object`.

#### Discussion

You only need to implement this if the view frame can differ between the page controller’s [`arrangedObjects`](nspagecontroller/arrangedobjects.md).

This method must return immediately. Avoid file, network or any potentially blocking or lengthy work to provide an answer.

If this method is not implemented, all [`arrangedObjects`](nspagecontroller/arrangedobjects.md) are assumed to have the same frame as the `pageController` object’s current [`selectedViewController`](nspagecontroller/selectedviewcontroller.md) instance’s `view` or the bounds of `view` when [`selectedViewController`](nspagecontroller/selectedviewcontroller.md) is `nil`.

This method is only useful if [`pageController(_:identifierFor:)`](nspagecontrollerdelegate/pagecontroller(_:identifierfor:).md) and [`pageController(_:viewControllerForIdentifier:)`](nspagecontrollerdelegate/pagecontroller(_:viewcontrollerforidentifier:).md) are implemented.

## Parameters

- `pageController`: The page controller.
- `object`: The object to display.

## See Also

- [func pageController(NSPageController, identifierFor: Any) -> NSPageController.ObjectIdentifier](nspagecontrollerdelegate/pagecontroller(_:identifierfor:).md)
  Return the identifier of the view controller that owns a view to display the object.
- [func pageController(NSPageController, viewControllerForIdentifier: NSPageController.ObjectIdentifier) -> NSViewController](nspagecontrollerdelegate/pagecontroller(_:viewcontrollerforidentifier:).md)
  Returns a view controller the page controller uses for managing the specified identifier.
- [func pageController(NSPageController, prepare: NSViewController, with: Any?)](nspagecontrollerdelegate/pagecontroller(_:prepare:with:).md)
  Prepare the view controller and it’s view for drawing.
- [NSPageController.ObjectIdentifier](nspagecontroller/objectidentifier.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspagecontrollerdelegate/pagecontroller(_:framefor:))*