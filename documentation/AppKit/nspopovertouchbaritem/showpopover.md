# showPopover(_:)

**Framework**: AppKit  
**Kind**: method

Replaces the main bar with this item’s popover bar.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.12.2+

## Declaration

```swift
@MainActor
func showPopover(_ sender: Any?)
```

#### Discussion

If this item is not visible, this method will have no effect.

## See Also

- [func dismissPopover(Any?)](nspopovertouchbaritem/dismisspopover(_:).md)
  Restores the previously visible main bar.
- [func makeStandardActivatePopoverGestureRecognizer() -> NSGestureRecognizer](nspopovertouchbaritem/makestandardactivatepopovergesturerecognizer.md)
  Returns a gesture recognizer, configured to invoke the [`showPopover(_:)`](nspopovertouchbaritem/showpopover(_:).md) method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspopovertouchbaritem/showpopover(_:))*