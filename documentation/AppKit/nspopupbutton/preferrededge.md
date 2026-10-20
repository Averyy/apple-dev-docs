# preferredEdge

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The edge of the button on which to display the menu when screen space is constrained.

**Availability**:
- macOS

## Declaration

```swift
var preferredEdge: NSRectEdge { get set }
```

```objc
@property NSRectEdge preferredEdge;
```

#### Discussion

Possible values include [`NSMinXEdge`](../../Foundation/nsrectedge/nsminxedge.md), [`NSMinYEdge`](../../Foundation/nsrectedge/nsminyedge.md), [`NSMaxXEdge`](../../Foundation/nsrectedge/nsmaxxedge.md), or [`NSMaxYEdge`](../../Foundation/nsrectedge/nsmaxyedge.md). For pull-down menus, the default behavior is to position the menu under the button. The bottom edge corresponds to the value `NSMaxYEdge` for flipped views or `NSMinYEdge` for unflipped views. For most pop-up menus, the `NSPopUpButton` object attempts to show the selected item directly over the button.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspopupbutton/preferrededge)*