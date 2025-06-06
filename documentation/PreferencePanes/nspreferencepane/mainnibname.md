# mainNibName

**Framework**: Preference Panes  
**Kind**: property

The name of the preference pane’s nib file.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.1+

## Declaration

```swift
var mainNibName: String { get }
```

#### Discussion

The name should not include the `.nib` extension.

The default implementation returns the value of the `NSMainNibFile` key in the bundle’s information property list. If the key does not exist, it returns a default value of `@”Main”`.

## See Also

- [var bundle: Bundle](nspreferencepane/bundle.md)
  The preference pane’s bundle.
- [var mainView: NSView](nspreferencepane/mainview.md)
  The main view of the preference pane.


---

*[View on Apple Developer](https://developer.apple.com/documentation/preferencepanes/nspreferencepane/mainnibname)*