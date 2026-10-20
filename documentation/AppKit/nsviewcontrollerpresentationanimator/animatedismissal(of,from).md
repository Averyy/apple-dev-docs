# animateDismissal(of:from:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Called when a previously-presented view controller is about to be dismissed.

**Availability**:
- macOS 10.10+

## Declaration

```swift
@MainActor
func animateDismissal(of viewController: NSViewController, from fromViewController: NSViewController)
```

```objc
- (void) animateDismissalOfViewController:(NSViewController *) viewController fromViewController:(NSViewController *) fromViewController;
```

#### Discussion

To add custom view controller dismissal animation, Implement it in this method.

## Parameters

- `viewController`: The view controller that is being dismissed.
- `fromViewController`: The view controller that is the parent of the one in the `viewController` parameter.

## See Also

### Animating Presentation and Dismissal of View Controllers
- [func animatePresentation(of: NSViewController, from: NSViewController)](./animatepresentation%28of,from%29.md)
  Called when the specified view controller is about to be presented.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsviewcontrollerpresentationanimator/animatedismissal(of:from:))*