# makeStandardActivatePopoverGestureRecognizer()

**Framework**: AppKit  
**Kind**: method

Returns a gesture recognizer, configured to invoke the [`showPopover(_:)`](nspopovertouchbaritem/showpopover(_:).md) method.

**Availability**:
- macOS 10.12.2+

## Declaration

```swift
@MainActor
func makeStandardActivatePopoverGestureRecognizer() -> NSGestureRecognizer
```

#### Discussion

Use this method to create a gesture recognizer that you then attach to a custom [`collapsedRepresentation`](nspopovertouchbaritem/collapsedrepresentation.md) view.

## See Also

- [func showPopover(Any?)](nspopovertouchbaritem/showpopover(_:).md)
  Replaces the main bar with this item’s popover bar.
- [func dismissPopover(Any?)](nspopovertouchbaritem/dismisspopover(_:).md)
  Restores the previously visible main bar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspopovertouchbaritem/makestandardactivatepopovergesturerecognizer())*