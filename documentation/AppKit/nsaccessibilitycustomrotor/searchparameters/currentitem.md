# currentItem

**Framework**: AppKit  
**Kind**: property

The current item that determines where the search starts.

**Availability**:
- macOS 10.13+

## Declaration

```swift
var currentItem: NSAccessibilityCustomRotor.ItemResult? { get set }
```

#### Discussion

If this value is `nil`, [`searchDirection`](nsaccessibilitycustomrotor/searchparameters/searchdirection.md) determines the current item. A search direction of [`NSAccessibilityCustomRotor.SearchDirection.next`](nsaccessibilitycustomrotor/searchdirection/next.md) begins the search from the first item, and a search direction of [`NSAccessibilityCustomRotor.SearchDirection.previous`](nsaccessibilitycustomrotor/searchdirection/previous.md) begins the search from the last item.

## See Also

- [NSAccessibilityCustomRotor.ItemResult](nsaccessibilitycustomrotor/itemresult.md)
  A target accessibility element that a custom rotor references.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsaccessibilitycustomrotor/searchparameters/currentitem)*