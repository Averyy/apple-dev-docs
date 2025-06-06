# dismissPopover(_:)

**Framework**: AppKit  
**Kind**: method

Restores the previously visible main bar.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.12.2+

## Declaration

```swift
@MainActor
func dismissPopover(_ sender: Any?)
```

#### Discussion

This method has the same effect as the user tapping the optional close button.

## See Also

- [func showPopover(Any?)](nspopovertouchbaritem/showpopover(_:).md)
  Replaces the main bar with this item’s popover bar.
- [func makeStandardActivatePopoverGestureRecognizer() -> NSGestureRecognizer](nspopovertouchbaritem/makestandardactivatepopovergesturerecognizer.md)
  Returns a gesture recognizer, configured to invoke the [`showPopover(_:)`](nspopovertouchbaritem/showpopover(_:).md) method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspopovertouchbaritem/dismisspopover(_:))*