# usesFindPanel

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the receiver allows for a find panel.

**Availability**:
- macOS

## Declaration

```swift
var usesFindPanel: Bool { get set }
```

```objc
@property BOOL usesFindPanel;
```

#### Discussion

[`true`](../../Swift/true.md) to allow the use of a find panel, [`false`](../../Swift/false.md) otherwise. A text view can use either a find panel or a find bar. If [`usesFindPanel`](./usesfindpanel.md) is set to [`true`](../../Swift/true.md), [`usesFindBar`](./usesfindbar.md) is set to [`false`](../../Swift/false.md) and vice versa.

## See Also

### Related Documentation
- [var usesFindBar: Bool](./usesfindbar.md)
  A Boolean value that indicates whether to use the find bar for this text view.
### Working with panels
- [var usesFontPanel: Bool](./usesfontpanel.md)
  A Boolean value that controls whether the text views sharing the receiver’s layout manager use the Font panel and Font menu.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextview/usesfindpanel)*