# mainViewDidLoad()

**Framework**: Preference Panes  
**Kind**: method  
**Role**: Instance Method

Notifies the preference pane that the main view is set up and prepared to be displayed.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.1+

## Declaration

```swift
func mainViewDidLoad()
```

```objc
- (void) mainViewDidLoad;
```

#### Discussion

Invoked by the default implementation of [`loadMainView()`](./loadmainview%28%29.md) after the main nib file has been loaded and the main view of the preference pane has been set. The default implementation does nothing. Override this method to initialize the main view with the current preference settings.

## See Also

### Loading the Main View
- [func loadMainView() -> NSView](./loadmainview%28%29.md)
  Loads the preference pane’s user interface into its main view.
- [func assignMainView()](./assignmainview%28%29.md)
  Locates and assigns the preference pane’s main view from the nib file loaded by [`loadMainView()`](./loadmainview%28%29.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/preferencepanes/nspreferencepane/mainviewdidload())*