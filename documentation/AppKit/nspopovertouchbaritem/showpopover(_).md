# showPopover(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Replaces the main bar with this item’s popover bar.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.12.2+

## Declaration

```swift
func showPopover(_ sender: Any?)
```

```objc
- (void) showPopover:(id) sender;
```

## Discussion

If this item is not visible, this method will have no effect.

## See Also

### Expanding and collapsing a popover
- [func dismissPopover(Any?)](./dismisspopover%28_%29.md)
  Restores the previously visible main bar.
- [func makeStandardActivatePopoverGestureRecognizer() -> NSGestureRecognizer](./makestandardactivatepopovergesturerecognizer%28%29.md)
  Returns a gesture recognizer, configured to invoke the [`showPopover(_:)`](./showpopover%28_%29.md) method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspopovertouchbaritem/showpopover(_:))*