# currentItem

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The current item that determines where the search starts.

**Availability**:
- macOS 10.13+

## Declaration

```swift
var currentItem: NSAccessibilityCustomRotor.ItemResult? { get set }
```

```objc
@property (strong, nullable) NSAccessibilityCustomRotorItemResult * currentItem;
```

#### Discussion

If this value is `nil`, [`searchDirection`](./searchdirection.md) determines the current item. A search direction of [`NSAccessibilityCustomRotor.SearchDirection.next`](../searchdirection/next.md) begins the search from the first item, and a search direction of [`NSAccessibilityCustomRotor.SearchDirection.previous`](../searchdirection/previous.md) begins the search from the last item.

## See Also

### Managing the Current Item
- [NSAccessibilityCustomRotor.ItemResult](../itemresult.md)
  A target accessibility element that a custom rotor references.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsaccessibilitycustomrotor/searchparameters/currentitem)*