# reply(toShouldUnselect:)

**Framework**: Preference Panes  
**Kind**: method

Notifies the main application of the preference pane’s ability to be deselected.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.1+

## Declaration

```swift
func reply(toShouldUnselect shouldUnselect: Bool)
```

#### Discussion

If you override [`shouldUnselect`](nspreferencepane/shouldunselect.md) to return [`NSPreferencePaneUnselectReply.unselectLater`](nspreferencepaneunselectreply/unselectlater.md), you must invoke [`reply(toShouldUnselect:)`](nspreferencepane/reply(toshouldunselect:).md) when you have determined whether or not the preference pane can be deselected.

You should not override this method.

## See Also

- [func willSelect()](nspreferencepane/willselect.md)
  Notifies the preference pane that the main app is about to display the preference pane’s main view.
- [func didSelect()](nspreferencepane/didselect.md)
  Notifies the preference pane that the main app has just displayed the preference pane’s main view.
- [func willUnselect()](nspreferencepane/willunselect.md)
  Notifies the preference pane that the main app is about to stop displaying the preference pane’s main view.
- [func didUnselect()](nspreferencepane/didunselect.md)
  Notifies the preference pane that the main app has just stopped displaying the preference pane’s main view.
- [var isSelected: Bool](nspreferencepane/isselected.md)
  A Boolean value that indicates whether the preference pane is currently selected.
- [var shouldUnselect: NSPreferencePaneUnselectReply](nspreferencepane/shouldunselect.md)
  A Boolean value that indicates whether the preference pane is able to be deselected.
- [enum NSPreferencePaneUnselectReply](nspreferencepaneunselectreply.md)
  Constants that indicate the preference pane’s availability to be deselected.


---

*[View on Apple Developer](https://developer.apple.com/documentation/preferencepanes/nspreferencepane/reply(toshouldunselect:))*