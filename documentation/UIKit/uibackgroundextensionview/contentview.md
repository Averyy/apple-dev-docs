# contentView

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The content view to extend to fill the `UIBackgroundExtensionView`.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
var contentView: UIView? { get set }
```

```objc
@property (nonatomic, strong, nullable) UIView * contentView;
```

#### Discussion

The content view will be added as a subview of the extension view and placed within the safe area by default. See `automaticallyPlacesContentView` to customize the layout.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibackgroundextensionview/contentview)*