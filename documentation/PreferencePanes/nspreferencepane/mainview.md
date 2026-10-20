# mainView

**Framework**: Preference Panes  
**Kind**: property  
**Role**: Instance Property

The main view of the preference pane.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.1+

## Declaration

```swift
var mainView: NSView { get set }
```

```objc
@property (strong, nonnull) NSView * mainView;
```

#### Discussion

Subclasses should not need to override this unless they override [`loadMainView()`](./loadmainview%28%29.md) or [`assignMainView()`](./assignmainview%28%29.md).

## See Also

### Getting the Bundle Information
- [var bundle: Bundle](./bundle.md)
  The preference pane’s bundle.
- [var mainNibName: String](./mainnibname.md)
  The name of the preference pane’s nib file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/preferencepanes/nspreferencepane/mainview)*