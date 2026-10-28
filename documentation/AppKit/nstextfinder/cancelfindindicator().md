# cancelFindIndicator()

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Cancels the find indicator immediately.

**Availability**:
- macOS 10.7+

## Declaration

```swift
func cancelFindIndicator()
```

```objc
- (void) cancelFindIndicator;
```

## Discussion

There may be some circumstances where the find indicator should be immediately cancelled or hidden, such as when the view’s content or selection is changed without the knowledge of the text finder. This method will immediately cancel the current find indicator.

The `NSTextFinder` and `NSView` classes will handle the find indicator correctly when a content view is resized, moved, or removed from the view hierarchy. If your content view’s scrolling is done by an `NSScrollView`, the find indicator will also be handled for you during scrolling.

## See Also

### Related Documentation
- [var findIndicatorNeedsUpdate: Bool](./findindicatorneedsupdate.md)
  Invoke to specify that the find indicator needs updating when not contained within a scroll view.
### Validating and Performing Text Finding
- [func performAction(NSTextFinder.Action)](./performaction%28_%29.md)
  Performs the specified text finding action.
- [func validateAction(NSTextFinder.Action) -> Bool](./validateaction%28_%29.md)
  Allows validation of the find action before performing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextfinder/cancelfindindicator())*