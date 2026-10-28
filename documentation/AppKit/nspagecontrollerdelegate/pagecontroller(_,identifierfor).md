# pageController(_:identifierFor:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Return the identifier of the view controller that owns a view to display the object.

**Availability**:
- macOS 10.8+

## Declaration

```swift
@MainActor
optional func pageController(_ pageController: NSPageController, identifierFor object: Any) -> NSPageController.ObjectIdentifier
```

```objc
- (NSPageControllerObjectIdentifier) pageController:(NSPageController *) pageController identifierForObject:(id) object;
```

## Return Value

Returns a string identifier for the view controller for the specified object.

## Discussion

If `pageController` does not have an unused view controller for this identifier, the you will be asked to create one via [`pageController(_:viewControllerForIdentifier:)`](./pagecontroller%28_,viewcontrollerforidentifier%29.md).

## Parameters

- `pageController`: The page controller.
- `object`: The object to display.

## See Also

### Managing View Controllers
- [func pageController(NSPageController, viewControllerForIdentifier: NSPageController.ObjectIdentifier) -> NSViewController](./pagecontroller%28_,viewcontrollerforidentifier%29.md)
  Returns a view controller the page controller uses for managing the specified identifier.
- [func pageController(NSPageController, prepare: NSViewController, with: Any?)](./pagecontroller%28_,prepare,with%29.md)
  Prepare the view controller and it’s view for drawing.
- [func pageController(NSPageController, frameFor: Any?) -> NSRect](./pagecontroller%28_,framefor%29.md)
  Returns the frame appropriate for displaying the specified object.
- [NSPageController.ObjectIdentifier](../nspagecontroller/objectidentifier.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspagecontrollerdelegate/pagecontroller(_:identifierfor:))*