# centersPlaceholder

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that determines whether the search field’s components are centered within the control.

**Availability**:
- macOS 10.11+ - Deprecated in 12.0

> **Deprecated**: The placeholder centering UI design is no longer available. Setting this property is no-op.

## Declaration

```swift
var centersPlaceholder: Bool { get set }
```

```objc
@property BOOL centersPlaceholder;
```

#### Discussion

When this property is set to [`true`](../../Swift/true.md), the search field’s components become centered within the control if the field is empty and doesn’t have focus. If the field is empty when receiving focus, the centered objects animate to the edges of the control. When this property is set to [`false`](../../Swift/false.md), the components are always at the edge. The default value is [`true`](../../Swift/true.md).

> **Note**:  When set to [`true`](../../Swift/true.md), [`wantsLayer`](../nsview/wantslayer.md) is also [`true`](../../Swift/true.md).

## See Also

### Deprecated
- [func rectForCancelButton(whenCentered: Bool) -> NSRect](./rectforcancelbutton%28whencentered%29.md)
  The rectangle for the cancel button within the bounds of the search field.
- [func rectForSearchButton(whenCentered: Bool) -> NSRect](./rectforsearchbutton%28whencentered%29.md)
  The rectangle for the search button within the bounds of the search field.
- [func rectForSearchText(whenCentered: Bool) -> NSRect](./rectforsearchtext%28whencentered%29.md)
  The rectangle for the search text within the bounds of the field.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssearchfield/centersplaceholder)*