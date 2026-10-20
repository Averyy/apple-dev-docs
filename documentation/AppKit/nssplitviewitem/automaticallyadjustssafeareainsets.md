# automaticallyAdjustsSafeAreaInsets

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

When YES, other items such as sidebars or inspectors may appear overlaid on top of this item’s `viewController` and this item’s `safeAreaInsets` will be adjusted with respect to overlaid content. Defaults to `NO`.

**Availability**:
- macOS 26.0+

## Declaration

```swift
var automaticallyAdjustsSafeAreaInsets: Bool { get set }
```

```objc
@property BOOL automaticallyAdjustsSafeAreaInsets;
```

## See Also

### Getting Auto Layout behaviors
- [var holdingPriority: NSLayoutConstraint.Priority](./holdingpriority.md)
  The priority for a split view item to hold its size.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssplitviewitem/automaticallyadjustssafeareainsets)*