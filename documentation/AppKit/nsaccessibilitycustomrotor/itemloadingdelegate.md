# itemLoadingDelegate

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The delegate for loading item results that don’t have a backing UI element at loading time.

**Availability**:
- macOS 10.13+

## Declaration

```swift
weak var itemLoadingDelegate: (any NSAccessibilityElementLoading)? { get set }
```

```objc
@property (weak, nullable) id<NSAccessibilityElementLoading> itemLoadingDelegate;
```

## See Also

### Loading the Item
- [protocol NSAccessibilityElementLoading](../nsaccessibilityelementloading.md)
  A role-based protocol that declares the minimum interface necessary for an accessibility element to support loading.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsaccessibilitycustomrotor/itemloadingdelegate)*