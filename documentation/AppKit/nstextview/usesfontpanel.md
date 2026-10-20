# usesFontPanel

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that controls whether the text views sharing the receiver’s layout manager use the Font panel and Font menu.

**Availability**:
- macOS

## Declaration

```swift
var usesFontPanel: Bool { get set }
```

```objc
@property BOOL usesFontPanel;
```

#### Discussion

[`true`](../../Swift/true.md) to make the text views sharing the receiver’s layout manager respond to messages from the Font panel and from the Font menu, and update the Font panel with the selection font whenever it changes, [`false`](../../Swift/false.md) to disallow character attribute changes.

## See Also

### Related Documentation
- [var rangeForUserCharacterAttributeChange: NSRange](./rangeforusercharacterattributechange.md)
  The range of characters affected by an action method that changes character (not paragraph) attributes.
### Working with panels
- [var usesFindPanel: Bool](./usesfindpanel.md)
  A Boolean value that indicates whether the receiver allows for a find panel.
- [func performFindPanelAction(Any?)](./performfindpanelaction%28_%29.md)
  Performs a find panel action specified by the sender’s tag.
- [func orderFrontLinkPanel(Any?)](./orderfrontlinkpanel%28_%29.md)
  Brings forward a panel allowing the user to manipulate links in the text view.
- [func orderFrontListPanel(Any?)](./orderfrontlistpanel%28_%29.md)
  Brings forward a panel allowing the user to manipulate text lists in the text view.
- [func orderFrontSpacingPanel(Any?)](./orderfrontspacingpanel%28_%29.md)
  Brings forward a panel allowing the user to manipulate text line heights, interline spacing, and paragraph spacing, in the text view.
- [func orderFrontTablePanel(Any?)](./orderfronttablepanel%28_%29.md)
  Brings forward a panel allowing the user to manipulate text tables in the text view.
- [func orderFrontSubstitutionsPanel(Any?)](./orderfrontsubstitutionspanel%28_%29.md)
  Brings forward a panel allowing the user to specify string substitutions in the text view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextview/usesfontpanel)*