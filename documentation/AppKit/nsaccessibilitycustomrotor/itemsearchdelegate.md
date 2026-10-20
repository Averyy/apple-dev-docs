# itemSearchDelegate

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The delegate for finding the next item result.

**Availability**:
- macOS 10.13+

## Declaration

```swift
weak var itemSearchDelegate: (any NSAccessibilityCustomRotorItemSearchDelegate)? { get set }
```

```objc
@property (weak) id<NSAccessibilityCustomRotorItemSearchDelegate> itemSearchDelegate;
```

## See Also

### Navigating to the Next Item
- [protocol NSAccessibilityCustomRotorItemSearchDelegate](../nsaccessibilitycustomrotoritemsearchdelegate.md)
  A delegate for a custom rotor that finds the next item result after performing a search with the specified search parameters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsaccessibilitycustomrotor/itemsearchdelegate)*