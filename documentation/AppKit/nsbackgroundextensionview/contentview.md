# contentView

**Framework**: AppKit  
**Kind**: property

The content view to extend to fill the `NSBackgroundExtensionView`.

**Availability**:
- macOS 26.0+ (Beta)

## Declaration

```swift
@MainActor
var contentView: NSView? { get set }
```

#### Discussion

The content view will be added as a subview of the extension view and placed within the safe area by default. See `automaticallyPlacesContentView` to customize the layout.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbackgroundextensionview/contentview)*