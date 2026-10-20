# setShowsHelp(_:)

**Framework**: Security Interface  
**Kind**: method  
**Role**: Instance Method

Displays a Help button in the sheet or panel.

**Availability**:
- macOS 10.4+

## Declaration

```swift
func setShowsHelp(_ showsHelp: Bool)
```

```objc
- (void) setShowsHelp:(BOOL) showsHelp;
```

#### Discussion

When a user clicks the help button, the choose identity panel first checks the delegate for a [`certificatePanelShowHelp(_:)`](../../ObjectiveC/nsobject-swift.class/certificatepanelshowhelp%28_%29.md) method. If the delegate does not implement such a method, or the delegate method returns [`false`](../../Swift/false.md), then the [`NSHelpManager`](../../AppKit/nshelpmanager.md) method [`openHelpAnchor(_:inBook:)`](../../AppKit/nshelpmanager/openhelpanchor%28_,inbook%29.md) is called with a `nil` book and the anchor specified by the [`setHelpAnchor(_:)`](./sethelpanchor%28_%29.md) method. An exception is raised if the delegate returns [`false`](../../Swift/false.md) and there is no help anchor set.

## Parameters

- `showsHelp`: Set to [`true`](../../Swift/true.md) to display the help button. The help button is hidden by default.

## See Also

### Related Documentation
- [func chooseIdentityPanelShowHelp(SFChooseIdentityPanel!) -> Bool](../../ObjectiveC/nsobject-swift.class/chooseidentitypanelshowhelp%28_%29.md)
  Implements custom help behavior for the modal panel.
- [func openHelpAnchor(NSHelpManager.AnchorName, inBook: NSHelpManager.BookName?)](../../AppKit/nshelpmanager/openhelpanchor%28_,inbook%29.md)
  Finds and displays the text at the given anchor location in the given book.
- [func showsHelp() -> Bool](./showshelp%28%29.md)
  Indicates whether the help button is currently set to be displayed.
### Providing Help
- [func setHelpAnchor(String!)](./sethelpanchor%28_%29.md)
  Sets the help anchor string for the sheet or modal panel.
- [func helpAnchor() -> String!](./helpanchor%28%29.md)
  Returns the current help anchor string for the sheet or panel.
- [func showsHelp() -> Bool](./showshelp%28%29.md)
  Indicates whether the help button is currently set to be displayed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/securityinterface/sfchooseidentitypanel/setshowshelp(_:))*