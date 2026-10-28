# sharedColorPanelExists

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

Returns  a Boolean value indicating whether the `NSColorPanel` has been created already.

**Availability**:
- macOS

## Declaration

```swift
class var sharedColorPanelExists: Bool { get }
```

```objc
@property (class, readonly) BOOL sharedColorPanelExists;
```

## Return Value

[`true`](../../Swift/true.md) if the `NSColorPanel` has been created already; otherwise [`false`](../../Swift/false.md).

## See Also

### Obtaining the shared color panel
- [class var shared: NSColorPanel](./shared.md)
  Returns the shared `NSColorPanel` instance, creating it if necessary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscolorpanel/sharedcolorpanelexists)*