# loadMainView()

**Framework**: Preference Panes  
**Kind**: method

Loads the preference pane’s user interface into its main view.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.1+

## Declaration

```swift
func loadMainView() -> NSView
```

#### Discussion

The default implementation loads the main nib file (identified by [`mainNibName`](nspreferencepane/mainnibname.md)) and calls [`assignMainView()`](nspreferencepane/assignmainview().md) to set the main view of the preference pane. Returns the main view if successful, or `nil` otherwise.

Subclasses should rarely need to override this method. Override this method if you need to use a non-nib based technique for creating the main view. Call [`NSPreferencePane`](nspreferencepane.md) to set the main view of the preference pane before returning. Also call [`NSPreferencePane`](nspreferencepane.md), [`NSPreferencePane`](nspreferencepane.md), and [`NSPreferencePane`](nspreferencepane.md) to set the initial, first, and last keyboard focus views, respectively.

## See Also

- [func assignMainView()](nspreferencepane/assignmainview.md)
  Locates and assigns the preference pane’s main view from the nib file loaded by [`loadMainView()`](nspreferencepane/loadmainview().md).
- [func mainViewDidLoad()](nspreferencepane/mainviewdidload.md)
  Notifies the preference pane that the main view is set up and prepared to be displayed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/preferencepanes/nspreferencepane/loadmainview())*