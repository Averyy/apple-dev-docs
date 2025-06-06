# mainView

**Framework**: Preference Panes  
**Kind**: property

The main view of the preference pane.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.1+

## Declaration

```swift
var mainView: NSView { get set }
```

#### Discussion

Subclasses should not need to override this unless they override [`loadMainView()`](nspreferencepane/loadmainview().md) or [`assignMainView()`](nspreferencepane/assignmainview().md).

## See Also

- [var bundle: Bundle](nspreferencepane/bundle.md)
  The preference pane’s bundle.
- [var mainNibName: String](nspreferencepane/mainnibname.md)
  The name of the preference pane’s nib file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/preferencepanes/nspreferencepane/mainview)*