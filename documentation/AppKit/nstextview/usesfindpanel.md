# usesFindPanel

**Framework**: AppKit  
**Kind**: property

A Boolean value that indicates whether the receiver allows for a find panel.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var usesFindPanel: Bool { get set }
```

#### Discussion

[`true`](https://developer.apple.com/documentation/Swift/true) to allow the use of a find panel, [`false`](https://developer.apple.com/documentation/Swift/false) otherwise. A text view can use either a find panel or a find bar. If [`usesFindPanel`](nstextview/usesfindpanel.md) is set to [`true`](https://developer.apple.com/documentation/Swift/true), [`usesFindBar`](nstextview/usesfindbar.md) is set to [`false`](https://developer.apple.com/documentation/Swift/false) and vice versa.

## See Also

- [var usesFindBar: Bool](nstextview/usesfindbar.md)
  A Boolean value that indicates whether to use the find bar for this text view.
- [var usesFontPanel: Bool](nstextview/usesfontpanel.md)
  A Boolean value that controls whether the text views sharing the receiver’s layout manager use the Font panel and Font menu.
- [func performFindPanelAction(Any?)](nstextview/performfindpanelaction(_:).md)
  Performs a find panel action specified by the sender’s tag.
- [func orderFrontLinkPanel(Any?)](nstextview/orderfrontlinkpanel(_:).md)
  Brings forward a panel allowing the user to manipulate links in the text view.
- [func orderFrontListPanel(Any?)](nstextview/orderfrontlistpanel(_:).md)
  Brings forward a panel allowing the user to manipulate text lists in the text view.
- [func orderFrontSpacingPanel(Any?)](nstextview/orderfrontspacingpanel(_:).md)
  Brings forward a panel allowing the user to manipulate text line heights, interline spacing, and paragraph spacing, in the text view.
- [func orderFrontTablePanel(Any?)](nstextview/orderfronttablepanel(_:).md)
  Brings forward a panel allowing the user to manipulate text tables in the text view.
- [func orderFrontSubstitutionsPanel(Any?)](nstextview/orderfrontsubstitutionspanel(_:).md)
  Brings forward a panel allowing the user to specify string substitutions in the text view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextview/usesfindpanel)*