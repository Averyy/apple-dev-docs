# assignMainView()

**Framework**: Preference Panes  
**Kind**: method

Locates and assigns the preference pane’s main view from the nib file loaded by [`loadMainView()`](nspreferencepane/loadmainview().md).

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.1+

## Declaration

```swift
func assignMainView()
```

#### Discussion

The default implementation sets the receiver’s main view to the content view of the window referenced by the `_window` outlet. Before returning, [`assignMainView()`](nspreferencepane/assignmainview().md) releases the window and sets the `_window` outlet to `nil`. Returns the main view if successful, `nil` otherwise.

Override this method if your main view is located in the nib file loaded by [`loadMainView()`](nspreferencepane/loadmainview().md), but is not the content view of a window in the file. Call [`NSPreferencePane`](nspreferencepane.md) to set the main view of the preference pane before returning. Also call [`NSPreferencePane`](nspreferencepane.md), [`NSPreferencePane`](nspreferencepane.md), and [`NSPreferencePane`](nspreferencepane.md) to set the initial, first, and last keyboard focus views, respectively.

## See Also

- [func loadMainView() -> NSView](nspreferencepane/loadmainview.md)
  Loads the preference pane’s user interface into its main view.
- [func mainViewDidLoad()](nspreferencepane/mainviewdidload.md)
  Notifies the preference pane that the main view is set up and prepared to be displayed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/preferencepanes/nspreferencepane/assignmainview())*