# isSelected

**Framework**: Preference Panes  
**Kind**: property

A Boolean value that indicates whether the preference pane is currently selected.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.1+

## Declaration

```swift
var isSelected: Bool { get }
```

#### Discussion

[`true`](https://developer.apple.com/documentation/swift/true) if preference pane is currently selected by user, [`false`](https://developer.apple.com/documentation/swift/false) otherwise.

## See Also

- [func willSelect()](nspreferencepane/willselect.md)
  Notifies the preference pane that the main app is about to display the preference pane’s main view.
- [func didSelect()](nspreferencepane/didselect.md)
  Notifies the preference pane that the main app has just displayed the preference pane’s main view.
- [func willUnselect()](nspreferencepane/willunselect.md)
  Notifies the preference pane that the main app is about to stop displaying the preference pane’s main view.
- [func didUnselect()](nspreferencepane/didunselect.md)
  Notifies the preference pane that the main app has just stopped displaying the preference pane’s main view.
- [var shouldUnselect: NSPreferencePaneUnselectReply](nspreferencepane/shouldunselect.md)
  A Boolean value that indicates whether the preference pane is able to be deselected.
- [enum NSPreferencePaneUnselectReply](nspreferencepaneunselectreply.md)
  Constants that indicate the preference pane’s availability to be deselected.
- [func reply(toShouldUnselect: Bool)](nspreferencepane/reply(toshouldunselect:).md)
  Notifies the main application of the preference pane’s ability to be deselected.


---

*[View on Apple Developer](https://developer.apple.com/documentation/preferencepanes/nspreferencepane/isselected)*