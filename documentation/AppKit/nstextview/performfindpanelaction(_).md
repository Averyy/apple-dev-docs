# performFindPanelAction(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Performs a find panel action specified by the sender’s tag.

**Availability**:
- macOS

## Declaration

```swift
func performFindPanelAction(_ sender: Any?)
```

```objc
- (void) performFindPanelAction:(id) sender;
```

## Discussion

This is the generic action method for the find menu and find panel, and can be overridden to implement a custom find panel.

## Parameters

- `sender`: The control sending the message. This method sends the [`tag`](../nscontrol/tag.md) method to determine what operation to perform. The list of possible tags is provided in Constants.

## See Also

### Working with panels
- [var usesFontPanel: Bool](./usesfontpanel.md)
  A Boolean value that controls whether the text views sharing the receiver’s layout manager use the Font panel and Font menu.
- [var usesFindPanel: Bool](./usesfindpanel.md)
  A Boolean value that indicates whether the receiver allows for a find panel.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextview/performfindpanelaction(_:))*