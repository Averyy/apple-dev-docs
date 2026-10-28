# makeStandardActivatePopoverGestureRecognizer()

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns a gesture recognizer, configured to invoke the [`showPopover(_:)`](./showpopover%28_%29.md) method.

**Availability**:
- macOS 10.12.2+

## Declaration

```swift
func makeStandardActivatePopoverGestureRecognizer() -> NSGestureRecognizer
```

```objc
- (NSGestureRecognizer *) makeStandardActivatePopoverGestureRecognizer;
```

## Discussion

Use this method to create a gesture recognizer that you then attach to a custom [`collapsedRepresentation`](./collapsedrepresentation.md) view.

## See Also

### Expanding and collapsing a popover
- [func showPopover(Any?)](./showpopover%28_%29.md)
  Replaces the main bar with this item’s popover bar.
- [func dismissPopover(Any?)](./dismisspopover%28_%29.md)
  Restores the previously visible main bar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspopovertouchbaritem/makestandardactivatepopovergesturerecognizer())*