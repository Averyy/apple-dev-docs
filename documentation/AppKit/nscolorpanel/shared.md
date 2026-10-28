# shared

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

Returns the shared `NSColorPanel` instance, creating it if necessary.

**Availability**:
- macOS

## Declaration

```swift
class var shared: NSColorPanel { get }
```

```objc
@property (class, strong, readonly) NSColorPanel * sharedColorPanel;
```

## Return Value

The shared `NSColorPanel` instance.

## See Also

### Related Documentation
- [class NSColorPanel](../nscolorpanel.md)
  A standard user interface for selecting color in an app.
### Obtaining the shared color panel
- [class var sharedColorPanelExists: Bool](./sharedcolorpanelexists.md)
  Returns  a Boolean value indicating whether the `NSColorPanel` has been created already.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscolorpanel/shared)*