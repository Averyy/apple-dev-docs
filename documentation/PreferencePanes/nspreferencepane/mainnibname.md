# mainNibName

**Framework**: Preference Panes  
**Kind**: property  
**Role**: Instance Property

The name of the preference pane’s nib file.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.1+

## Declaration

```swift
var mainNibName: String { get }
```

```objc
@property (strong, readonly, nonnull) NSString * mainNibName;
```

#### Discussion

The name should not include the `.nib` extension.

The default implementation returns the value of the `NSMainNibFile` key in the bundle’s information property list. If the key does not exist, it returns a default value of `@”Main”`.

## See Also

### Getting the Bundle Information
- [var bundle: Bundle](./bundle.md)
  The preference pane’s bundle.
- [var mainView: NSView](./mainview.md)
  The main view of the preference pane.


---

*[View on Apple Developer](https://developer.apple.com/documentation/preferencepanes/nspreferencepane/mainnibname)*