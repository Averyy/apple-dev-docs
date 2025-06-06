# preferredEdge

**Framework**: AppKit  
**Kind**: property

The edge of the button on which to display the menu when screen space is constrained.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var preferredEdge: NSRectEdge { get set }
```

#### Discussion

Possible values include [`NSMinXEdge`](https://developer.apple.com/documentation/Foundation/NSRectEdge/NSMinXEdge), [`NSMinYEdge`](https://developer.apple.com/documentation/Foundation/NSRectEdge/NSMinYEdge), [`NSMaxXEdge`](https://developer.apple.com/documentation/Foundation/NSRectEdge/NSMaxXEdge), or [`NSMaxYEdge`](https://developer.apple.com/documentation/Foundation/NSRectEdge/NSMaxYEdge). For pull-down menus, the default behavior is to position the menu under the button. The bottom edge corresponds to the value `NSMaxYEdge` for flipped views or `NSMinYEdge` for unflipped views. For most pop-up menus, the `NSPopUpButton` object attempts to show the selected item directly over the button.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspopupbutton/preferrededge)*