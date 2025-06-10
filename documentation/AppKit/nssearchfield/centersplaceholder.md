# centersPlaceholder

**Framework**: AppKit  
**Kind**: property

A Boolean value that determines whether the search field’s components are centered within the control.

**Availability**:
- macOS 10.11+

## Declaration

```swift
@MainActor
var centersPlaceholder: Bool { get set }
```

#### Discussion

When this property is set to [`true`](https://developer.apple.com/documentation/swift/true), the search field’s components become centered within the control if the field is empty and doesn’t have focus. If the field is empty when receiving focus, the centered objects animate to the edges of the control. When this property is set to [`false`](https://developer.apple.com/documentation/swift/false), the components are always at the edge. The default value is [`true`](https://developer.apple.com/documentation/swift/true).

> **Note**:  When set to [`true`](https://developer.apple.com/documentation/swift/true), [`wantsLayer`](nsview/wantslayer.md) is also [`true`](https://developer.apple.com/documentation/swift/true).

## See Also

- [func rectForCancelButton(whenCentered: Bool) -> NSRect](nssearchfield/rectforcancelbutton(whencentered:).md)
  The rectangle for the cancel button within the bounds of the search field.
- [func rectForSearchButton(whenCentered: Bool) -> NSRect](nssearchfield/rectforsearchbutton(whencentered:).md)
  The rectangle for the search button within the bounds of the search field.
- [func rectForSearchText(whenCentered: Bool) -> NSRect](nssearchfield/rectforsearchtext(whencentered:).md)
  The rectangle for the search text within the bounds of the field.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssearchfield/centersplaceholder)*