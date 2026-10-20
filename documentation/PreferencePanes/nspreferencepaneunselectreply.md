# NSPreferencePaneUnselectReply

**Framework**: Preference Panes  
**Kind**: enum  
**Role**: Enumeration

Constants that indicate the preference pane’s availability to be deselected.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.1+

## Declaration

```swift
enum NSPreferencePaneUnselectReply
```

```c
enum NSPreferencePaneUnselectReply : NSUInteger;
```

## Topics

### Replies
- [NSPreferencePaneUnselectReply.unselectCancel](./nspreferencepaneunselectreply/unselectcancel.md)
  Cancel the deselection.
- [NSPreferencePaneUnselectReply.unselectNow](./nspreferencepaneunselectreply/unselectnow.md)
  Continue the deselection.
- [NSPreferencePaneUnselectReply.unselectLater](./nspreferencepaneunselectreply/unselectlater.md)
  Delay the deselection until the preference pane invokes [`reply(toShouldUnselect:)`](./nspreferencepane/reply%28toshouldunselect%29.md).
### Initializers
- [init?(rawValue: UInt)](./nspreferencepaneunselectreply/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Selecting and Deselecting the Preference Pane
- [func willSelect()](./nspreferencepane/willselect%28%29.md)
  Notifies the preference pane that the main app is about to display the preference pane’s main view.
- [func didSelect()](./nspreferencepane/didselect%28%29.md)
  Notifies the preference pane that the main app has just displayed the preference pane’s main view.
- [func willUnselect()](./nspreferencepane/willunselect%28%29.md)
  Notifies the preference pane that the main app is about to stop displaying the preference pane’s main view.
- [func didUnselect()](./nspreferencepane/didunselect%28%29.md)
  Notifies the preference pane that the main app has just stopped displaying the preference pane’s main view.
- [var isSelected: Bool](./nspreferencepane/isselected.md)
  A Boolean value that indicates whether the preference pane is currently selected.
- [var shouldUnselect: NSPreferencePaneUnselectReply](./nspreferencepane/shouldunselect.md)
  A Boolean value that indicates whether the preference pane is able to be deselected.
- [func reply(toShouldUnselect: Bool)](./nspreferencepane/reply%28toshouldunselect%29.md)
  Notifies the main application of the preference pane’s ability to be deselected.


---

*[View on Apple Developer](https://developer.apple.com/documentation/preferencepanes/nspreferencepaneunselectreply)*