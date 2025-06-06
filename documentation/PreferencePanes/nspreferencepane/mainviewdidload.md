# mainViewDidLoad()

**Framework**: Preference Panes  
**Kind**: method

Notifies the preference pane that the main view is set up and prepared to be displayed.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.1+

## Declaration

```swift
func mainViewDidLoad()
```

#### Discussion

Invoked by the default implementation of [`loadMainView()`](nspreferencepane/loadmainview().md) after the main nib file has been loaded and the main view of the preference pane has been set. The default implementation does nothing. Override this method to initialize the main view with the current preference settings.

## See Also

- [func loadMainView() -> NSView](nspreferencepane/loadmainview.md)
  Loads the preference pane’s user interface into its main view.
- [func assignMainView()](nspreferencepane/assignmainview.md)
  Locates and assigns the preference pane’s main view from the nib file loaded by [`loadMainView()`](nspreferencepane/loadmainview().md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/preferencepanes/nspreferencepane/mainviewdidload())*