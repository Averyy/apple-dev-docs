# animateDismissal(of:from:)

**Framework**: AppKit  
**Kind**: method  
**Required**: Yes

Called when a previously-presented view controller is about to be dismissed.

**Availability**:
- macOS 10.10+

## Declaration

```swift
@MainActor
func animateDismissal(of viewController: NSViewController, from fromViewController: NSViewController)
```

#### Discussion

To add custom view controller dismissal animation, Implement it in this method.

## Parameters

- `viewController`: The view controller that is being dismissed.
- `fromViewController`: The view controller that is the parent of the one in the   parameter.

## See Also

- [func animatePresentation(of: NSViewController, from: NSViewController)](nsviewcontrollerpresentationanimator/animatepresentation(of:from:).md)
  Called when the specified view controller is about to be presented.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsviewcontrollerpresentationanimator/animatedismissal(of:from:))*