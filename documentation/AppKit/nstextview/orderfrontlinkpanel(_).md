# orderFrontLinkPanel(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Brings forward a panel allowing the user to manipulate links in the text view.

**Availability**:
- macOS

## Declaration

```swift
func orderFrontLinkPanel(_ sender: Any?)
```

```objc
- (void) orderFrontLinkPanel:(id) sender;
```

## Parameters

- `sender`: The control sending the message. May be `nil`.

## See Also

### Working with panels
- [var usesFontPanel: Bool](./usesfontpanel.md)
  A Boolean value that controls whether the text views sharing the receiver’s layout manager use the Font panel and Font menu.
- [var usesFindPanel: Bool](./usesfindpanel.md)
  A Boolean value that indicates whether the receiver allows for a find panel.
- [func performFindPanelAction(Any?)](./performfindpanelaction%28_%29.md)
  Performs a find panel action specified by the sender’s tag.
- [func orderFrontListPanel(Any?)](./orderfrontlistpanel%28_%29.md)
  Brings forward a panel allowing the user to manipulate text lists in the text view.
- [func orderFrontSpacingPanel(Any?)](./orderfrontspacingpanel%28_%29.md)
  Brings forward a panel allowing the user to manipulate text line heights, interline spacing, and paragraph spacing, in the text view.
- [func orderFrontTablePanel(Any?)](./orderfronttablepanel%28_%29.md)
  Brings forward a panel allowing the user to manipulate text tables in the text view.
- [func orderFrontSubstitutionsPanel(Any?)](./orderfrontsubstitutionspanel%28_%29.md)
  Brings forward a panel allowing the user to specify string substitutions in the text view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextview/orderfrontlinkpanel(_:))*