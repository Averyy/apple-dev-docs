# rectForCancelButton(whenCentered:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

The rectangle for the cancel button within the bounds of the search field.

**Availability**:
- macOS 10.11+ - Deprecated in 12.0

## Declaration

```swift
func rectForCancelButton(whenCentered isCentered: Bool) -> NSRect
```

```objc
- (NSRect) rectForCancelButtonWhenCentered:(BOOL) isCentered;
```

## Parameters

- `isCentered`: A Boolean value that indicates whether the search field’s components are centered within the control. For more information, see [`centersPlaceholder`](./centersplaceholder.md).

## See Also

### Deprecated
- [var centersPlaceholder: Bool](./centersplaceholder.md)
  A Boolean value that determines whether the search field’s components are centered within the control.
- [func rectForSearchButton(whenCentered: Bool) -> NSRect](./rectforsearchbutton%28whencentered%29.md)
  The rectangle for the search button within the bounds of the search field.
- [func rectForSearchText(whenCentered: Bool) -> NSRect](./rectforsearchtext%28whencentered%29.md)
  The rectangle for the search text within the bounds of the field.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssearchfield/rectforcancelbutton(whencentered:))*