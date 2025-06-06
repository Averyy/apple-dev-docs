# orderFrontTablePanel(_:)

**Framework**: AppKit  
**Kind**: method

Brings forward a panel allowing the user to manipulate text tables in the text view.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func orderFrontTablePanel(_ sender: Any?)
```

## Parameters

- `sender`: The control sending the message. May be  .

## See Also

- [var usesFontPanel: Bool](nstextview/usesfontpanel.md)
  A Boolean value that controls whether the text views sharing the receiver’s layout manager use the Font panel and Font menu.
- [var usesFindPanel: Bool](nstextview/usesfindpanel.md)
  A Boolean value that indicates whether the receiver allows for a find panel.
- [func performFindPanelAction(Any?)](nstextview/performfindpanelaction(_:).md)
  Performs a find panel action specified by the sender’s tag.
- [func orderFrontLinkPanel(Any?)](nstextview/orderfrontlinkpanel(_:).md)
  Brings forward a panel allowing the user to manipulate links in the text view.
- [func orderFrontListPanel(Any?)](nstextview/orderfrontlistpanel(_:).md)
  Brings forward a panel allowing the user to manipulate text lists in the text view.
- [func orderFrontSpacingPanel(Any?)](nstextview/orderfrontspacingpanel(_:).md)
  Brings forward a panel allowing the user to manipulate text line heights, interline spacing, and paragraph spacing, in the text view.
- [func orderFrontSubstitutionsPanel(Any?)](nstextview/orderfrontsubstitutionspanel(_:).md)
  Brings forward a panel allowing the user to specify string substitutions in the text view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextview/orderfronttablepanel(_:))*