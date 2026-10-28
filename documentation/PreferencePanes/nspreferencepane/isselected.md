# isSelected

**Framework**: Preference Panes  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the preference pane is currently selected.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.1+

## Declaration

```swift
var isSelected: Bool { get }
```

```objc
@property (readonly, getter=isSelected) BOOL selected;
```

## Discussion

[`true`](../../Swift/true.md) if preference pane is currently selected by user, [`false`](../../Swift/false.md) otherwise.

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
- [var shouldUnselect: NSPreferencePaneUnselectReply](./shouldunselect.md)
  A Boolean value that indicates whether the preference pane is able to be deselected.
- [enum NSPreferencePaneUnselectReply](../nspreferencepaneunselectreply.md)
  Constants that indicate the preference pane’s availability to be deselected.
- [func reply(toShouldUnselect: Bool)](./reply%28toshouldunselect%29.md)
  Notifies the main application of the preference pane’s ability to be deselected.


---

*[View on Apple Developer](https://developer.apple.com/documentation/preferencepanes/nspreferencepane/isselected)*