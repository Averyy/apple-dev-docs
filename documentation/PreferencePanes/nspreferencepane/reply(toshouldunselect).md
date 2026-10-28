# reply(toShouldUnselect:)

**Framework**: Preference Panes  
**Kind**: method  
**Role**: Instance Method

Notifies the main application of the preference pane’s ability to be deselected.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.1+

## Declaration

```swift
func reply(toShouldUnselect shouldUnselect: Bool)
```

```objc
- (void) replyToShouldUnselect:(BOOL) shouldUnselect;
```

## Discussion

If you override [`shouldUnselect`](./shouldunselect.md) to return [`NSPreferencePaneUnselectReply.unselectLater`](../nspreferencepaneunselectreply/unselectlater.md), you must invoke [`reply(toShouldUnselect:)`](./reply%28toshouldunselect%29.md) when you have determined whether or not the preference pane can be deselected.

You should not override this method.

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
- [var shouldUnselect: NSPreferencePaneUnselectReply](./shouldunselect.md)
  A Boolean value that indicates whether the preference pane is able to be deselected.
- [enum NSPreferencePaneUnselectReply](../nspreferencepaneunselectreply.md)
  Constants that indicate the preference pane’s availability to be deselected.


---

*[View on Apple Developer](https://developer.apple.com/documentation/preferencepanes/nspreferencepane/reply(toshouldunselect:))*