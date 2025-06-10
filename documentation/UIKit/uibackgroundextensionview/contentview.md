# contentView

**Framework**: UIKit  
**Kind**: property

The content view to extend to fill the `UIBackgroundExtensionView`.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
@MainActor
var contentView: UIView? { get set }
```

#### Discussion

The content view will be added as a subview of the extension view and placed within the safe area by default. See `automaticallyPlacesContentView` to customize the layout.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibackgroundextensionview/contentview)*