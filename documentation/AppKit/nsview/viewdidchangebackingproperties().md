# viewDidChangeBackingProperties()

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Responds when the view’s backing store properties change.

**Availability**:
- macOS 10.7+

## Declaration

```swift
func viewDidChangeBackingProperties()
```

```objc
- (void) viewDidChangeBackingProperties;
```

#### Discussion

The view gets this message when the backing store scale or color space changes. Provide an implementation if you need to swap assets or make other adjustments when a view’s backing store properties change.

## See Also

### Responding to Appearance Changes
- [func viewDidChangeEffectiveAppearance()](./viewdidchangeeffectiveappearance%28%29.md)
  Informs the view that its effective appearance changed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/viewdidchangebackingproperties())*