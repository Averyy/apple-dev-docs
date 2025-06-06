# animatePresentation(of:from:)

**Framework**: AppKit  
**Kind**: method  
**Required**: Yes

Called when the specified view controller is about to be presented.

**Availability**:
- macOS 10.10+

## Declaration

```swift
@MainActor
func animatePresentation(of viewController: NSViewController, from fromViewController: NSViewController)
```

#### Discussion

To add custom presentation animation, Implement it in this method.

## Parameters

- `viewController`: The view controller that is being presented in place of the one in the   parameter.
- `fromViewController`: The view controller that is the parent of the one in the   parameter.

## See Also

- [func animateDismissal(of: NSViewController, from: NSViewController)](nsviewcontrollerpresentationanimator/animatedismissal(of:from:).md)
  Called when a previously-presented view controller is about to be dismissed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsviewcontrollerpresentationanimator/animatepresentation(of:from:))*