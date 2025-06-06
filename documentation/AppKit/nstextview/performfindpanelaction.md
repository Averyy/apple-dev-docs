# performFindPanelAction(_:)

**Framework**: AppKit  
**Kind**: method

Performs a find panel action specified by the sender’s tag.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func performFindPanelAction(_ sender: Any?)
```

#### Discussion

This is the generic action method for the find menu and find panel, and can be overridden to implement a custom find panel.

## Parameters

- `sender`: The control sending the message. This method sends the   method to determine what operation to perform. The list of possible tags is provided in Constants.

## See Also

- [var usesFontPanel: Bool](nstextview/usesfontpanel.md)
  A Boolean value that controls whether the text views sharing the receiver’s layout manager use the Font panel and Font menu.
- [var usesFindPanel: Bool](nstextview/usesfindpanel.md)
  A Boolean value that indicates whether the receiver allows for a find panel.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextview/performfindpanelaction(_:))*