# willSelect()

**Framework**: Preference Panes  
**Kind**: method

Notifies the preference pane that the main app is about to display the preference pane’s main view.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.1+

## Declaration

```swift
func willSelect()
```

#### Discussion

Default implementation does nothing. Override this method to perform actions right before the main view is displayed.

## See Also

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
- [func reply(toShouldUnselect: Bool)](nspreferencepane/reply(toshouldunselect:).md)
  Notifies the main application of the preference pane’s ability to be deselected.


---

*[View on Apple Developer](https://developer.apple.com/documentation/preferencepanes/nspreferencepane/willselect())*