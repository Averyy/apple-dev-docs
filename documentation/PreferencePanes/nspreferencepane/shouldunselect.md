# shouldUnselect

**Framework**: Preference Panes  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the preference pane is able to be deselected.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.1+

## Declaration

```swift
var shouldUnselect: NSPreferencePaneUnselectReply { get }
```

```objc
@property (readonly) NSPreferencePaneUnselectReply shouldUnselect;
```

## Discussion

The possible values are described in Help Menu Support. The default implementation always returns [`NSPreferencePaneUnselectReply.unselectNow`](../nspreferencepaneunselectreply/unselectnow.md). Override this method if your pane needs to cancel or delay a deselect action. If you override this method to return [`NSPreferencePaneUnselectReply.unselectLater`](../nspreferencepaneunselectreply/unselectlater.md), you must invoke [`reply(toShouldUnselect:)`](./reply%28toshouldunselect%29.md) when you have determined whether or not the deselection can occur.

## See Also

### Selecting and Deselecting the Preference Pane
- [func willSelect()](./willselect%28%29.md)
  Notifies the preference pane that the main app is about to display the preference pane’s main view.
- [func didSelect()](./didselect%28%29.md)
  Notifies the preference pane that the main app has just displayed the preference pane’s main view.
- [func willUnselect()](./willunselect%28%29.md)
  Notifies the preference pane that the main app is about to stop displaying the preference pane’s main view.
- [func didUnselect()](./didunselect%28%29.md)
  Notifies the preference pane that the main app has just stopped displaying the preference pane’s main view.
- [var isSelected: Bool](./isselected.md)
  A Boolean value that indicates whether the preference pane is currently selected.
- [enum NSPreferencePaneUnselectReply](../nspreferencepaneunselectreply.md)
  Constants that indicate the preference pane’s availability to be deselected.
- [func reply(toShouldUnselect: Bool)](./reply%28toshouldunselect%29.md)
  Notifies the main application of the preference pane’s ability to be deselected.


---

*[View on Apple Developer](https://developer.apple.com/documentation/preferencepanes/nspreferencepane/shouldunselect)*