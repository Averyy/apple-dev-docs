# pageController(_:viewControllerForIdentifier:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns a view controller the page controller uses for managing the specified identifier.

**Availability**:
- macOS 10.8+

## Declaration

```swift
@MainActor
optional func pageController(_ pageController: NSPageController, viewControllerForIdentifier identifier: NSPageController.ObjectIdentifier) -> NSViewController
```

```objc
- (NSViewController *) pageController:(NSPageController *) pageController viewControllerForIdentifier:(NSPageControllerObjectIdentifier) identifier;
```

## Return Value

Returns the view controller for the specified identifier.

## Discussion

Your implementation of this method should return the requested view controller for the identifier or create and return a new view controller.

`NSPageController` will cache as many view controllers and views as necessary to maintain performance. This method is called whenever another instance is required.

The view controller may become the [`selectedViewController`](../nspagecontroller/selectedviewcontroller.md) after a transition if necessary.

## Parameters

- `pageController`: The page controller.
- `identifier`: The identifier for a view controller.

## See Also

### Managing View Controllers
- [func pageController(NSPageController, identifierFor: Any) -> NSPageController.ObjectIdentifier](./pagecontroller%28_,identifierfor%29.md)
  Return the identifier of the view controller that owns a view to display the object.
- [func pageController(NSPageController, prepare: NSViewController, with: Any?)](./pagecontroller%28_,prepare,with%29.md)
  Prepare the view controller and it’s view for drawing.
- [func pageController(NSPageController, frameFor: Any?) -> NSRect](./pagecontroller%28_,framefor%29.md)
  Returns the frame appropriate for displaying the specified object.
- [NSPageController.ObjectIdentifier](../nspagecontroller/objectidentifier.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspagecontrollerdelegate/pagecontroller(_:viewcontrollerforidentifier:))*