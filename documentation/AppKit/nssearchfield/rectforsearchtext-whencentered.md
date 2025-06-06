# rectForSearchText(whenCentered:)

**Framework**: AppKit  
**Kind**: method

The rectangle for the search text within the bounds of the field.

**Availability**:
- macOS 10.11+

## Declaration

```swift
@MainActor
func rectForSearchText(whenCentered isCentered: Bool) -> NSRect
```

## Parameters

- `isCentered`: A Boolean value that indicates whether the search field’s components are centered within the control. For more information, see  .

## See Also

- [var centersPlaceholder: Bool](nssearchfield/centersplaceholder.md)
  A Boolean value that determines whether the search field’s components are centered within the control.
- [func rectForCancelButton(whenCentered: Bool) -> NSRect](nssearchfield/rectforcancelbutton(whencentered:).md)
  The rectangle for the cancel button within the bounds of the search field.
- [func rectForSearchButton(whenCentered: Bool) -> NSRect](nssearchfield/rectforsearchbutton(whencentered:).md)
  The rectangle for the search button within the bounds of the search field.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssearchfield/rectforsearchtext(whencentered:))*