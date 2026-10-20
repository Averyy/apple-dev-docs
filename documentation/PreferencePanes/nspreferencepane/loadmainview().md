# loadMainView()

**Framework**: Preference Panes  
**Kind**: method  
**Role**: Instance Method

Loads the preference pane’s user interface into its main view.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.1+

## Declaration

```swift
func loadMainView() -> NSView
```

```objc
- (NSView *) loadMainView;
```

#### Discussion

The default implementation loads the main nib file (identified by [`mainNibName`](./mainnibname.md)) and calls [`assignMainView()`](./assignmainview%28%29.md) to set the main view of the preference pane. Returns the main view if successful, or `nil` otherwise.

Subclasses should rarely need to override this method. Override this method if you need to use a non-nib based technique for creating the main view. Call [`NSPreferencePane`](../nspreferencepane.md) to set the main view of the preference pane before returning. Also call [`NSPreferencePane`](../nspreferencepane.md), [`NSPreferencePane`](../nspreferencepane.md), and [`NSPreferencePane`](../nspreferencepane.md) to set the initial, first, and last keyboard focus views, respectively.

## See Also

### Loading the Main View
- [func assignMainView()](./assignmainview%28%29.md)
  Locates and assigns the preference pane’s main view from the nib file loaded by [`loadMainView()`](./loadmainview%28%29.md).
- [func mainViewDidLoad()](./mainviewdidload%28%29.md)
  Notifies the preference pane that the main view is set up and prepared to be displayed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/preferencepanes/nspreferencepane/loadmainview())*