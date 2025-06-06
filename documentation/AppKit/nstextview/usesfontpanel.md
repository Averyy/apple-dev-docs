# usesFontPanel

**Framework**: AppKit  
**Kind**: property

A Boolean value that controls whether the text views sharing the receiver’s layout manager use the Font panel and Font menu.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var usesFontPanel: Bool { get set }
```

#### Discussion

[`true`](https://developer.apple.com/documentation/swift/true) to make the text views sharing the receiver’s layout manager respond to messages from the Font panel and from the Font menu, and update the Font panel with the selection font whenever it changes, [`false`](https://developer.apple.com/documentation/swift/false) to disallow character attribute changes.

## See Also

- [var rangeForUserCharacterAttributeChange: NSRange](nstextview/rangeforusercharacterattributechange.md)
  The range of characters affected by an action method that changes character (not paragraph) attributes.
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
- [func orderFrontTablePanel(Any?)](nstextview/orderfronttablepanel(_:).md)
  Brings forward a panel allowing the user to manipulate text tables in the text view.
- [func orderFrontSubstitutionsPanel(Any?)](nstextview/orderfrontsubstitutionspanel(_:).md)
  Brings forward a panel allowing the user to specify string substitutions in the text view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextview/usesfontpanel)*