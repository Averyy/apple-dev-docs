# sharedColorPanelExists

**Framework**: AppKit  
**Kind**: property

Returns  a Boolean value indicating whether the `NSColorPanel` has been created already.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
class var sharedColorPanelExists: Bool { get }
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if the `NSColorPanel` has been created already; otherwise [`false`](https://developer.apple.com/documentation/Swift/false).

## See Also

- [class var shared: NSColorPanel](nscolorpanel/shared.md)
  Returns the shared `NSColorPanel` instance, creating it if necessary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscolorpanel/sharedcolorpanelexists)*