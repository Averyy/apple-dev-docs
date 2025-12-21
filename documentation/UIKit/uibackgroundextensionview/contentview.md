# contentView

**Framework**: UIKit  
**Kind**: property

The content view to extend to fill the `UIBackgroundExtensionView`.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
@MainActor
var contentView: UIView? { get set }
```

#### Discussion

The content view will be added as a subview of the extension view and placed within the safe area by default. See `automaticallyPlacesContentView` to customize the layout.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibackgroundextensionview/contentview)*